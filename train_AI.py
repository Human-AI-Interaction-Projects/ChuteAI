"""
Created on Sun Dec  1 14:05:32 2019

@author: Loic
"""

import utility_functions
import sys
import os

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

def train_AI():
    
    processing_output = []
    all_input_features = []
    ML_output_falling = []
    ML_output_landing = []

    #Store all values for normalization
    all_mingz = []
    all_maxgz = []
    all_diff_minmaxay = []
    all_mingx = []

    #Extract features/outputs from all training sets
    for file in os.listdir("Training_Sets"):
        processing_output.append(utility_functions.process_file("Training_Sets\\" + file))


    #Split up processing output into ML input, and output labels for both metrics
    all_input_features = [data[0:4] for data in processing_output]
    ML_output_falling = [data[4] for data in processing_output]
    ML_output_landing = [data[5] for data in processing_output]

    #Normalize all features for ML algorithm (between 0 and 1)
    all_mingz = [data[0] for data in all_input_features]
    max_all_mingz = max(all_mingz)
    min_all_mingz = min(all_mingz)

    all_maxgz = [data[1] for data in all_input_features]
    max_all_maxgz = max(all_maxgz)
    min_all_maxgz = min(all_maxgz)

    all_diff_minmaxay = [data[2] for data in all_input_features]
    max_diff_minmaxay = max(all_diff_minmaxay)
    min_diff_minmaxay = min(all_diff_minmaxay)

    all_mingx = [data[3] for data in all_input_features]
    max_all_mingx = max(all_mingx)
    min_all_mingx = min(all_mingx)
    
    #Save normalization values for later use.
    with open('normalization_values.txt', 'w') as f:
        f.write(str(max_all_mingz) + '\n')
        f.write(str(min_all_mingz) + '\n')
        f.write(str(max_all_maxgz) + '\n')
        f.write(str(min_all_maxgz) + '\n')
        f.write(str(max_diff_minmaxay) + '\n')
        f.write(str(min_diff_minmaxay) + '\n')
        f.write(str(max_all_mingx) + '\n')
        f.write(str(min_all_mingx) + '\n')
        f.close()
        
    for data in all_input_features:
        data[0] = utility_functions.normalize(data[0], max_all_mingz, min_all_mingz)
        data[1] = utility_functions.normalize(data[1], max_all_maxgz, min_all_maxgz)
        data[2] = utility_functions.normalize(data[2], max_diff_minmaxay, min_diff_minmaxay)
        data[3] = utility_functions.normalize(data[3], max_all_mingx, min_all_mingx)

    #Now that all data is normalized,
    ML_input_falling = [data[0:2] for data in all_input_features]
    ML_input_landing = [data[2:4] for data in all_input_features]

    #For testing purposes
    """x_train_fall, x_test_fall, y_train_fall, y_test_fall = train_test_split(ML_input_falling, ML_output_falling, random_state=0)
    
    clf = DecisionTreeClassifier().fit(x_train_fall, y_train_fall)
    print('Accuracy of Decision Tree classifier on training set: {:.2f}'
          .format(clf.score(x_train_fall, y_train_fall)))
    print('Accuracy of Decision Tree classifier on test set: {:.2f}'
          .format(clf.score(x_test_fall, y_test_fall)))
    """
    
    clf_fall = DecisionTreeClassifier().fit(ML_input_falling, ML_output_falling)
    print('Accuracy of Falling classifier on training set: {:.2f}'
          .format(clf_fall.score(ML_input_falling, ML_output_falling)))
    
    #Remove Datasets where falling was bad. If falling is bad, landing is bad
    #Go backwards, to avoid messing up index
    reverse_iter = len(ML_output_falling) - 1
    while(reverse_iter >= 0):
        if (ML_output_falling[reverse_iter] != 'center'):
            ML_input_landing.pop(reverse_iter)
            ML_output_landing.pop(reverse_iter)
        reverse_iter -= 1
    
    clf_land = DecisionTreeClassifier().fit(ML_input_landing, ML_output_landing)
    print('Accuracy of Landing classifier on training set: {:.2f}'
          .format(clf_land.score(ML_input_landing, ML_output_landing)))
    
    #Save classifiers to be used later
    joblib.dump(clf_fall, 'falling_classifier.dt')
    joblib.dump(clf_land, 'landing_classifier.dt')
    
def main(args):
    train_AI()

if __name__ == '__main__':
    main(sys.argv[1:])