# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 09:38:27 2025

@author: vaish
"""
def validate_experience(exp):
    if not isinstance(exp, int) or exp<0:
        raise ValueError("Experience must be non-negative")
    return exp

def validate_role(role):
    valid_roles={"Intern","Junior","Mid-level","Senior","manager"}
    if role not in valid_roles:
        raise ValueError(f"Inavalid role:Choose from {valid_roles}")
    return role