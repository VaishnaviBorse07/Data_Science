# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 08:20:49 2025

@author: vaish
"""

def display_salary(name,experience,role,salary):
    print("\n== Salary Details ==")
    print(f"Employee name: {name}")
    print(f"Role: {role}")
    print(f"Experience: {experience} years")
    print(f"Calculated Salary: ${salary:,.2f}")
    print("============")