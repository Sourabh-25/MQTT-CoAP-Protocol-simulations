# MQTT Simulation for QOS1

This repository contains Python scripts for simulating MQTT QOS1 for a Publisher Subscriber Model and also contains Test scripts for collecting data so that analysis can be done 
## Contents:

1. **Client.py**
   - Provides Scripts for a basic Publisher of QOS1

2. **Subscriber.py**
   - Provides Scripts for a basic Subscriber of QOS1

3. **Test Scripts:**
   - **Response_Time_test.py:** For getting Response time of QOS1 and HTTP for different data size.
   - **TotalMessagesComparison.py:** For getting number of messages required to send so that a given number of messages can be successfully delivered .
     
4. **http_server.py**
   - Provides Scripts for a basic Http Server
  

## How to Run:

1. Run mosquitto(broker)
2. Run http_server.py
3. Run Subscriber.py
4. Run Response_Time_test.py
5. Run Total MessagesComparison.py
6. Run respective Graphs Scripts to get the graphs from the results produced

## Dependencies:

-  Install mosquitto
-  Install paho.mqtt.client
-  other necessary dependencies

## Results:

  1. **For Response time we have**
     - http_respoinse_times.csv
     - mqtt_response_times.csv
     - response_times_plot.png
     - Response_times_messages_number.png
  2. **For Toal Messages Required**
     - results_10.txt
     - results_20.txt
     - message_count.png
![response_times_plot](https://github.com/jay-3101/CSN-341-Project_Group10/assets/114606348/7dd2c6dd-d566-4039-8c9c-473b05f1c238)

