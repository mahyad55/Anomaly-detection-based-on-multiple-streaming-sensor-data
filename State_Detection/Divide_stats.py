from collections import deque
from State_Detection import define
from State_Detection import Distance
from Edge_Detector_1D import diff_sort

def Data2_Divide_stats(stats=[[[]]]):
    event = []
    C = []

    k = 8
    alpha = 0.5

    #Initilize Events and Cluster set
    for i in range(1,stats.__len__()-1):
        #print(stats[i][0])
        #print( stats[i][1])
        data2 = define.Data2()
        data2_C = define.Data2_C()

        data2.Start = stats[i][0]
        data2.End = stats[i][1]
        data2.Range = stats[i][2]
        data2.right_left = stats[i][3]
        data2.Max_Min = stats[i][4]
        data2.Mean = stats[i][5]
        data2.Stdv = stats[i][6]
        event.append(data2)

        #print(data2.Range)
        if (i < k + 2): #start from i = 1
            data2_C.Range = stats[i][2]
            data2_C.right_left = stats[i][3]
            data2_C.Max_Min = stats[i][4]
            data2_C.Mean = stats[i][5]
            data2_C.Stdv = stats[i][6]
            data2_C.events.append(i-1)
            C.append(data2_C)

    # Initilize d*
    update_distance = 1000000

    for i in range(0,k):
        #print(C[i].Range)
        for j in range(i+1,k+1):
            (flag,d) = Distance.Data2_Distance(C[i],C[j])
            if(d<update_distance and flag == 1):
                update_distance = d
                temp_i = i
                temp_j = j
    #print(temp_i)
    #print(temp_j)
    ##print("update_distance: %f" %update_distance)

    t =k + 1
    while t< event.__len__():
        # get the nearest cluster to event[t]
        #print('Event:%d' %(t+1), 'Range: %d' %event[t].Range)
        if(C.__len__()<=k):
            min_dis = 1000000
            for i in range(0,k):
                (flag,d) = Distance.Data2_Distance(event[t], C[i])
                if(d<min_dis and flag ==1):
                    min_dis = d
                    index = i

            #print('Nearest cluster:%d'%index ,'Crange %d' %C[index].Range)
            if(min_dis<= 2*update_distance):
                # add event[t] to the nearest cluster
                #event[t].state = index
                C[index].Range = C[index].Range + alpha*(event[t].Range-C[index].Range)
                C[index].right_left = C[index].right_left + alpha*(event[t].right_left - C[index].right_left)
                C[index].Max_Min = C[index].Max_Min + alpha*(event[t].Max_Min - C[index].Max_Min)
                C[index].Mean = C[index].Mean+alpha*(event[t].Mean-C[index].Mean)
                C[index].Stdv = C[index].Stdv+alpha*(event[t].Stdv-C[index].Stdv)
                C[index].events.append(t)

            #create new cluster comprising of event[t]
            else:
                #print("Create new cluster")
                data2_C = define.Data2_C()
                data2_C.Range = event[t].Range
                data2_C.right_left = event[t].right_left
                data2_C.Max_Min = event[t].Max_Min
                data2_C.Mean = event[t].Mean
                data2_C.Stdv = event[t].Stdv
                data2_C.events.append(t)
                C.append(data2_C)
            t = t +1
        else:
            #Clustering merging step
            Merge_distance = 1000000
            # find two closet clusters
            index_i = -1
            index_j = -1
            for i in range(0, k):
                for j in range(i+1, k + 1):
                    (flag,d) = Distance.Data2_Distance(C[i], C[j])
                    if (d < Merge_distance and flag ==1):
                        Merge_distance = d
                        index_i = i
                        index_j = j
            #print('Merge: %d' %index_i,'%d' %index_j )

            #Merge the clusters
            data2_C = define.Data4_C()
            data2_C.Range = (C[index_i].Range*C[index_i].events.__len__()
                             +C[index_j].Range*C[index_j].events.__len__())/(C[index_i].events.__len__()+C[index_j].events.__len__())
            data2_C.right_left = (C[index_i].right_left*C[index_i].events.__len__()+
                            C[index_j].right_left*C[index_j].events.__len__())/(C[index_i].events.__len__()+C[index_j].events.__len__())
            data2_C.Max_Min = (C[index_i].Max_Min*C[index_i].events.__len__()+
                               C[index_j].Max_Min*C[index_j].events.__len__())/(C[index_i].events.__len__()+C[index_j].events.__len__())
            data2_C.Mean = (C[index_i].Mean * C[index_i].events.__len__() +
                               C[index_j].Mean * C[index_j].events.__len__()) /(C[index_i].events.__len__() + C[index_j].events.__len__())
            data2_C.Stdv = (C[index_i].Stdv * C[index_i].events.__len__() +
                            C[index_j].Stdv * C[index_j].events.__len__()) / (
                                       C[index_i].events.__len__() + C[index_j].events.__len__())

            for i in range(0,C[index_i].events.__len__()):
                data2_C.events.append(C[index_i].events[i])
            for i in range(0,C[index_j].events.__len__()):
                data2_C.events.append(C[index_j].events[i])
            C.pop(index_i)
            C.pop(index_j-1)
            C.append(data2_C)
            update_distance = update_distance * 2
            #print("update_distance: %f" % update_distance)

    for i in range(0,C.__len__()):
        #print("Cluster : %d" % i)
        for j in range(0,C[i].events.__len__()):
            #start = (C[i].event[j].Start)

            #print('Event: %d'%C[i].events[j])
            index = C[i].events[j]
            event[index].state = i

    temp_state = []
    for i in range(0, event.__len__()):
        print('Event:%d' %(i+1),'State:%d' %event[i].state)
        temp_state.append(event[i].state)
    print(temp_state)
    return event


