# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 14:05:32 2019

@author: Loic
"""

import sys
import utility_functions
import train_AI
import subprocess
import os

def retrain(file_location, desired_falling_score, desired_landing_score):


    for i in range(0, 1000):
        new_name = "added" + str(i) + ".csv"
        if (not os.path.exists("Training_Sets\\" + new_name)):
            break

    if (desired_falling_score != 'center' and desired_falling_score != 'bad_right' and desired_falling_score != 'bad_left'):
        return 'failure'
    if (desired_landing_score != 'good' and desired_landing_score != 'bad' and desired_landing_score !='N/A'):
        return 'failure'

    if (desired_falling_score != 'center'):
        desired_landing_score = 'bad'

    #Copy data file to Training_Sets Directory
    subprocess.run(["cp", file_location, "Training_Sets\\" + new_name])

    #Add desired output to beginning of data file
    utility_functions.prepend_file("Training_Sets\\" + new_name, desired_falling_score + ',' + desired_landing_score)
    
    train_AI.train_AI()
    return 'success'

def main(args):
    if (len(args) != 3):
        print("Usage: retrain_AI <file location> <desired falling score> <desired landing score>")
        exit()
    return retrain(args[0], args[1], args[2])

if __name__ == '__main__':
    main(sys.argv[1:])