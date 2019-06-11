from State_Detection import define
from State_Detection import Data_Merit
from State_Detection import Divide_stats
from Edge_Detector_1D import AnalyzeEdges
from Edge_Detector_1D import RegionStats
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from pylab import *
import numpy as np
from collections import deque
import csv
import matplotlib.pyplot as plt

#defaults
tranRad = 1
t_prev_event = 1
phi = 350
delta = 450
start_point = 2500
seq = []
seq_queue = deque()
data = []

def Data2_Print(stats = [], minmaxIdx_global = []):
    print('Num         Time\t     Range\t \t    End-Start\t   Max-Min\t    Mean\t     Stdv')
    k = 0
    for i in range(1, minmaxIdx_global.__len__()):
        k = k + 1
        if (i == 0):
            print('%d    ' % k, ' [%5d' % stats[i][0], '%5d)' % stats[i][1], '    %d  ' % stats[i][2],
                  '         %5.4f ' % stats[i][3], '            %5.4f ' % stats[i][4],
                  '    %5.4f ' % stats[i][5], '    %5.4f ' % stats[i][6])
        if (0 < i and i < 9):
            print('%d    ' % k, '  [%5d' % stats[i][0], '%5d)' % stats[i][1],
                  '   %d  ' % stats[i][2], '         %5.4f ' % stats[i][3], '        %5.4f ' % stats[i][4],
                  '    %5.4f ' % stats[i][5], '    %5.4f ' % stats[i][6])

        if (9 <= i and i < minmaxIdx_global.__len__()):
            print('%d    ' % k, '  [%5d' % stats[i][0], '%5d)' % stats[i][1],
                  '  %d  ' % stats[i][2], '         %5.4f ' % stats[i][3], '        %5.4f ' % stats[i][4],
                  '    %5.4f ' % stats[i][5], '    %5.4f ' % stats[i][6])
    plt.figure(figsize=(15, 12))
    plt.plot(data)
    plt.plot(1.0 * minmax_global * max(data), 'r')
    plt.show()

    '''
    print('Num         Time\t     Mean\t   Stdv')
    k=1
    for i  in range(0,minmaxIdx_global.__len__()):
        if(i==0):
            print('%d    ' %k, '[%5d' %1, '%5d)' %(minmaxIdx_global[i]),'    %5.4f ' % stats[i][0], '  %5.4f ' % stats[i][1])
        else:
            print('%d    ' %k, '[%5d' %(minmaxIdx_global[i-1]),'%5d)' %minmaxIdx_global[i], '    %5.4f ' %stats[i][0], '  %5.4f ' %stats[i][1])
        k = k +1
    print('%d    ' %k, '[%5d' %(minmaxIdx_global[minmaxIdx_global.__len__()-1]),'%5d]' %(data.__len__()), '    %5.4f' %stats[stats.__len__()-1][0], '   %5.4f' %stats[stats.__len__()-1][1])
    '''
    
def Data4_Print(stats = [], minmaxIdx_global = []):
    print('Num         Time\t     Range\t    Local_min-Start\t   Max-Min\t    Mean')
    k = 0
    for i in range(1, minmaxIdx_global.__len__()):
        k = k + 1
        if (i == 0):
            print('%d    ' % k, ' [%5d' % stats[i][0], '%5d)' % stats[i][1], '    %d  ' % stats[i][2],
                  '         %5.4f ' % stats[i][3], '            %5.4f ' % stats[i][4], '    %5.4f ' % stats[i][5])
        if (0 < i and i < 9):
            print('%d    ' % k, '  [%5d' % stats[i][0], '%5d)' % stats[i][1],
                  '   %d  ' % stats[i][2], '         %5.4f ' % stats[i][3], '        %5.4f ' % stats[i][4],
                  '    %5.4f ' % stats[i][5])

        if (9 <= i and i < minmaxIdx_global.__len__()):
            print('%d    ' % k, '  [%5d' % stats[i][0], '%5d)' % stats[i][1],
                  '  %d  ' % stats[i][2], '         %5.4f ' % stats[i][3], '        %5.4f ' % stats[i][4],
                  '    %5.4f ' % stats[i][5])
    plt.figure(figsize=(15, 12))
    plt.plot(data)
    plt.plot(1.0 * minmax_global * max(data), 'r')
    plt.show()
    

def Data10_Print(stats = [], minmaxIdx_global = []):
    print('Num         Time\t     Range\t \t    End-Local_min\t  Max-Min\t   Mean\t    Stdv')
    k = 0
    for i in range(1, minmaxIdx_global.__len__()):
        k = k + 1
        if (i == 0):
            print('%d    ' % k, ' [%5d' % stats[i][0], '%5d)' % stats[i][1], '    %d  ' % stats[i][2],
                  '         %5.4f ' % stats[i][3], '            %5.4f ' % stats[i][4],
                  '    %5.4f ' % stats[i][5], '    %5.4f ' % stats[i][6])
        if (0 < i and i < 9):
            print('%d    ' % k, '  [%5d' % stats[i][0], '%5d)' % stats[i][1],
                  '   %d  ' % stats[i][2], '         %5.4f ' % stats[i][3], '        %5.4f ' % stats[i][4],
                  '    %5.4f ' % stats[i][5], '    %5.4f ' % stats[i][6])

        if (9 <= i and i < minmaxIdx_global.__len__()):
            print('%d    ' % k, '  [%5d' % stats[i][0], '%5d)' % stats[i][1],
                  '  %d  ' % stats[i][2], '         %5.4f ' % stats[i][3], '        %5.4f ' % stats[i][4],
                  '    %5.4f ' % stats[i][5], '    %5.4f ' % stats[i][6])

    plt.figure(figsize=(15, 12))
    plt.plot(data)
    plt.plot(1.0 * minmax_global * max(data), 'r')
    plt.show()
    
    
