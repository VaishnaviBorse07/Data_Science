# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 09:27:29 2025

@author: vaish
"""

def calculate_salary(experience,role):
    base_salary={"Intern":30000,"Junior":50000,"Mid-level":80000,"Senior":100000,"manager":150000}
    if role not in base_salary:
        raise ValueError("Invalid job role")
    return base_salary[role]+(experience*2000)