#! /usr/bin/env python

# Import libraries
from ncclient import manager
from xml.dom import minidom
import xmltodict
import sys
from time import sleep 


loopback = {"int_name": "Loopback1",
            "description": "Test Building",
            "ip": "1.1.1.1",
            "netmask": "255.255.0.0"}

# Create config template for an interface
config_data = """
<config>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
        <name>{int_name}</name>
        <description>{description}</description>
        <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
	  ianaift:softwareLoopback
        </type>
        <enabled>true</enabled>
        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
          <address>
            <ip>{ip}</ip>
            <netmask>{netmask}</netmask>
          </address>
        </ipv4>
      </interface>
  </interfaces>
</config>
"""

# Open NETCONF connection to device
with manager.connect(host = '10.2.2.1',
                     port = 830,
                     username = 'cisco',
                     password = 'cisco-netman',
                     hostkey_verify = False,allow_agent=False) as m:
    # ADD YOUR CODE HERE FOR MULTIPLE LOOPBACKS
    # Create desired NETCONF config payload and <edit-config>

    for index in range(1, 11):
	loopback = {}
	loopback["int_name"] = "Loopback" + str(index)
	loopback["description"] = "ECE-NTUA-Building-" + str(index)
	loopback["ip"] = "147.102." + str(index) + ".1"
	loopback["netmask"] = "255.255.255.0"
	print(loopback)
	config = config_data.format(**loopback)
	r = m.edit_config(target = "running", config = config)
	sleep(1)

    # Print OK status
    print("NETCONF RPC OK: {}".format(r.ok)+" Loopback1 created")
