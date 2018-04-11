# SmartAg
Web application for smartag monitoring system

<h3>The structure of this code is as follows:</h3>

<h4>Cognito-JS-SDK</h4>
--This folder holds the SDK for AWS Cognito. It is used for all calls to the Cognito service.

<h4>PiSensorScripts</h4>
-- This folder contains all scripts tasked with reading in data from sensors and sending them to AWS.

- DHT11.py is the script for reading in data from the DHT11 temperature and humidity sensor

- TSL2561.py is the script for reading in data from the TSL2561 light sensor

- YL69_ADS1015.py is the script for reading in data from the YL69 moisture sensor

- IoTConnect.py is the python script tasked with formatting the sensor data from above and sending it to AWS IoT

<h4>PiSensorScripts</h4>
-- This folder houses the code for the front end/web site
- Included in this folder is code for the main index page, code for logging in to the site, and code for displaying the data

<h4>PiSensorScripts</h4>
-- This folder is for testing. It currently has a test call for dynamoDB.
