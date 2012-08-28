#!/bin/bash

INSTALLATION_DIR=".setBrightness"

#move to home
#cd ~

#Check for the existence of the installation folder
if [ ! -d "~/$INSTALLATION_DIR" ]; then
    #create the target folder
    mkdir $INSTALLATION_DIR
    
    
else
    echo "The target directory for installation," $INSTALLATION_DIR ",already exists in your home folder"
    echo "Exiting installation."
    
fi
