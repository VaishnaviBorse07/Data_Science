# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 16:08:43 2025

@author: ptlpr
"""

import time
file_path = 'D:/1-Python/server.log'
def tail_log_file(file_path):
    """Generator that continuosly reads new line from a log"""
    with open(file_path ,"r") as file:
        file.seek(0,2)
        while True:
            line = file.readline()
            if not line:
                time.sleep(1)#wait for new log to be addressed
                continue
            yield line.strip()#yield new log title

#example usage: Process logs as they come in
for log in tail_log_file(file_path):
    if "ERROR"in log:
        print(f"Alert :{log}")#trigger alert for an error
        
