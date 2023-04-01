#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 17:33:52 2023

@author: giannidiarbi

 Gianni Diarbi
 DS2000
 Spring 2023
 HW 4 Problem 1
 suffrage.py
 
"""

VOTER_FILE = "1920_women_voters.csv"

AGE_POSITION = 10

TWENTIES_MIN = 20
THIRTIES_MIN = 30
FORTIES_MIN = 40
FIFTIES_MIN = 50
OVER_FIFTY_MIN = 60


import matplotlib.pyplot as plt

def main():
    
    # Collect Data - Open file and read in the header
    with open(VOTER_FILE, "r") as infile:
        header = infile.readline()
 
    # Create an empty list to append age data to
        ages = []
        
        # Use a for loop to read in voter info
        for line in infile:
            
           # Turn the string line into a list of strings
           age_lst = line.split(",")
           
           # Define the age data
           age_data = age_lst[AGE_POSITION]
            
          # Check if an age exists in each line, and append the age data to
          # the ages list
           if age_data != "":
               ages.append(int(age_data))
           
        # Create separate lists for each age range
        twenties = []
        thirties = []
        forties = []
        fifties = []
        over_fifty = []
           
        # Append the age data to the appropriate age range list
        for i in ages:
            if i >= TWENTIES_MIN and i < THIRTIES_MIN:
                twenties.append(i)
            elif i >= THIRTIES_MIN and i < FORTIES_MIN:
                thirties.append(i)
            elif i >= FORTIES_MIN and i < FIFTIES_MIN:
                forties.append(i)
            elif i >= FIFTIES_MIN and i < OVER_FIFTY_MIN:
                fifties.append(i)
            else:
                over_fifty.append(age_data)
       
        # Communication - create a bar chart representing the number of 
        # women in each age category
        plt.bar("twenties", len(twenties), color = "palevioletred")
        plt.bar("thirties", len(thirties), color = "teal")
        plt.bar("forties", len(forties), color = "darkslateblue")
        plt.bar("fifties", len(fifties), color = "darkgoldenrod")
        plt.bar("over fifty", len(over_fifty), color = "darkred")
        
        # Add titles and axes labels to the axes
        plt.xlabel("Age Group")
        plt.ylabel("Number of Women")
        plt.title("Number of Women Voters in 1920, by Age")
  
main()

