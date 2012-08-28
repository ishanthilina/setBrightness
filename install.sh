#!/bin/bash

echo "Begining installation"

INSTALLATION_DIR=".setBrightness"
CURRENT_DIR=$PWD
START_APP_DIR=$HOME"/.config/autostart"

#move to home
cd ~

#Check for the existence of the installation folder
if [ ! -d "$INSTALLATION_DIR" ]; then
    #create the target folder
    mkdir $INSTALLATION_DIR
    #copy the source file
    cp $CURRENT_DIR"/src/setBrightness.py" $INSTALLATION_DIR
    #copy the config file
    cp $CURRENT_DIR"/conf/config.cfg" $INSTALLATION_DIR


    #check for the existence of the startup app folder
    if [ -d "$START_APP_DIR" ]; then
	#copy the auto start file
	cp $CURRENT_DIR"/conf/setBrightness.desktop" $START_APP_DIR
		
    else
	#create the directory
	mkdir $START_APP_DIR
	#copy the auto start file
	cp $CURRENT_DIR"/conf/setBrightness.desktop" $START_APP_DIR

    fi
    echo "Installation finished successfully!"
        
else
    echo "The target directory for installation," $INSTALLATION_DIR ",already exists in your home folder"
    echo "Exiting installation."
    
fi
