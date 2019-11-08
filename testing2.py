#!/usr/bin/env python

from ncclient import manager

host='localhost'
port='8830'
username='vagrant'
password='vagrant'

m = manager.connect(host=host,
                    port=port,
                    username=username,
                    password=password,
                    hostkey_verify=False)

acl2 = '''
       <config>
       </config>
       '''
acl = '''
            <config>
                <access-list>
					<standard xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-acl">
						<name>CUHKnet-xmlimport</name>
						<access-list-seq-rule>
							<sequence>10</sequence>
							<permit>
								<std-ace>
									<ipv4-prefix>103.49.160.0</ipv4-prefix>
									<mask>0.0.3.255</mask>
								</std-ace>
							</permit>
						</access-list-seq-rule>
						<access-list-seq-rule>
							<sequence>20</sequence>
							<permit>
								<std-ace>
									<ipv4-prefix>123.255.64.0</ipv4-prefix>
									<mask>0.0.63.255</mask>
								</std-ace>
							</permit>
						</access-list-seq-rule>
					</standard>
			    </access-list>	   
			</config>
   '''

push = m.edit_config(acl2, target="running")

print (xml.dom.minidom.parseString(push.xml).toprettyxml())

m.close_session()