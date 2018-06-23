#!/bin/sh

### Welcome to piWeatherman Installer

### We will just install some basic tkinter libraries and requirements
### on your raspberry pi to get you up and running. So sit back and enjoy
### your very own raspberry pi weather station!

printf 'piWeatherman - Install basic tkinter libraries and requirements '
printf '\nFor more information, visit us at https://github.com/abhishtagatya/typeDef'
printf '\n\nIssue and report bugs and misinformation in the github issue page\n'


install_module() {
  # Change this if you are not running Linux or Raspbian (Debian based distribution)
  # TODO : Set installer to be os independent

  # Install Packages
  while read package; do
    sudo apt-get install $package
  done < packages.txt

  # Install Pip Modules
  while read module; do
    sudo pip install $module --upgrade
  done < requirements.txt

}

pingtest=$(ping -c 1 -W 5 8.8.8.8 > /dev/null)
if [ $? -eq 0 ]; then
  install_module
else
  printf 'You are not connected to the internet\n'
  printf 'Please connect to the internet to use the application\n'
  exit 1
fi


printf '\nLooks like all your dependencies has been installed...'
printf '\nProceeding to application, make sure your datetime is correct'

python app.py

printf '\nThank you for using piWeatherman\n'

# Deletes Caches
find . -name \*.pyc -delete

exit 0