def Data4_Divide_stats(stats=[[[[[]]]]]):
    event = []
    C = []

    k = 10
    alpha = 0.5

    #Initilize Events and Cluster set
    for i in range(1,stats.__len__()-1):
        #print(stats[i][0])
        #print( stats[i][1])
        data4 = define.Data4()
        data4_C = define.Data4_C()

        data4.Start = stats[i][0]
        data4.End = stats[i][1]
        data4.Range = stats[i][2]
        data4.right_left = stats[i][3]
        data4.Max_Min = stats[i][4]
        data4.Mean = stats[i][5]
        event.append(data4)

        #print(data4.Range)
        if (i < k + 2): #start from i = 2
            data4_C.Range = stats[i][2]
            data4_C.right_left = stats[i][3]
            data4_C.Max_Min = stats[i][4]
            data4_C.Mean = stats[i][5]
            data4_C.events.append(i-1)
            C.append(data4_C)

    # Initilize d*
    update_distance = 1000000

    for i in range(0,k):
        #print(C[i].Range)
        for j in range(i+1,k+1):
            (flag,d) = Distance.Data4_Distance(C[i],C[j])
            if(d<update_distance):
                update_distance = d
                temp_i = i
                temp_j = j
    #print(temp_i)
    #print(temp_j)
    ##print("update_distance: %f" %update_distance)

    t = k + 1
    while t< event.__len__():
        # get the nearest cluster to event[t]
        #print('Event:%d' %(t+1), 'Range: %d' %event[t].Range)
        if(C.__len__()<=k):
            min_dis = 1000000
            for i in range(0,k):
                (flag,d) = Distance.Data4_Distance(event[t], C[i])
                if(d<min_dis and flag ==1):
                    min_dis = d
                    index = i

            #print('Nearest cluster:%d'%index ,'Crange %d' %C[index].Range)
            if(min_dis<= 2*update_distance):
                # add event[t] to the nearest cluster
                #event[t].state = index
                C[index].Range = C[index].Range + alpha*(event[t].Range-C[index].Range)
                C[index].right_left = C[index].right_left + alpha*(event[t].right_left - C[index].right_left)
                C[index].Max_Min = C[index].Max_Min + alpha*(event[t].Max_Min - C[index].Max_Min)
                C[index].Mean = C[index].Mean+alpha*(event[t].Mean-C[index].Mean)
                C[index].events.append(t)

            #create new cluster comprising of event[t]
            else:
                #print("Create new cluster")
                data4_C = define.Data4_C()
                data4_C.Range = event[t].Range
                data4_C.right_left = event[t].right_left
                data4_C.Max_Min = event[t].Max_Min
                data4_C.Mean = event[t].Mean
                data4_C.events.append(t)
                C.append(data4_C)
            t = t +1
        else:
            #Clustering merging step
            Merge_distance = 1000000
            # find two closet clusters
            index_i = -1
            index_j = -1
            for i in range(0, k):
                for j in range(i+1, k + 1):
                    (flag,d) = Distance.Data4_Distance(C[i], C[j])
                    if (d < Merge_distance and flag ==1):
                        Merge_distance = d
                        index_i = i
                        index_j = j
            #print('Merge: %d' %index_i,'%d' %index_j )

            #Merge the clusters
            data4_C = define.Data4_C()
            data4_C.Range = (C[index_i].Range*C[index_i].events.__len__()
                             +C[index_j].Range)*C[index_j].events.__len__()/(C[index_i].events.__len__()+C[index_j].events.__len__())
            data4_C.right_left = (C[index_i].right_left*C[index_i].events.__len__()+
                            C[index_j].right_left*C[index_j].events.__len__())/(C[index_i].events.__len__()+C[index_j].events.__len__())
            data4_C.Max_Min = (C[index_i].Max_Min*C[index_i].events.__len__()+
                               C[index_j].Max_Min*C[index_j].events.__len__())/(C[index_i].events.__len__()+C[index_j].events.__len__())
            data4_C.Mean = (C[index_i].Mean * C[index_i].events.__len__() +
                               C[index_j].Mean * C[index_j].events.__len__()) /(C[index_i].events.__len__() + C[index_j].events.__len__())
            for i in range(0,C[index_i].events.__len__()):
                data4_C.events.append(C[index_i].events[i])
            for i in range(0,C[index_j].events.__len__()):
                data4_C.events.append(C[index_j].events[i])
            C.pop(index_i)
            C.pop(index_j-1)
            C.append(data4_C)
            update_distance = update_distance * 2
            #print("update_distance: %f" % update_distance)

    for i in range(0,C.__len__()):
        #print("Cluster : %d" % i)
        for j in range(0,C[i].events.__len__()):
            #start = (C[i].event[j].Start)

            #print('Event: %d'%C[i].events[j])
            index = C[i].events[j]
            event[index].state = i

    temp_state = []
    for i in range(0, event.__len__()):
        print('Event:%d' %(i+1),'State:%d' %event[i].state)
        temp_state.append(event[i].state)
    print(temp_state)
    return event