'''
minmaxIdx_global = []
minmax_global = np.zeros(50000)
with open('Data2_prey.csv') as csvfile:
    reader = csv.reader(csvfile)
    for index, row in enumerate(reader):
        seq.clear()
        data.append(row[0])
        if start_point<=index and index <start_point+phi-1:
            seq_queue.append(row[0])

        if start_point+phi-1 <=index and index<50000:
            if phi-1+start_point < index:
                seq_queue.popleft()
            seq_queue.append(row[0])
            for i, element in enumerate(seq_queue):
                seq.append(element)
            print(index+1-phi+1)
            #print(seq)
            (stats,minmaxIdx_local) = AnalyzeEdges.AnalyzeEdges(seq,index,phi)
                #if(ref.__len__()>0):
                    #print(ref)
                #print(H.t_start,H.t_end)
            for element in minmaxIdx_local:
               #print(element)
                minmax_global[element] = 1

for i in range(0, minmax_global.__len__() ):
    if (minmax_global[i] == 1):
        if(i+1-t_prev_event) < delta:
            minmax_global[i]= 0
        else:
            t_prev_event = i+1
            minmaxIdx_global.append(i)
print(minmaxIdx_global)
for i in minmaxIdx_global:
    minmax_global[i]= 1
data = np.array(data)
data = data.astype(np.float)
#stats1 = RegionStats.RegionStats(data, minmaxIdx_global, tranRad)
stats = Data_Merit.Data2_Merit(data, minmaxIdx_global)
Data2_Print(stats, minmaxIdx_global)
Divide_stats = Divide_stats.Data2_Divide_stats(stats)
'''



#data2
'''
with open('Data2_prey.csv') as csvfile:
    reader = csv.reader(csvfile)
    for index,row in enumerate(reader):
            data.append(row[0])

minmax_global = np.zeros(data.__len__())
minmaxIdx_global = []
length = data.__len__()
minmaxIdx_global = [4506,5377,6840,7643,9562,10261,11028,11925,12782,14744,15419,17110,17748,19203,20068,21729,22453,24078,25176,26553,27254,28899,29576,31500,32220,34020,34809,36670,37905,38832,39724,41128,42330,43581,44479,46144,46965,48593]

for i in minmaxIdx_global:
    minmax_global[i]= 1
data = np.array(data)
data = data.astype(np.float)
#stats1 = RegionStats.RegionStats(data, minmaxIdx_global, tranRad)
stats = Data_Merit.Data2_Merit(data, minmaxIdx_global)
Data2_Print(stats, minmaxIdx_global)
Divide_stats = Divide_stats.Data2_Divide_stats(stats)
'''

#data4
'''
with open('Data4_prey.csv') as csvfile:
    reader = csv.reader(csvfile)
    for index,row in enumerate(reader):
            data.append(row[0])

minmax_global = np.zeros(data.__len__())
minmaxIdx_global = []
length = data.__len__()
minmaxIdx_global = [4637,7030,9733,11157,12187,14888,17347,19417,21947,24279,26792,29042,31638,34219,36862,38968,41488,43787,46264,48829]
for i in minmaxIdx_global:
    minmax_global[i]= 1
data = np.array(data)
data = data.astype(np.float)
#stats1 = RegionStats.RegionStats(data, minmaxIdx_global, tranRad)
stats = Data_Merit.Data4_Merit(data, minmaxIdx_global)
Data4_Print(stats, minmaxIdx_global)
Divide_stats = Divide_stats.Data4_Divide_stats(stats)
'''


#data10

with open('Data10_prey.csv') as csvfile:
    reader = csv.reader(csvfile)
    for index,row in enumerate(reader):
            data.append(row[0])

minmax_global = np.zeros(data.__len__())
minmaxIdx_global = []
length = data.__len__()
minmaxIdx_global = [4544,6922,9666,11286,14435,16882,19218,21883,24103,26571,28931,31397,34161,36659,38989,41336,43583,46149,48478]
for i in minmaxIdx_global:
    minmax_global[i]= 1
data = np.array(data)
data = data.astype(np.float)
#stats1 = RegionStats.RegionStats(data, minmaxIdx_global, tranRad)
stats = Data_Merit.Data10_Merit(data, minmaxIdx_global)
Data10_Print(stats, minmaxIdx_global)
Divide_stats = Divide_stats.Data10_Divide_stats(stats)


#the time of data read is very long, so to save time, after the minmaxIdx_global result, just put it in this set.
#And can choose to presnt the result of Data set 2/4/10. Here is the result of data 10.






