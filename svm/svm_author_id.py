#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np

clf = SVC(kernel='rbf', C=10000.0)

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
clf.fit(features_train, labels_train)
print "training time fit:", round(time()-t0, 3), "s"



t0 = time()
pred = clf.predict(features_test)
print "training time predict:", round(time()-t0, 3), "s"

print "perdictions:"
print "perdictions for 10 - "
print pred[10]
print "perdictions for 26 - "
print pred[26]
print "perdictions for 50 - "
print pred[50]

print "perdictions in favour of 1:"
print np.count_nonzero(pred == 1)

print "Accuracy:"
print accuracy_score(pred, labels_test)
#########################################################


