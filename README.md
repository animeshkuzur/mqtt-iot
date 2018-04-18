# MQTT-IoT Client and Publisher
Minimalistic MQTT client and publisher to send and record smoke, temperature and light intensity data from a node MCU module.

### Prerequisite Modules
* Paho MQTT Client (`pip install -r /path/to/requirements.txt`)
* Nginx (`apt-get install nginx`)
* MQTT Broker (`apt-get install mosquitto`)

### JSON Syntax
This JSON syntax is for Node MCU to send the MQTT Broker on the network.
* For Smoke Data: `{'smoke':'23.23','temp':'','light':''}`
* For Temperature Data: `{'smoke':'','temp':'27.54','light':''}`
* For Light Intensity: `{'smoke':'23.23','temp':'','light':'6.7'}`

Note: The broker isn't designed to accept more than 1 key-value pair at a time, if there are more than 1 value then data loss might occur.

### Deployment and Configuration
* First: Install all the prerequisite modules and clone the repository `git clone https://github.com/animeshkuzur/mqtt-iot.git` at your home directory
* Second: Open up `config.py` and edit the `DATA_PATH` variable to your public directory. eg: `/var/www/data` and run the following command `sudo mkdir /var/www/data`
* Third: Run `sudo chmod -R 777 /var/www/data` and `sudo cp ~/mqtt-iot/html/index.html /var/www/`
* Fourth: Check the IP address of your MQTT Broker (`ifconfig`) and copy the IP address into your Node MCU script
* Fifth: Run `mosquitto` at the terminal
* Sixth: Run `python3 ~/mqtt-iot/client.py`
* Seventh: To check the graph, either open `127.0.0.1` on your local browser or type in the IP address of the broker into a different machine (which is on the same wifi network)
