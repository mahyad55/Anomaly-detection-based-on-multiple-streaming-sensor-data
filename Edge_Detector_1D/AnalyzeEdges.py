import numpy as np
from Edge_Detector_1D import CreateGaussScaleSpace
from Edge_Detector_1D  import  FindLocalExtrema
from Edge_Detector_1D import RegionStats
from Edge_Detector_1D import Divide_stats
import csv
import matplotlib.pyplot as plt


def AnalyzeEdges(data = [], index = 0, phi = 0):

    #defaults
    tranRad = 1

    # time scale
    thresholds = [.13, .26, 0.52, 1.04]
    scales = [1, 2, 4, 8]


    #Limit analysis to time region specified
    dData = CreateGaussScaleSpace.CreateGaussScaleSpace(data, 1, scales)
    minmax = FindLocalExtrema.FindLocalExtrema(dData[scales.__len__()-1], thresholds[scales.__len__()-1], scales[scales.__len__()-1]);
    minmaxIdx = []
    for i in range(0, minmax.__len__()-1):
        if(minmax[i]==1):
            minmaxIdx.append(i+1)
   #Refine min/max positions through scale space
    if (minmaxIdx.__len__()>0):
        for i in range(scales.__len__()-2,-1,-1):
            if(minmaxIdx.__len__()>0):
                minmax = FindLocalExtrema.FindLocalExtrema(dData[i], thresholds[i], scales[i], minmaxIdx)
            minmaxIdx.clear()
            for j in range(0, minmax.__len__()-1):
                if (minmax[j] == 1):
                    minmaxIdx.append(j + 1)

    minmaxIdx_convert = []
    minmax_convert = np.zeros(data.__len__())
    for element in minmaxIdx:
        minmaxIdx_convert.append(element+index+1-phi)


    for element in minmaxIdx_convert:
        minmax_convert[element-1-index-1] = 1


   #Find the data statistics in each region
    data = np.array(data)
    data = data.astype(np.float)
    stats = RegionStats.RegionStats(data, minmaxIdx_convert, tranRad,index,phi)
    return stats, minmaxIdx_convert

    #print(minmaxIdx_smooth)
#Print region statistics
#    format = '%5d\t%5.2f\t%5.2f'
    ''' if(flag == 1):
        print('Num         Time\t     Mean\t   Stdv')
        k = 1
        for i  in range(0,minmaxIdx_convert.__len__()):
            if(i==0):
                print('%d    ' %k, '[%5d' %(index-phi+1), '%5d)' %(minmaxIdx_convert[i]+1),'    %5.4f ' % stats[i][0], '  %5.4f ' % stats[i][1])
            else:
                temp =minmaxIdx_convert[i]-minmaxIdx_convert[i-1]-1
                if(temp <2):
                    continue
                print('%d    ' %k, '[%5d' %(minmaxIdx_convert[i-1]+1),'%5d)' %minmaxIdx_convert[i], '    %5.4f ' %stats[i][0], '  %5.4f ' %stats[i][1])
            k = k +1
        print('%d    ' %k, '[%5d' %(minmaxIdx_convert[minmaxIdx_convert.__len__()-1]+1),'%5d]' %(data.__len__()+index+1-phi), '    %5.4f' %stats[stats.__len__()-1][0], '   %5.4f' %stats[stats.__len__()-1][1])
    '''
#Divide_stats.Divide_stats(stats,minmaxIdx_smooth)