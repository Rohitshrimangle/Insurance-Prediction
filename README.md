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
#  Now we want to add more files to carry out the other function instead of creating the various files manually we can write a script or code so that all the required files with their extension gets in one shot, for this purpose we have to create a template.py file and in which we have to specify the required files and other stuff you can also copy the script from the end-to-end_project repository and now you have to run template.py and we get all the required files we have the architecture struture which is also called as boiller plate which is universal, data science architecture boiller plate is noting which is predefined file

# init file:- we can see init file in every folder the reason is inside a folder if we have file/module/.py file this complte thing is called as package in the python Eg:- folder-> src-.py file- class/def --- (src - _init__.py - class/def) in this way we can create our own packages, How python knows that it is your local package so to justify this thing we use __init__.py this is a rule from python side if you want to create your own local package you have to create __init__.py file 

# Now we have our own package and we need to install it so what we can do is we can use -e . in requirements.txt with other packages and now install the requirements using pip install -r requirements.txt here we can see the local file aswell

# Now we can see all the packages by using pip list command

# Now we can add the csv file in the data folder and start working on EDA on notebook before that install the ipykernel and select the interpreter

# Now next step is start working on EDA preprocessing where we clean, arrange or mange the data in orgnized manner. We work on the features which are important and those feature are not of any use we remove them. EDA is very interesting job here we can play with the data such as we get to the info about data how manny coloumns, rows are there how many null rows or columns which feature is having maximun null values based on it we decide wheather that feature is important or not and also we cheek lineartiy between features and decides which is independent and dependent features. We can aslo explore the data in visual manner with the help of seaborn and matplotlib libraries overall feature engineering is done.

# Next is modelling here after completing the EDA we have to decide which algorithm is best suitable for the model based on the evaluation parameters such r2 score, mse, rmse, mae etc

# Next is components and pipeline here, in EDA and modelling is done in ipynb i.e notebooks which are cellular in nature but we need to do modular codeing and in modular coding we can't code in celluar ipynb file we need to code in .py python file here in modular coding we sagregate the task in multiple files.

# Start working on Data Ingestion, Data Transformation, Model Trainer, Logger and exception file

# utlis is a helper file it is a helping entity.

# Logger file is used to store the records of changes done in files with date and time with message.

# mentain a rough ipynb file to experiment or code something before coding it into .py file

# We had done exception handling in the exception.py file for the errors

# Data ingestion - import libraries in it pandas numpy local InsurancePrediction from sklearn train_test_split dataclasses and pathlib from path

# Pipeline:- Now we have to collect all the components like data ingestion data transformation  and model trainer in pipline file in training pipeline

# Data Ingestion:- I faced errors and many issues in data ingestion while creating artifacts with all raw, test and train file all togther because of line no 29,38,29

# Remember while working on utils file we have to create utils.py inside utils folder while creating keep your eye on it's spelling and ignore the waring for  utils.utils import evaluate and save_object

# very tough but resolved the error it took a week now resolved be carefull from line no. 73 to 116 in data transformation in class initialize_data_transformation

# Finally issue resolved 

# Pipeline:- prediction pipline

# UI Part done :- Template folder created index.html, form.html and result.html files created for user interface, Some chages done in UI part in this process app.py file also plays a important role.

# I was trying to deploy this on render as it is a free deployer.