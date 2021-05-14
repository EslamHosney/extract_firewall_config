# extract_firewall_config
This project is created to automate the extraction of firewalls' configuration files to be used by another tools to work on the firewalls offline not to impact their performance in live environment and avoid any operational issues ISA. 

## How To Use

To clone and run the examples you'll need:
* [Python2](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installing/)
* [netmiko](https://pypi.org/project/netmiko/)

From your command line:

```bash

# Clone this repository
$ git clone https://github.com/EslamHosney/extract_firewall_config.git

# Go into the repository

# Install dependencies
$ pip install -r requirements.txt

# Edit FirewallsData.csv to your Fortigate/SRX/Netscreen details (IP and credentials)
$ vim FirewallsData.csv

# Run the .py file
$ python extract_firewalls_configuration.py
```


## Prerequisites

* Change IP and credentials on FirewallsData.csv file
* Install python dependencies


## Environment

Tested on:
* Windows X 10
* python 2.7
* FortiOS 6.0
* Netscreen
* SRX

It should work on different environments, just keep in mind the versions above.

