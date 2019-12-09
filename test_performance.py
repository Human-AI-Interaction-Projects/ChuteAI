# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 11:28:35 2019

@author: Loic
"""
import utility_functions
import sys

from sklearn.externals import joblib

def test_data(file_location):

    #file_location = 'Training_Sets\\goodland2.csv'


    processed_output = utility_functions.process_file(file_location, 1, 0)
    normalization_values = []
    
    with open('normalization_values.txt', 'r') as f:
        for line in f:
            normalization_values.append(int(line))
        f.close()

    ML_input_falling = []
    ML_input_landing = []

    #To ensure it is list of lists(for classifier input), append output list to list
    ML_input_falling.append([utility_functions.normalize(processed_output[0], normalization_values[0], normalization_values[1]),
                        utility_functions.normalize(processed_output[1], normalization_values[2], normalization_values[3])])
    ML_input_landing.append([utility_functions.normalize(processed_output[2], normalization_values[4], normalization_values[5]),
                        utility_functions.normalize(processed_output[3], normalization_values[6], normalization_values[7])])
    ML_output_falling = processed_output[4]
    ML_output_landing = processed_output[5]

    assert(ML_output_falling == 'no_label' and ML_output_landing == 'no_label')

    falling_model = joblib.load('falling_classifier.dt')
    landing_model = joblib.load('landing_classifier.dt')
    falling_prediction = falling_model.predict(ML_input_falling)
    landing_prediction = landing_model.predict(ML_input_landing)
    
    print(landing_prediction)
    print(falling_prediction)

    #Only return landing prediction if falling is good
    if (falling_prediction[0] != 'center'):
        return falling_prediction[0], 'N/A'
    else:
        return falling_prediction[0], landing_prediction[0]

def main(args):
    if (len(args) != 1):
        exit(-1)
    return test_data(args[0])
if __name__ == '__main__':
    main(sys.argv[1:])