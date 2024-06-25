# This is my intership project
# I will show each and every step
# 1. Setup
#   Very first step is create a folder anywhere on your system
#   Now open this folder in VScode
#   Create a Readme.md file in it
#   Open new terminal gitbash or command promt
#   now initialize the git by giving the command git init
#   Create a git repository on github
#   Now you can push the changes done in vscode to git repository directly by using source control or we can use git add .
#   we can commit by using git commit -m "my first commit"
#   Now by clicking on sync changes option we get a option to choose the repository we have to choose the public repository and a public repository get created on github for the same foder name 
#   We can create the file on github itself by clicking + option on github
# create a gitignore file choose python template and commit on github itself
# create a licence file on github
# now fetch all this changes done on github on your local system by using git pull command on your terminal
# Now we have to create evironment and other installations but if you don't wan t to do it manually then we have to create a script for that we will create a file init_setup.sh here sh (shell) we use this script because if i dont want to write a mannual command and want to automate that process so we will write all commands in shell script this is a linux system script we can't use this in windows unless and untill we use git bash
#  Now use bash init_setup.sh command in bash terminal
# some times the source activate command in shell script don't work in this case we need to activate the environment by giving manual command source activate ./env
#  Now we want to add more files to carry out the other function instead of creating the various files manually we can write a script or code so that all the required files withe their extension gets in one shot, for this purpose we have to create a template.py file and in which we have to specify the required files and other stuff you can also copy the script from the end-to-end_project repository and now you have to run template.py and we get all the required files we have the architecture struture which is also called as boiller plate which is universal data science architecture boiller plate is noting which is predefined file

# init file:- we can see init file in every folder the reason is inside a folder if we have file/module/.py file this complte thing is called as package in the python Eg:- folder-> src-.py file- class/def --- (src - _init__.py - class/def) in this way we can create our own packages, How python knows that it is your local package so to justify this thing we use __init__.py this is a rule from python side if you want to crate your own local package you have to create __init__.py file 

# Now we have our own package and we need to install it so what we can do is we can use -e . in requirements.txt with other packages and now install the requirements using pip install -r requirements.txt here we can see the local file aswell

# Now we can see all the packages by using pip list command