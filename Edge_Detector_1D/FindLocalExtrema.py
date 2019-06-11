import math
import numpy as np

def FindLocalExtrema ( data , threshold , scale , regions = [0]):


# maxmin = FindLocalExtrema( data )
# Finds locally maximal or minimal values in the y direction of the given data.
# Input:
#   data        1D data array (image)
#   threshold   What fraction of total maximum or minimum a data point
#               needs to be for consideration (non-maximum supression)
#   scale       Specifies the number of data points in a local neighborhood
#               (neighborhood legth is 2 * scale + 1)
#   regions     Specifies a set of regions to look in--if not supplied,
#               the whole data region will be searched
# Output:
#   extrema     a vector the same size as the input data with value 1 at
#               input data maxima and minima, 0 elsewhere

# rescale data


    rdataMax = data / max(data)
    rdataMin = data / min(data)
    #print(rdataMax)
    winmax = np.zeros(data.__len__())
    winmin = np.zeros(data.__len__())
# Note: It would have been nice to do the follwing as a vector operation,
# even within the min/max detection below.  For reasons opaque to me, the
# max() function doesn't seem to work in a vector operation.  We wanted something like:
# winmax(ii) = max(rdataMax(ii-scale:ii+scale));
# But, this seems to generate a vector mostly of, almost like the maximum
# is being applied cummulatively. Oh, well...this isn't too slow if the
# data are not too big.
# create a sliding window min & max



    for i in range(scale, data.__len__() - scale) :

        winmax[i] = np.max(rdataMax[i - scale:i + scale+1])
        winmin[i] = np.max(rdataMin[i - scale:i + scale+1])

    maxima = np.zeros(data.__len__())
    minima = np.zeros(data.__len__())

# find the local minima and maxima
    if(regions[0] == 0):
        for ii in range(scale, data.__len__() - scale):
            maxima[ii] = rdataMax[ii] >= threshold and rdataMax[ii] >= winmax[ii]
            minima[ii] = rdataMin[ii] >= threshold and rdataMin[ii] >= winmin[ii]
    else:
        for k in range(0,regions.__len__()):
            for ii in range(max(scale, regions[k] - scale-1), min(data.__len__() - scale, regions[k] + scale)):
                maxima[ii] = rdataMax[ii] >= threshold and rdataMax[ii] >= winmax[ii]
                minima[ii] = rdataMin[ii] >= threshold and rdataMin[ii] >= winmin[ii]

# combine min and max
    extrema = maxima + minima
    return extrema

