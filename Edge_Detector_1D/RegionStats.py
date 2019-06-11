import numpy as np
import math


def RegionStats( data, regionIdx, radius, index = 0, phi = 0 ):
# [ stats ] = RegionStats( data, regionIdx )
# Finds statistics for data broken up into distinct regions.
# Input:
#   data        The data to analyze
#   regionIdx   The indices that demarcate distinct data regions
#   radius      The radius of transition regions (data within transition
#               regions is excluded from statistics)
    stats = [[]]
    if (regionIdx.__len__ () > 0):
        #flag = 1
        stats = [[]] * (regionIdx.__len__()+1)
        #print(range(0,regionIdx[0] - radius  - index + phi))
        #print(data[0:regionIdx[0] - radius  - index + phi])
        stats[0] = [np.mean(data[0:regionIdx[0]-radius-index+phi]), np.std(data[0:regionIdx[0]-radius-index+phi])]

        for i in range(1,regionIdx.__len__()):

            #print(range(regionIdx[i-1]+radius-1-index+phi,regionIdx[i]-radius-index+phi))
            #print(data[regionIdx[i-1]+radius-1-index+phi:regionIdx[i]-radius-index+phi])
            stats[i] = [np.mean(data[regionIdx[i-1]+radius-1-index+phi:regionIdx[i]-radius-index+phi]), np.std(data[regionIdx[i-1]+radius-1-index+phi:regionIdx[i]-radius-index+phi])]

        #print(range(regionIdx[regionIdx.__len__()-1]+radius-1-index-phi, data.__len__()))
        #print(data[regionIdx[regionIdx.__len__()-1]+radius-1-index-phi:data.__len__()])
        stats[regionIdx.__len__()] = [np.mean(data[regionIdx[regionIdx.__len__()-1]+radius-1-index-phi:data.__len__()]), np.std(data[regionIdx[regionIdx.__len__()-1]+radius-1-index-phi:data.__len__()])]

        #print(stats)
    return stats
