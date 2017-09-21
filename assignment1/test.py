import sys
import numpy as np

def L2_distance_2_loop(test_data, train_data):
    row_test = test_data.shape[0]
    row_train = train_data.shape[0]

    dists = np.zeros((row_test, row_train))
    for i in range(row_test):
        for j in range(row_train):
            dist = np.sqrt(np.sum(np.square(test_data[i] - train_data[j])))
            dists[i][j] = dist

    return dists

def L2_distance_1_loop(test_data, train_data):
    row_test = test_data.shape[0]
    row_train = train_data.shape[0]

    dists = np.zeros((row_test, row_train))
    for i in range(row_test):
        dists[i,:] = np.sqrt(np.sum(np.square(test_data[i] - train_data), axis=1))
    return dists

def L2_distance_0_loop(test_data, train_data):
    row_test = test_data.shape[0]
    row_train = train_data.shape[0]

    dists = np.zeros((row_test, row_train))

    x2 = np.sum(test_data**2, axis=1).reshape((row_test, 1))
    y2 = np.sum(train_data**2, axis=1).reshape((1, row_train))
    xy = test_data.dot(train_data.T)
    dists = np.sqrt(x2 + y2 - 2*xy)

    return dists

test_data_raw = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [3, 2, 1]]) # (3, 4)
train_data_raw = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5],[6, 6, 6],[7, 7, 7],[8, 8, 8]])

print "L2_distance_2_loop".center(80, '=')
print L2_distance_2_loop(test_data_raw, train_data_raw)
print "L2_distance_1_loop".center(80, '=')
print L2_distance_1_loop(test_data_raw, train_data_raw)
print "L2_distance_0_loop".center(80, '=')
print L2_distance_0_loop(test_data_raw, train_data_raw)

dists = L2_distance_0_loop(test_data_raw, train_data_raw)
sorted_dist_arg = np.argsort(dists, axis=-1)
sorted_dist_arg = sorted_dist_arg[:,:2]
print sorted_dist_arg
