# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 15:21:28 2025

@author: ptlpr
"""

import time
import random

LOG_FILE ="D:/1-Python/server.log"
LOG_LEVELS =["INFO","WARNING", "ERROR", "CRITICAL"]
MESSAGES = [
    "User logged in: user123",
    "High memory usage detected",
    "Database connection failed: timeout",
    "File uploaded: report.pdf",
    "Server crash detected! Restarting.....",
    "User logged out: user456",
    ]

def generate_logs():
    """Continously writes logs to a file every 2 seconds"""
    with open(LOG_FILE,"a") as file:
        while True:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            log_level = random.choice(LOG_LEVELS)
            message = random.choice(MESSAGES)
            log_entry = f"{timestamp} {log_level} {message}\n"
            file.write(log_entry)
            file.flush()
            print(f"Generated log: {log_entry.strip()}")
            time.sleep(2) #Simulate real-
            
generate_logs()
