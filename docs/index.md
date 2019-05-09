# Documentation

### Setup Script To Autorun At Login

#### Ubuntu / Gnome

You are going to need an intermediate script that grabs the necessary environment variables. See [this](https://askubuntu.com/questions/483687/editing-gsettings-unsuccesful-when-initiated-from-cron) link for further info.

    #!/bin/bash

    PID=$(pgrep gnome-session)
    export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-);/path/to/script.py
