#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 18:48:20 2019
@author: tushar
"""

import json
from docker import APIClient
import pandas as pd

#calling docker api to get data
client1=APIClient(base_url='unix://var/run/docker.sock')

# in below we will provide the username of container like(inspiring_bardeen)
stats_obj=client1.stats('inspiring_bardeen')

f=open("output.txt","a+") 
for stat in stats_obj:
    print(stat)
    print(type(stat))
    df=pd.read_json(stat,orient='columns') 
   # with open("output.txt","a+") as f:
   # print("hello")
    f.write(str( stat)+"\n\n") 
    # f.close()
            
"""   
#for conversion to json
my_json=new_bytes.decode('utf8').replace("'",'"')
data=json.loads(my_json)
s=json.dumps(data, intent=4, sort_keys=True)"""


client1.id()
