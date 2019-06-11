import numpy as np
import math
from Edge_Detector_1D import GaussianKernel1D
import csv

'''
% space = CreateGaussScaleSpace( data, deriv, scales )
% Computes the Gaussian scale space of a 1D data set.  (Scale parameters
% are in data-spacing units.)
% Input:
%   data        A 1D data set
%   deriv       The order of Gaussian scale space to compute (e.g. 0 is a
%               smoothing scale space; 1 is an edge detecting scale space)
%   scales      A list (vector) of scales to compute
% Output:
%   space       A scale space representation of the input data
'''

def CreateGaussScaleSpace(data = [], deriv = 1, scales = []):
    space = [[]] * 4
    k = 0
    for i in scales:
        scale = i
        # Find the gaussian kernel, convolve
        g = GaussianKernel1D.GaussianKernel1D(scale, deriv,3);
        # we have to pad the data to avoid the derivative blowing up at the boundaries, fill start and end data with g.__len__
        padData = data.copy()
        # padData = [data(1) * math.ones(g.__len__, 1), data, data(data.__len__()) * math.ones(g.__len__, 1)]
        for j in g:
            padData.insert(0,padData[0])

        for j in range(0,g.__len__()):
            padData.append(padData[padData.__len__()-1])

        padData = np.array(padData)
        padData = padData.astype(np.float)
        #print(padData)
        g = np.array(g)
        fData = np.convolve(padData, g, mode ='full')

        Flength = fData.__len__()
        Dlength =  data.__len__()
        offset = (Flength -Dlength)/2
        offset = offset.__int__()
        #print(offset)
        fData = fData[offset -1 : offset + Dlength-1] #data length same as before
        #print(fData)
        space[k] = fData
        k= k + 1
    #print(space)

    return  space


