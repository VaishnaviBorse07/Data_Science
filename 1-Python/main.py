# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 08:26:24 2025

@author: vaish
"""

from salary import calculate_salary
from validation import validate_experience,validate_role
from display import display_salary

def main():
    try:
        name=input("Enter Employee name:")
        experience=input("Enter years of experience:")
        role=input("Enter job role(Intern,Junior,Mid-Level,Senior,manager):")
        
        #validate inputs
        experience=validate_experience(experience)
        role=validate_role(role)
        
        #calculate salary
        salary=calculate_salary(experience, role)
        
        #display salary
        display_salary(name, experience, role, salary)
        
    except ValueError as e:
        print(f"Error:{e}")
        