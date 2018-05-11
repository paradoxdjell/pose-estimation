import numpy as np
import math
import pickle
import os, sys


def rotate(angle):
    radian = angle * math.pi / 180.0
    rot_mat = np.identity(3)
    sine = math.sin(radian)
    cosine = math.cos(radian)
    rot_mat[0][0] = cosine
    rot_mat[0][1] = -sine
    rot_mat[1][0] = sine
    rot_mat[1][1] = cosine
    return rot_mat


def translate(distance_x, distance_y):
    trn_mat = np.identity(3)
    trn_mat[0][2] = distance_x
    trn_mat[1][2] = distance_y
    return trn_mat

for i in range(0, 11, 1):
    for j in range(0, 5, 1):
        for k in range(0, 5, 1):
            rotation_matrix = rotate(i)
            translation_matrix = translate(j, k)
            transformation_matrix = rotation_matrix
            pickle_name = "tm_" + str(i) + ".pkl"
            with open(os.path.dirname(sys.modules['__main__'].__file__) + "/pickle_files_both_sides/" + pickle_name, 'wb+') as f:
                pickle.dump(transformation_matrix, f)
            if i != 0:
                rotation_matrix = rotate(-i)
                transformation_matrix = rotation_matrix
                pickle_name = "tm_" + str(-i) + ".pkl"
                with open(os.path.dirname(sys.modules['__main__'].__file__) + "/pickle_files_both_sides/" + pickle_name, 'wb+') as f:
                    pickle.dump(transformation_matrix, f)
