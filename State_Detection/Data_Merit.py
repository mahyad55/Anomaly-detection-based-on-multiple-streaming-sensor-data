import numpy as np
import math

def Data2_Merit(data = [], regionIdx = []):
# [ stats ] = RegionStats( data, regionIdx )
# Finds statistics for data broken up into distinct regions.
# Input:
#   data        The data to analyze
#   regionIdx   The indices that demarcate distinct data regions
    stats = [[[[[[]]]]]]
    if (regionIdx.__len__ () > 0):
        stats = [[[[[[[]]]]]]] * (regionIdx.__len__()+1)
        #print(range(0,regionIdx[0] - radius  - index + phi))
        #print(data[0:regionIdx[0] - radius  - index + phi])
        #why regionIdx[0]-1-1, -1 is the diffenence between index and element in regionIdx
        # also -1 again, because the element in RegionIdx means the change point,
        #so for a state, only cound the range before the change point.
        stats[0] = [1,regionIdx[0],regionIdx[0]-1, data[regionIdx[0]-1-1-1]-data[0],
                    np.max(data[0:regionIdx[0]-1-1])-np.min(data[0:regionIdx[0]-1-1]),
                    np.mean(data[0:regionIdx[0]-1-1]),np.std(data[0:regionIdx[0]-1-1])]
        #print(data[0])
        #print(data[0:regionIdx[0]-1-1])


        for i in range(1,regionIdx.__len__()):
            #if(i == 4):
                #print(data[regionIdx[i-1]-1:regionIdx[i]-1-1])
                #print(data[regionIdx[i]-1-1-1])

            #print(range(regionIdx[i-1]+radius-1-index+phi,regionIdx[i]-radius-index+phi))
            #print(data[regionIdx[i-1]+radius-1-index+phi:regionIdx[i]-radius-index+phi])
            stats[i] = [regionIdx[i-1],regionIdx[i],regionIdx[i]-regionIdx[i-1], data[regionIdx[i]-1-1-1]-data[regionIdx[i-1]-1],
                        np.max(data[regionIdx[i-1]-1:regionIdx[i]-1-1])-np.min(data[regionIdx[i-1]-1:regionIdx[i]-1-1]),
                        np.mean(data[regionIdx[i-1]-1:regionIdx[i]-1-1]),np.std(data[regionIdx[i-1]-1:regionIdx[i]-1-1])]

            #print(data[regionIdx[i-1]-1])
            #print(data[regionIdx[i]-1-1])
        #print(range(regionIdx[regionIdx.__len__()-1]+radius-1-index-phi, data.__len__()))
        #print(data[regionIdx[regionIdx.__len__()-1]+radius-1-index-phi:data.__len__()])
        #stats[regionIdx.__len__()] = [regionIdx[regionIdx.__len__()-1],data.__len__(),data.__len__()-regionIdx[regionIdx.__len__()-1]+1,
        #                             data[data.__len__()-1]- data[regionIdx[regionIdx.__len__()-1]-1],
        #                            np.max(data[regionIdx[regionIdx.__len__()-1]-1:data.__len__()])-
        #                              np.min(data[regionIdx[regionIdx.__len__()-1] - 1:data.__len__()]),
        #                              np.mean(data[regionIdx[regionIdx.__len__()-1] - 1:data.__len__()]),
        #                              np.std(data[regionIdx[regionIdx.__len__()-1] - 1:data.__len__()])]
        #print(data[regionIdx[regionIdx.__len__()-1]-1])
        #print(data.__len__()-1)
    return stats


def Data4_Merit(data = [], regionIdx = []):
# [ stats ] = RegionStats( data, regionIdx )
# Finds statistics for data broken up into distinct regions.
# Input:
#   data        The data to analyze
#   regionIdx   The indices that demarcate distinct data regions
    stats = [[[[[[]]]]]]
    if (regionIdx.__len__ () > 0):
        stats = [[]] * (regionIdx.__len__()+1)
        #print(range(0,regionIdx[0] - radius  - index + phi))
        #print(data[0:regionIdx[0] - radius  - index + phi])
        #why regionIdx[0]-1-1, -1 is the diffenence between index and element in regionIdx
        # also -1 again, because the element in RegionIdx means the change point,
        #so for a state, only cound the range before the change point.
        local_min = np.min(data[0:regionIdx[0]-1])
        stats[0] = [1,regionIdx[0],regionIdx[0]-1, local_min-data[0],
                    np.max(data[0:regionIdx[0]-1])-np.min(data[0:regionIdx[0]-1]),np.mean(data[0:regionIdx[0]-1])]
        #print(data[0])
        #print(data[regionIdx[0]-1-1])


        for i in range(1,regionIdx.__len__()):

            #print(range(regionIdx[i-1]+radius-1-index+phi,regionIdx[i]-radius-index+phi))
            #print(data[regionIdx[i-1]+radius-1-index+phi:regionIdx[i]-radius-index+phi])
            local_min = np.min(data[regionIdx[i-1]-1:regionIdx[i]-1])
            stats[i] = [regionIdx[i-1],regionIdx[i],regionIdx[i]-regionIdx[i-1], local_min-data[regionIdx[i-1]-1],
                        np.max(data[regionIdx[i-1]-1:regionIdx[i]-1])-np.min(data[regionIdx[i-1]-1:regionIdx[i]-1]),
                        np.mean(data[regionIdx[i-1]-1:regionIdx[i]-1])]

            #print(data[regionIdx[i-1]-1])
            #print(data[regionIdx[i]-1-1])
        #print(range(regionIdx[regionIdx.__len__()-1]+radius-1-index-phi, data.__len__()))
        #print(data[regionIdx[regionIdx.__len__()-1]+radius-1-index-phi:data.__len__()])
        local_min = np.min(data[regionIdx[regionIdx.__len__()-1] - 1:data.__len__()])
        stats[regionIdx.__len__()] = [regionIdx[regionIdx.__len__()-1],data.__len__(),data.__len__()-regionIdx[regionIdx.__len__()-1]+1,
                                      local_min- data[regionIdx[regionIdx.__len__()-1]-1],
                                      np.max(data[regionIdx[regionIdx.__len__()-1]-1:data.__len__()])-
                                      np.min(data[regionIdx[regionIdx.__len__()-1] - 1:data.__len__()]),
                                      np.mean(data[regionIdx[regionIdx.__len__()-1] - 1:data.__len__()])]
        #print(data[regionIdx[regionIdx.__len__()-1]-1])
        #print(data.__len__()-1)
    return stats


