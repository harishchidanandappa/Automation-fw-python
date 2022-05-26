# Automation-fw-python
Selenium automation framework.
Selenium Automation Framework:
Project is developed based on page object factory organised as per the pages classes.

Running project
Step 1: Clone repo
First you need to clone the repo to your local

Clone with SSH:
git@github.com:Harishchidanandappa/automation_fw_python.git

OR

Clone with HTTPS:
https://github.com/Harishchidanandappa/automation_fw_python.git

Step 2: Setting up envionment variables
Add API key to run the API test by adding below variable string under the file Data/config_data.py

APIKEY: str = ''
geckodriver_path = ''

Download gecko driver from the link below and set executable path for mac

https://github.com/mozilla/geckodriver/releases/tag/v0.29.1
Running code through python
The application can be run directly through python after fullfilling the above mentioned configuration:

Install python

python3 must be installed , the project is build on python3.9
Set the python path

export PYTHONPATH="${PYTHONPATH}:/users/username/projectmainpath/"
Create and activate a virtual environment

Run this command to create a virtual environment

python3 -m venv myproject
Switch to virtual environemt by activating following command

source myproject/bin/activate
Install project

Clone the repo as mentioned in step1

Install dependencies

Enter the project folder and run below command to install all dependencies

pip install -r requirements.txt
https://github.com/Harishchidanandappa/automation_fw_python/blob/master/tests/conftest.py

Run Project

To run test suite run the below command in the console:

py.test tests/test_suite.py --browser firefox
Run Individual scripts

To run all tests individually run the below command within the console:

py.test -s -v tests/home/test_manual_select.py --browser firefox
py.test -s -v tests/home/test_import_csv.py --browser firefox
py.test -s -v tests/home/test_geo_cordinates_api.py
