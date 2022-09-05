# !/user/bin/even python
# -*- coding:utf-8 -*-
import os, sys
import re
import time, datetime
import json
from seleniumRequests import creatChrome


bro=creatChrome().modifyEnviroment()
bro.get('https://www.modes.com/us/shopping/woman/clothing-coats')

time.sleep(1)
print(bro.page_source)


for i in range(600):
    print(i)
    time.sleep(1)

bro.close()