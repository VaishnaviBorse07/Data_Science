# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 15:18:35 2025

@author: ptlpr
"""
import csv

def process_transaction(transaction):
    ''' dummy  fucntion to stimulate processing a transaction'''
    if "ERROR" in transaction[2]:
        #stimulate an error for some transactions
        raise ValueError("transaction failed!")
    return f"Processed transaction :{transaction}"

#Open and read the CSV file
with open ("D:/1-Python/transaction.csv","r") as file:
    reader = csv.reader(file)
    next(reader) #skip the header
    
    for index, transaction in enumerate(reader, start=1):
        try: 
            result = process_transaction(transaction)
            print(f"Row {index}:{result}")
        except ValueError as e:
            print(f"Error at Row {index}:{e}")
            
    