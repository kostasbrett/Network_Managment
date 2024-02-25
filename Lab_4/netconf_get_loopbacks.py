#! /usr/bin/env python

# Import libraries
from ncclient import manager
from xml.dom import minidom
import xmltodict
import sys
from time import sleep 


# Create config template for an interface
config_data = """<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>{int_name}</name>
    </interface>
  </interfaces>
</filter>""" 

# Open NETCONF connection to device
with manager.connect(host = '10.2.2.1',
                     port = 830,
                     username = 'cisco',
                     password = 'cisco-netman',
                     hostkey_verify = False,allow_agent=False) as m:
    # ADD YOUR CODE HERE FOR MULTIPLE LOOPBACKS
    # Create desired NETCONF config payload and <edit-config>
    for index in range(1, 11):
	    interface_name = "Loopback" + str(index)
    	config = config_data.format(int_name = interface_name)
    	r = m.get_config("running", config)
    	xml_doc = minidom.parseString(r.xml)
    	#print(xml_doc.toprettyxml(indent = "  "))
    	# Process the XML data into Python Dictionary and use
    	interface = xmltodict.parse(r.xml)
    	# Only if RPC returned data
    	if not interface["rpc-reply"]["data"] is None:
        	interface = interface["rpc-reply"]["data"]["interfaces"]["interface"]

        	print("The interface {name} has ip address {ip}/{mask}".format(
                name = interface["name"]["#text"],
                ip = interface["ipv4"]["address"]["ip"],
                mask = interface["ipv4"]["address"]["netmask"],
                )
            )
    	else:
        	print("No interface {} found".format("GigabitEthernet2"))
