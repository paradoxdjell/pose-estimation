import numpy as np
import math
import pickle


def rotate(angle):
    radian = angle * math.pi / 180
    rot_mat = np.identity(3)
    sine = math.sin(radian)
    cosine = math.cos(radian)
    rot_mat[0][0] = cosine
    rot_mat[0][1] = -sine
    rot_mat[1][0] = sine
    rot_mat[1][1] = cosine
    return rot_mat


def translate(distance):
    trn_mat = np.identity(3)
    trn_mat[0][2] = distance
    trn_mat[1][2] = distance
    return trn_mat


for i in range(0, 61, 3):
    for j in range(0, 11, 2):
        rotation_matrix = rotate(i)
        translation_matrix = translate(j)
        transformation_matrix = rotation_matrix.dot(translation_matrix)
        pickle_name = "tm_" + str(i) + "_" + str(j) + ".pkl"
        with open("./pickle_files/" + pickle_name, 'wb+') as f:
            pickle.dump(translation_matrix, f)