def Data10_Divide_stats(stats=[[[[[]]]]]):
    event = []
    C = []

    k = 4
    alpha = 0.5

    #Initilize Events and Cluster set
    for i in range(1,stats.__len__()-1):
        data10 = define.Data10()
        data10_C = define.Data10_C()

        data10.Start = stats[i][0]
        data10.End = stats[i][1]
        data10.Range = stats[i][2]
        data10.Right_Local_min = stats[i][3]
        data10.Max_Min = stats[i][4]
        data10.Mean = stats[i][5]
        data10.Stdv = stats[i][6]
        event.append(data10)

        #print(data4.Range)
        if (i < k + 2): #start from i = 1
            data10_C.Range = stats[i][2]
            data10_C.Right_Local_min = stats[i][3]
            data10_C.Max_Min = stats[i][4]
            data10_C.Mean = stats[i][5]
            data10_C.Stdv = stats[i][6]
            data10_C.events.append(i-1)
            C.append(data10_C)

    # Initilize d*
    update_distance = 1000000

    for i in range(0,k):
        #print(C[i].Range)
        for j in range(i+1,k+1):
            (flag,d) = Distance.Data10_Distance(C[i],C[j])
            if(d<update_distance and flag == 1):
                update_distance = d
                temp_i = i
                temp_j = j
    #print(temp_i)
    #print(temp_j)
    ##print("update_distance: %f" %update_distance)

    t =k + 1
    while t< event.__len__():
        # get the nearest cluster to event[t]
        #print('Event:%d' %(t+1), 'Range: %d' %event[t].Range)
        if(C.__len__()<=k):
            min_dis = 1000000
            for i in range(0,k):
                (flag,d) = Distance.Data10_Distance(event[t], C[i])
                #print(t)
                #if(t == 7):
                 #   print(flag)
                 #   print(event[t].Start)
                if(d<min_dis and flag ==1):
                    min_dis = d
                    index = i

            #print('Nearest cluster:%d'%index ,'Crange %d' %C[index].Range)
            if(min_dis<= 2*update_distance):
                # add event[t] to the nearest cluster
                #event[t].state = index
                C[index].Range = C[index].Range + alpha*(event[t].Range-C[index].Range)
                C[index].Right_Local_min = C[index].Right_Local_min + alpha*(event[t].Right_Local_min - C[index].Right_Local_min)
                C[index].Max_Min = C[index].Max_Min + alpha*(event[t].Max_Min - C[index].Max_Min)
                C[index].Mean = C[index].Mean+alpha*(event[t].Mean-C[index].Mean)
                C[index].Stdv = C[index].Stdv+alpha*(event[t].Stdv-C[index].Stdv)
                C[index].events.append(t)

            #create new cluster comprising of event[t]
            else:
                #print("Create new cluster")
                data10_C = define.Data10_C()
                data10_C.Range = event[t].Range
                data10_C.Right_Local_min = event[t].Right_Local_min
                data10_C.Max_Min = event[t].Max_Min
                data10_C.Mean = event[t].Mean
                data10_C.Stdv = event[t].Stdv
                data10_C.events.append(t)
                C.append(data10_C)
            t = t +1
        else:
            #Clustering merging step
            Merge_distance = 1000000
            # find two closet clusters
            index_i = -1
            index_j = -1
            for i in range(0, k):
                for j in range(i+1, k + 1):
                    (flag,d) = Distance.Data10_Distance(C[i], C[j])
                    if (d < Merge_distance and flag ==1):
                        Merge_distance = d
                        index_i = i
                        index_j = j
            #print('Merge: %d' %index_i,'%d' %index_j )

            #Merge the clusters
            data10_C = define.Data4_C()
            data10_C.Range = (C[index_i].Range*C[index_i].events.__len__()
                             +C[index_j].Range*C[index_j].events.__len__())/(C[index_i].events.__len__()+C[index_j].events.__len__())
            data10_C.Right_Local_min = (C[index_i].Right_Local_min*C[index_i].events.__len__()+
                            C[index_j].Right_Local_min*C[index_j].events.__len__())/(C[index_i].events.__len__()+C[index_j].events.__len__())
            data10_C.Max_Min = (C[index_i].Max_Min*C[index_i].events.__len__()+
                               C[index_j].Max_Min*C[index_j].events.__len__())/(C[index_i].events.__len__()+C[index_j].events.__len__())
            data10_C.Mean = (C[index_i].Mean * C[index_i].events.__len__() +
                               C[index_j].Mean * C[index_j].events.__len__()) /(C[index_i].events.__len__() + C[index_j].events.__len__())
            data10_C.Stdv = (C[index_i].Stdv * C[index_i].events.__len__() +
                            C[index_j].Stdv * C[index_j].events.__len__()) / (
                                       C[index_i].events.__len__() + C[index_j].events.__len__())

            for i in range(0,C[index_i].events.__len__()):
                data10_C.events.append(C[index_i].events[i])
            for i in range(0,C[index_j].events.__len__()):
                data10_C.events.append(C[index_j].events[i])
            C.pop(index_i)
            C.pop(index_j-1)
            C.append(data10_C)
            update_distance = update_distance * 2
            #print("update_distance: %f" % update_distance)

    for i in range(0,C.__len__()):
        #print("Cluster : %d" % i)
        for j in range(0,C[i].events.__len__()):
            #start = (C[i].event[j].Start)

            #print('Event: %d'%C[i].events[j])
            index = C[i].events[j]
            event[index].state = i

    temp_state = []
    for i in range(0, event.__len__()):
        print('Event:%d' %(i+1),'State:%d' %event[i].state)
        temp_state.append(event[i].state)
    print(temp_state)
    return event
