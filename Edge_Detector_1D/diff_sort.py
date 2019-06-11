from Edge_Detector_1D import define
from collections import deque


def diff_sort(diff = []):

    for i,element_i in enumerate(diff):
        for j,element_j in enumerate(diff):
            if (element_i.diff_Mean > element_j.diff_Mean):
                temp = element_i
                diff[i] = diff[j]
                diff[j] = temp

            if(element_i.diff_Leng > element_j.diff_Leng):
                temp = element_i
                diff[i] = diff[j]
                diff[j] = temp

            if (element_i.diff_Stdv > element_j.diff_Stdv):
                temp = element_i
                diff[i] = diff[j]
                diff[j] = temp


    return diff