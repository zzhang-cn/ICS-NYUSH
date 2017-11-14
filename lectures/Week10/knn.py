# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 18:17:10 2017

@author: zhengzhang
"""
import sample
import random
import util
import knn_helper
    
def knn(p, data, k):
    """ Compute the distance between p to every sample in data,
        set p's label to the label of the maximum of samples 
        within the k nearest neighbors
    """
    
    """ Steps:
        1. Iterate through samples in data and store the 
           distance from p in the dictionary "distance"; key is the 
           distance, value is the sample.
        2. Creat a sorted list of samples according to ascending
           order of the distances.
        3. In the dictioary "label_votes", stores number of votes
           in each label among the top-k nearest samples
        4. Assign p the most popular label
    """

    max_label = util.LABELS[0]
    p.setLabel(max_label)
    # above forces a fixed label: remove them
    # replace knn_helper.knn(p, data, k) with your own logic
    print(p)
    knn_helper.knn(p, data, k)
    print(p)
    
if __name__ == "__main__":
    
    random.seed(0)
    n = 100
    K = 3
    
    data = util.genDistribution(n=10)
    for d in data:
        d.setLabel(random.choice(util.LABELS))

    print("before....")
    util.plot_data(data)
    
    new_pt = sample.Sample('', [0.2, 0.3], '')
    knn(new_pt, data, K)
    
    data.append(new_pt)
    print("\nafter....")
    util.plot_data(data)   
