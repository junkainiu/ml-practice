from numpy import *
import operator

def create_data_set():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inx, data_set, labels, k):
    data_set_size = data_set.shape[0]
    diff_mat = tile(inx, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat ** 2
    sq_distance = sq_diff_mat.sum(axis=1)
    distance = sq_distance**0.5
    sorted_dist_indices = distance.argsort()
    class_count = {}
    for i in range(k):
        vote_ilabel = labels[sorted_dist_indices[i]]
        class_count[vote_ilabel] = class_count.get(vote_ilabel, 0) + 1
    sorted_class_count = sorted(class_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]





res = classify0([1,2], create_data_set()[0], create_data_set()[1], 1)
print res
