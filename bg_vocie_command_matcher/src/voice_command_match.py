#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''voice_command_match ROS Node'''
import rospy
import os
import json
from io import open
from std_msgs.msg import String

#     #################################
#     # 
#     # Created by Stefan 
#     # SRG - Service Robotics Group Bulgaria
#     # Version 1.0 from Apr. 7th, 2019.
#     #
#     #################################

class VoiceCommandMatcher(object):
    '''
    Reads dictionarry with mapping from keywords or phrases to commands from ../config/dictionary.json file
    Than, it attempts to match the incomming (on topic /sttbg_ros/stt_text) recognized by the STT word or phrase, to the
    keywords_to_command dictionary and publish the appropriate command to the /robco/command topic
    '''

    def __init__(self):

        super(VoiceCommandMatcher, self).__init__()

        # rospy.init_node('VoiceCommandMatcher', anonymous=True)
        rospy.init_node('VoiceCommandMatcher')

        # Set publish rate
        self.rate = rospy.get_param("~rate", 5)
        rate = rospy.Rate(self.rate)

        # rospy.on_shutdown(self.cleanup)

        self._sttbg_recognized_text_topic = '/sttbg_ros/stt_text'
        self._output_command_topic = '/robco/command'
        self._last_incomming_stt_text = None
        self._command = None


        # Find the absolute path to this python file
        our_python_script_path = os.path.abspath(os.path.dirname(__file__))

        # relative path to the file, which is in another folder (on the same level as the folder this python file is in)
        #  i.e. <package name>/src/<this python File> and <package name>/config/dictionary.json
        new_path = os.path.join(our_python_script_path, "../config/dictionary.json")

        ##########################################################################################
        ###### IMPORTANT when you add new commands to dictionary.json follow the jason syntax!
        ###### Copy and paste the file contents to https://jsonformatter.curiousconcept.com/
        ###### for online check for valid jason in the file!
        ##########################################################################################

        # Read from file /config/dictionary.txt the dictionary values for mapping from keywords or phrases to commands
        with open(new_path, mode='r', encoding='utf-8') as jason_file:
            self.keywords_to_command = json.loads(jason_file.read())

        # Pretty Printing JSON string back
        # print(json.dumps(self.keywords_to_command, indent = 4, sort_keys=True))


        # Create publisher passing it the /robco/command output topic and msg_type
        self.matched_command_pub = rospy.Publisher(self._output_command_topic, String, queue_size=1)


        # Create subscriber to the incomming on recognized by stt text
        rospy.Subscriber("/sttbg_ros/stt_text", String, self.incomming_text_callback)



    def incomming_text_callback(self, data):
        '''voice_command_recognize Callback Function'''
        # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        rospy.loginfo("New incomming text from the STT topic: %s", data.data)
        self._last_incomming_stt_text = data.data.decode('utf-8')

        # Get the command from the incomming recognized stt phrase
        command = self.get_command(self._last_incomming_stt_text)
        # command = self.get_command(data.data)
        # rospy.loginfo("Command output from get command: %s", command)

        if command != '':
            # Log the command to the screen
            rospy.loginfo("Publishing the matched command: %s", command)
            # Publish matched command to the command ouptut topic
            self.matched_command_pub.publish(command)
        else:

            # No need to publish om the output topic!
            # self.matched_command_pub.publish("nomatch")
            rospy.loginfo("No match found for the incomming string: %s", data.data)


    def get_command(self, data):
        '''Attempts to match the incomming word or phrase to the keywords_to_command dictionary'''

        # Attempt to match the recognized by stt word or phrase to the
        # keywords_to_command dictionary and return the appropriate
        # command
        for (command, keywords) in self.keywords_to_command.iteritems():
            for word in keywords:
                # rospy.loginfo("Vatre v get command self._last_incomming_stt_text: %s", self._last_incomming_stt_text)
                # rospy.loginfo("Vatre v get command word: %s", word)
                if data.find(word) > -1:

                    return command




if __name__ == "__main__":
    try:
        VoiceCommandMatcher()
        # Anounce that we are ready to operate to the terminal:
        rospy.loginfo(" ")
        rospy.loginfo("###########################################################")
        rospy.loginfo("Command matcher is ready to receive STT recognized text")
        rospy.loginfo("on /sttbg_ros/stt_text topic for matching to robot commands")
        rospy.loginfo("###########################################################")
        rospy.loginfo(" ")

        rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo(" ")
        rospy.loginfo("Voice command matching terminated.")
