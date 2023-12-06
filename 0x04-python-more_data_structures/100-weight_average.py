#!/usr/bin/python3
def weight_average(my_list=[]):
    score = 0
    denominator = 0
    if my_list:
        for element in my_list:
            score += element[0] * element[1]
            denominator += element[1]
        score = score/denominator
    return score
