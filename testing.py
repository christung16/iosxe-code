#!/usr/bin/env python

from ncclient import manager
import xml.dom.minidom

host = 'localhost'
port = 8830
user = 'vagrant'
password = 'vagrant'

netconf_connection = manager.connect(host=host,
                                     port=port,
                                     username=user,
                                     password=password,
                                     hostkey_verify=False)

config = netconf_connection.get_config("running")

file = open("standard_config.xml","w")
file.write(xml.dom.minidom.parseString(config.xml).toprettyxml())
file.close()



print (xml.dom.minidom.parseString(config.xml).toprettyxml())

netconf_connection.close_session()