def Data10_Merit(data = [], regionIdx = []):
# [ stats ] = RegionStats( data, regionIdx )
# Finds statistics for data broken up into distinct regions.
# Input:
#   data        The data to analyze
#   regionIdx   The indices that demarcate distinct data regions
    stats = [[[[[[]]]]]]
    if (regionIdx.__len__ () > 0):
        #flag = 1
        stats = [[[[[[[]]]]]]] * (regionIdx.__len__()+1)
        #print(range(0,regionIdx[0] - radius  - index + phi))
        #print(data[0:regionIdx[0] - radius  - index + phi])
        #why regionIdx[0]-1-1, -1 is the diffenence between index and element in regionIdx
        # also -1 again, because the element in RegionIdx means the change point,
        #so for a state, only cound the range before the change point.
        local_min = np.min(data[0:regionIdx[0]-1-1])
        stats[0] = [1,regionIdx[0],regionIdx[0]-1, data[regionIdx[0]-1-1-1]-local_min,
                    np.max(data[0:regionIdx[0]-1-1])-np.min(data[0:regionIdx[0]-1-1]),
                    np.mean(data[0:regionIdx[0]-1-1]),np.std(data[0:regionIdx[0]-1-1])]
        #print(data[0])
        #print(data[0:regionIdx[0]-1-1])


        for i in range(1,regionIdx.__len__()):
            #if(i == 4):
                #print(data[regionIdx[i-1]-1:regionIdx[i]-1-1])
                #print(data[regionIdx[i]-1-1-1])

            #print(range(regionIdx[i-1]+radius-1-index+phi,regionIdx[i]-radius-index+phi))
            #print(data[regionIdx[i-1]+radius-1-index+phi:regionIdx[i]-radius-index+phi])
            local_min = np.min(data[regionIdx[i - 1] - 1:regionIdx[i] - 1-1])
            stats[i] = [regionIdx[i-1],regionIdx[i],regionIdx[i]-regionIdx[i-1], data[regionIdx[i]-1-1-1]-local_min,
                        np.max(data[regionIdx[i-1]-1:regionIdx[i]-1-1])-np.min(data[regionIdx[i-1]-1:regionIdx[i]-1-1]),
                        np.mean(data[regionIdx[i-1]-1:regionIdx[i]-1-1]),np.std(data[regionIdx[i-1]-1:regionIdx[i]-1-1])]

            #print(data[regionIdx[i-1]-1])
            #print(data[regionIdx[i]-1-1])
        #print(range(regionIdx[regionIdx.__len__()-1]+radius-1-index-phi, data.__len__()))
        #print(data[regionIdx[regionIdx.__len__()-1]+radius-1-index-phi:data.__len__()])
        local_min = np.min(data[regionIdx[regionIdx.__len__() - 1] - 1:data.__len__()])
        stats[regionIdx.__len__()] = [regionIdx[regionIdx.__len__()-1],data.__len__(),data.__len__()-regionIdx[regionIdx.__len__()-1]+1,
                                      data[data.__len__()-1]- local_min,
                                      np.max(data[regionIdx[regionIdx.__len__()-1]-1:data.__len__()])-
                                      np.min(data[regionIdx[regionIdx.__len__()-1] - 1:data.__len__()]),
                                      np.mean(data[regionIdx[regionIdx.__len__()-1] - 1:data.__len__()]),
                                      np.std(data[regionIdx[regionIdx.__len__()-1] - 1:data.__len__()])]
        #print(data[regionIdx[regionIdx.__len__()-1]-1])
        #print(data.__len__()-1)
    return stats

