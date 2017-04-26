Otcclient
==========

[![PyPI version](https://badge.fury.io/py/python-otcclient.png)](https://badge.fury.io/py/python-otcclient)

Open Telecom Cloud API tool 
-----------------------------------------------

**#OTC #cloud #devops #IAAS #PAAS #DBAAS #BDAAS #container-services**

Purposes of the OTC Tool to manage OTC cloud environment via command line similar way like AWS cli. OTC Cli provides common interface to operation and DEVOPS teams to manage their cloud services. 
On top of that, the language implementations (Python at the moment) are secure and relatively fast.

More at [OTC site](https://console.otc.t-systems.com/console/#/home)

OTC makes it easy to use the cloud environment. It borrows the best parts from Huawei Service and Native Oenstack API.


Documentation
-------------

[Otcclient Reference](https://docs.otc.t-systems.com/?locale=en-us)

Command line usage
-----

`````sh
$ sudo pip install python-otcclient
`````
or
`````sh
$ git clone https://github.com/OpenTelekomCloud/python-otcclient.git
`````

Usage
----------------

`````sh
OTC Tool Configuration Commands:
otc configure                                                        Configuring OTC client tool (mandatory in first use)
otc configure-proxy                                                  Configureing proxy settings ( ONLY https )
otc version                                                          Print OTC Client tool version
S3 Commands:
otc s3 ls                                                            List Buckets
otc s3 ls mybucket                                                   List Bucket files
otc s3 mb mybucket                                                   Create New Bucket
otc s3 cp s3://bucketname/filename.txt /localdir/filename.txt        Download from bucket to local
otc s3 cp /localdir/filename.txt s3://bucketname/filename.txt        Upload file / directory to bucket
ECS Flavor & Image Commands:
otc ecs describe-flavors                                             List avaliable flavors (VM templates)
otc ecs describe-images                                              List image templates
VPC Commands:
otc ecs create-vpc --vpc-name myvpc --cidr 10.0.0.0/8                Crete new VPC
otc ecs describe-vpcs                                                List VPCs
Subnet Commands:
otc ecs create-subnet --subnet-name subnettest --cidr 192.168.1.0/16 --gateway-ip 192.168.1.2 --primary-dns 8.8.8.8 --secondary-dns 8.8.4.4 --availability-zone eu-de-01 --vpc-name default-vpc    Create new subnet for VPC
otc ecs describe-subnets --output Json
Security Group Commands:
otc ecs create-security-group --group-name test2 --vpc-name default-vpc  Create new security group
otc ecs describe-security-groups                                     List existing security-groups
otc ecs authorize-security-group-ingress --group-name test2 --vpc-name default-vpc --protocol tcp --ethertype IPv4 --portmin 22 --portmax 25      Add new incomming rule to security-group
otc ecs authorize-security-group-egress --group-name test2 --vpc-name default-vpc --protocol tcp --ethertype IPv4 --portmin 7000 --portmax 7001   Add new outcomming rule to security-group
Keypair Commands:
otc ecs describe-key-pairs                                           List key pairs
otc ecs create-key-pair --key-name mykeypair "ssh-rsa AA..."       Create key pair
Instance Commands:
otc ecs describe-instances                                           List VM instances
otc ecs describe-instances  --instance-ids 097da903-ab95-44f3-bb5d-5fc08dfb6cc3 --output Json     Detailed information of specific VM instance (JSON)
otc ecs run-instances --count 1  --admin-pass yourpass123! --instance-type c1.medium --instance-name instancename --image-name Standard_CentOS_6.7_latest --subnet-name testsubnet --vpc-name testvpc --group-name testsecgroup     Create new VM instance and START
otc ecs run-instances --count 1  --admin-pass yourpass123! --instance-type c1.medium --instance-name instancename --image-name Standard_CentOS_6.7_latest --subnet-name testsubnet --vpc-name testvpc --group-name testsecgroup  --key-name testsshkeypair --file1 /otc/a=/otc/a
--associate-public-ip-address  --wait-instance-running    Create new VM instance with injected SSH keypair, with public ip, additional file injection, wait instance created and running
otc ecs describe-instances                                           List VM instances
otc ecs stop-instances   --instance-ids b6c602b1-06d0-4bdb-b764-5d43b47abc14        Stop VM instance
otc ecs start-instances  --instance-ids b6c602b1-06d0-4bdb-b764-5d43b47abc14        Start VM instance
otc ecs reboot-instances --instance-ids b6c602b1-06d0-4bdb-b764-5d43b47abc14        Reboot VM instance
otc ecs delete-instances --instance-ids b6c602b1-06d0-4bdb-b764-5d43b47abc14        Delete VM instance (public ip + EVS also)
Backup Commands:
otc ecs create-snapshot  --volume-id b197b8af-fe63-465f-97b6-5e5b89exxxx  Create snapshot of volume
otc ecs describe-snapshots                                           List backup volumes
otc ecs delete-snapshot  --snapshot-id 0c942ff7-454e-xxxx            Delete volume backup
Volume Commands:
otc ecs describe-volumes                                             List volumes
otc ecs create-volume   --volume-id b197b8af-fe63-465f-97b6-5e5b89exxx --snapshot-id 0c942ff7-454e-xxxx Create volume from snapshot
otc ecs create-volume   --count 1 --volume-name myvolume  --size 100 --volume-type SATA      Create new Volume [type: SSD,SAS,SATA]
otc ecs attach-volume   --instance-ids f344b625-6f73-44f8-ad56-9fcb05a523c4 --volume-id 8c0de9a7-9f61-4613-a68a-21f456cb7298             Attach volume to instance
otc ecs detach-volume   --instance-ids f344b625-6f73-44f8-ad56-9fcb05a523c4 --volume-id 8c0de9a7-9f61-4613-a68a-21f456cb7298             Detach volume from instance
otc ecs delete-volume   --volume-id 8c0de9a7-9f61-4613-a68a-21f456cb7298                                                                 Delete volume
Public Ip Commands:
otc otc ecs describe-addresses                                       List public ip adresses
otc ecs allocate-address                                             Allocate public ip address from public ip pool
otc ecs associate-address --public-ip 46.29.96.246 --network-interface-id b197b8af-fe63-465f-97b6-5e5b89exxx      Assodicate public ip with Network Interface Id
`````

Writing clients
---------------

### Example Client with JSON output
 
	#!/usr/bin/env python
	
	import sys
	import os
	
	from otcclient.core.userconfigaction import userconfigaction
	from otcclient.core.configloader import configloader
	from otcclient.core.OtcConfig import OtcConfig
	from otcclient.plugins.ecs import ecs
	
	if __name__ == '__main__':
	    configloader.readUserValues() 
	    configloader.readProxyValues()
	
	    OtcConfig.OUTPUT_FORMAT = "Json"
	
	    ecs.getIamToken()
	    ecs.describe_vpcs()

### Example Ansible Module

- Ansible modules should not print everything to STDOUT (_noout_ plugin)
- Returned results are strings and need to bo converted back into data (_json.loads()_)

```
	#!/usr/bin/python
	
	import os
	import sys
	import re
	import json
	
	from ansible.module_utils.basic import *
	
	from otcclient.core.userconfigaction import userconfigaction
	from otcclient.core.configloader import configloader
	from otcclient.core.OtcConfig import OtcConfig
	from otcclient.plugins.ecs import ecs
	
	# DOCUMENTATION = """
	# ---
	# module: otc_vpc
	# short_description: manage otc vpcs aka tenants
	# description:
	# - create or a delete an otc vpc
	# options:
	#   name:
	#   - description: Name of VPC
	#   cidr:
	#   - description: Net for VPC in CIDR format
	#   state:
	#   - description: absent or present
	# author: Matthias Witte <matthias.witte@telekom.de>
	# """
	
	def _otc_init():
	    configloader.readUserValues()
	    configloader.readProxyValues()
	
	    OtcConfig.OUTPUT_FORMAT = "noout"
	    if OtcConfig.TOKEN == "":
	        ecs.getIamToken()
	
	def _get_vpcs():
	    try:
	        vpcs = json.loads(ecs.describe_vpcs())['vpcs']
	    except:
	        module.fail_json(msg="Result has no key 'vpcs'")
	    return vpcs
	
	
	def _vpc_create(module):
	    OtcConfig.VPCNAME = module.params['name']
	    OtcConfig.VPC_CIDR = module.params['cidr']
	    ecs.create_vpc()
	
	def _vpc_delete(module):
	    OtcConfig.VPCNAME = module.params['name']
	    module.fail_json(msg="Not implemented in OTC API.")
	    ecs.delete_vpc()
	
	def main():
	    module = AnsibleModule(
	        argument_spec = dict(
	            name    = dict(required=True),
	            cidr    = dict(required=False),
	            state   = dict(default='present', choices=['absent', 'present']),
	         )
	    )
	
	    if module.params['state'] == 'present' and 'cidr' not in module.params:
	        module.fail_json(msg="Missing argument 'cidr'")
	
	    _otc_init()
	
	    vpc_changed = False
	    vpc = [vpc for vpc in _get_vpcs() if vpc['name'] == module.params['name']]
	    if len(vpc) == 0:
	        if module.params['state'] == 'present':
	            _vpc_create(module)
	            vpc_changed = True
	    elif len(vpc) == 1:
	        if module.params['state'] == 'absent':
	            _vpc_delete(module)
	            vpc_changed = True
	    else:
	        module.fail_json(msg="Tenant name not unique.")
	
	    module.exit_json(changed=vpc_changed)
	
	if __name__ == '__main__':
	    main()
```

License
-------

The MIT License (MIT)

Copyright (c) 2016 OpenTelekomCloud

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
