#! /bin/bash

while [ 1 ]
do
    python readLight.py
    python readMoisture.py
    python readTempHumid.py 11 23
    sleep 10
done
