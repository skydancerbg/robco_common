#!/bin/bash

sleep 5

sudo chmod 666 /dev/ttyUSB0

sudo modprobe gspca_kinect

gnome-terminal \
  --tab-with-profile=halt -e '/bin/bash -c "\
    cd ~/WebUI/webui; \
    python manage.py runserver 0.0.0.0:8000; \
  " ' \
  --tab-with-profile=halt -e '/bin/bash -c "\
    cd ~/WebUI/nodejs_channel_server; \
    node channel_server.js; \
  " ' \
  --tab-with-profile=halt -e '/bin/bash -i -c "\
    cd ~/WebUI/startup_script; \
    ./ros.sh restart\
  " '

