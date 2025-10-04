# -*- coding: utf-8 -*-
"""
Module containing ridiculous maths stuff
"""
import matplotlib.pyplot as plt
import numpy as np

def add_numbers(x,y):
    return x+y

def sub_numbers(x,y):
    return x-y

def return_biggest(x,y):
    return max(x,y)

magic_number = 27

def plot_family(n,m):
    """
    plot_family plots the family of curves x^n+i for i between -m and m
    """
    x = np.linspace(-2,2,100)
    for i in range(-m,m+1):
        plt.plot(x,x**n+i)

    plt.show()