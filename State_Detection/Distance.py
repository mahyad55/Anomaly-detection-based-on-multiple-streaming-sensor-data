from State_Detection import define


def Data2_Distance(Datai = define.Data2(), Dataj = define.Data2()):
    a = 0  #right - left
    b = 0.1  #Max-Min
    c = 0.65  #Mean
    d = 0.25     #stdv
    flag = 1
    diff_range = abs(Dataj.Range-Datai.Range)
    if(Dataj.Range > Datai.Range):
        bigger = Dataj.Range
    else:
        bigger = Datai.Range
    diff_Mean = abs(Dataj.Mean-Datai.Mean)
    diff_Stdv = abs(Dataj.Stdv-Datai.Stdv)
    diff_MM = abs(Dataj.Max_Min-Datai.Max_Min)
    if(diff_range/bigger > 0.3):
        flag = 0
    #if(Datai.right_left*Dataj.right_left<0):
    #    flag = 0
    if (diff_Mean > 0.2):
        flag = 0
    if(diff_Stdv>0.1):
        flag = 0
    #if(Datai.Range == 803 or Datai.Range ==699):
        #print(flag)
    #print('Diff_range: %d' %diff_range)
    diff_ES = (Dataj.right_left- Datai.right_left)*100.0
    diff_MM = (Dataj.Max_Min-Datai.Max_Min)*100.0
    diff_Mean = (Dataj.Mean-Datai.Mean)*100.0
    diff_Stdv = (Dataj.Stdv-Datai.Stdv)*50.0

    diff = a*diff_ES*diff_ES+b*diff_MM*diff_MM+c*diff_Mean*diff_Mean+d*diff_Stdv*diff_Stdv

    return flag,diff

def Data4_Distance(Datai = define.Data4(), Dataj = define.Data4()):
    a = 0.15
    b = 0.35
    c = 0.5
    flag = 1
    diff_range = abs(Dataj.Range-Datai.Range)
    if(diff_range > 450):
        flag = 0
    if (Datai.right_left * Dataj.right_left < 0):
        flag = 0
    #print('Diff_range: %d' %diff_range)
    diff_ES = (Dataj.right_left- Datai.right_left)*100.0
    diff_MM = (Dataj.Max_Min-Datai.Max_Min)*100.0
    diff_Mean = (Dataj.Mean-Datai.Mean)*100.0

    diff = a*diff_ES*diff_ES+b*diff_MM*diff_MM+c*diff_Mean*diff_Mean

    return flag,diff


def Data10_Distance(Datai = define.Data10(), Dataj = define.Data10()):
    a = 0.4  #Right - local_min
    b = 0.3 #Max-Min
    c = 0.15  #Mean
    d = 0.15  #stdv
    flag = 1

    diff_range = abs(Dataj.Range-Datai.Range)
    if(Dataj.Range > Datai.Range):
        bigger = Dataj.Range
    else:
        bigger = Datai.Range

    diff_RMin = abs(Dataj.Right_Local_min-Datai.Right_Local_min)
    diff_MM = abs(Dataj.Max_Min - Datai.Max_Min)

    if(diff_range/bigger > 0.3):
        flag = 0
    if(diff_RMin>0.2):
        flag = 0
    if(diff_MM>0.1):
        flag = 0

    #if(Datai.Range == 803 or Datai.Range ==699):
        #print(flag)
    #print('Diff_range: %d' %diff_range)
    diff_ES = (Dataj.Right_Local_min- Datai.Right_Local_min)*100.0
    diff_MM = (Dataj.Max_Min-Datai.Max_Min)*100.0
    diff_Mean = (Dataj.Mean-Datai.Mean)*100.0
    diff_Stdv = (Dataj.Stdv-Datai.Stdv)*100.0

    diff = a*diff_ES*diff_ES+b*diff_MM*diff_MM+c*diff_Mean*diff_Mean+d*diff_Stdv*diff_Stdv

    return flag,diff
