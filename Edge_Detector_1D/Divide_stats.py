from collections import deque
from Edge_Detector_1D import diff_sort
from Edge_Detector_1D import define



def Divide_stats(stats=[[]],minmaxIdx_smooth=[]):
    clu = define.clu()
    diff = define.diff()
    cluster_queue = deque()
    Array_diff = []
    k = 0

    for i  in range(0,minmaxIdx_smooth.__len__()):
        if(i==0):
            length = minmaxIdx_smooth[0]
            clu.Leng = length
            clu.Mean = stats[i][0]
            clu.Stdv = stats[i][1]
            clu.state = k
            cluster_queue.append(clu)
            k = k + 1

        else:
            print("cluster queue")
            for j, element in enumerate(cluster_queue):
                print(element.Mean)
            print('\n')
            Array_diff.clear()
            length = minmaxIdx_smooth[i]- minmaxIdx_smooth[i-1]+1
            print("current element:")
            print(stats[i][0])
            print('\n')
            for element in enumerate(cluster_queue):
                diff.diff_Leng = abs(length-element[1].Leng)
                diff.diff_Mean = abs(stats[i][0]-element[1].Mean)
                diff.diff_Stdv = abs(stats[i][1]-element[1].Stdv)
                Array_diff.append(diff)

            Array_diff = diff_sort.diff_sort(Array_diff)


            if(Array_diff[0].diff_Leng>130):
                clu.Leng = length
                clu.Mean = stats[i][0]
                clu.Stdv = stats[i][1]
                clu.state = k
                cluster_queue.append(clu)
                k = k + 1
                continue
            if (Array_diff[0].diff_Mean > 0.36):
                clu.Leng = length
                clu.Mean = stats[i][0]
                clu.Stdv = stats[i][1]
                clu.state = k
                cluster_queue.append(clu)
                k = k + 1
                continue
            if (Array_diff[0].diff_Stdv > 0.025):
                clu.Leng = length
                clu.Mean = stats[i][0]
                clu.Stdv = stats[i][1]
                clu.state = k
                cluster_queue.append(clu)
                k = k + 1
                continue
            else:
                print(1)


