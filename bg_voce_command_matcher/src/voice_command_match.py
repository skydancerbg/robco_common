#!/usr/bin/env python
'''voice_command_recognize ROS Node'''
import rospy
from std_msgs.msg import String

class VoiceCommandRecognizer(object):
    '''
 voice_command_recognize


    '''

    def __init__(self):

        super(VoiceCommandRecognizer, self).__init__()

        rospy.init_node('voice_command_recognize', anonymous=True)
        # We don't have to run the script very fast
        self.rate = rospy.get_param("~rate", 5)
        rate = rospy.Rate(self.rate)

        # rospy.on_shutdown(self.cleanup)

        self._sttbg_recognized_text_topic = '/sttbg_ros/stt_text'
        self._output_command_topic = '/voce_command'
        self._last_incomming_stt_text = None
        self._command = None
        # self._sttbg_response_topic = '/sttbg_ros/response'

        # A mapping from keywords or phrases to commands
        self.keywords_to_command = {'stop': ['stop', 'halt', 'abort', 'kill', 'panic', 'off', 'freeze', 'shut down', 'turn off', 'help', 'help me'],
                                    'slower': ['slow down', 'slower'],
                                    'faster': ['speed up', 'faster'],
                                    'forward': ['forward', 'ahead', 'straight'],
                                    'backward': ['back', 'backward', 'back up'],
                                    'rotate left': ['rotate left'],
                                    'rotate right': ['rotate right'],
                                    'turn left': ['turn left'],
                                    'turn right': ['turn right'],
                                    'quarter': ['quarter speed'],
                                    'half': ['half speed'],
                                    'full': ['full speed'],
                                    'pause': ['pause speech'],
                                    'continue': ['continue speech']}


        #create publisher passing it the '/voce_command' output topic and msg_type
        self.matched_command_pub = rospy.Publisher(self._output_command_topic, String, queue_size=1)

        # self.pub_ttsbg_text = ProxyPublisher({self._sttbg_text_to_recognize_topic: String})
        # #create publisher passing it the ttsbg_topic and msg_type
        # self.cmd_vel_pub = rospy.Publisher(self._sttbg_command_topic, String, queue_size=1)

        # self.pub_ttsbg_command = ProxyPublisher({self._sttbg_command_topic: String})

        #create subscriber to the incomming recognized commands
        rospy.Subscriber("/sttbg_ros/stt_text", String, self.incomming_text_callback)
        rospy.loginfo("Command recognizer from the Speech To Text input topic is ready to receive voice commands for processing")



    def incomming_text_callback(self, data):
        '''voice_command_recognize Callback Function'''
        # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        rospy.loginfo("New incomming text from the STT topic: %s", data.data)
        self._last_incomming_stt_text = data.data

        # Get the motion command from the recognized phrase
        command = self.get_command(self._last_incomming_stt_text)
        command = self.get_command(data.data)
        # rospy.loginfo("Command output from get command: %s", command)

        if command != '':
            # Log the command to the screen
            rospy.loginfo("Publishing the matched command: %s", command)
            # Publish matcehd command to the command ouptut topic
            self.matched_command_pub.publish(command)
        else:
            # Publish matcehd command to the command ouptut topic
            # self.matched_command_pub.publish("No match found for the incomming string: %s", data)

            # No need to publish om the output topic!
            # self.matched_command_pub.publish("nomatch")
            rospy.loginfo("No match found for the incomming string: %s", data.data)

    # def command_recognizer():
    #     pass

    def get_command(self, data):
        '''Attempts to match the incomming word or phrase to the keywords_to_command dictionary'''

        # Attempt to match the recognized word or phrase to the
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
        VoiceCommandRecognizer()
        rospy.loginfo("Voice command matching started.")        
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("Voice command matching terminated.")


# List of possible commands:
# pause speech
# continue speech
# move forward
# move backward
# move back
# move left
# move right
# go forward
# go backward
# go back
# go left
# go right
# go straight
# come forward
# come backward
# come left
# come right
# turn left
# turn right
# rotate left
# rotate right
# faster
# speed up
# slower
# slow down
# quarter speed
# half speed
# full speed
# stop
# stop now
# halt
# abort
# kill
# panic
# help
# help me
# freeze
# turn off
# shut down
# cancel