import numpy as np
from collections import deque

class H:
    def __init__(self):
        self.t_start = '';
        self.t_end = '';
        self.ApEn = '';

class seq:
    def __init__(self,sequence):
        self.sequence = [float(item) for item in sequence]

class Data2:
    def __init__(self):
        self.Start = '';
        self.End = '';
        self.Range = '';
        self.right_left = '';
        self.Max_Min = '';
        self.Mean = 0.0;
        self.Stdv = 0.0;
        self.state = -1;

class Data2_C:
    def __init__(self):
        self.Range = 0.0;
        self.right_left = 0.0;
        self.Max_Min = 0.0;
        self.Mean = 0.0;
        self.Stdv = 0.0;
        self.events = deque();

class Data4:
    def __init__(self):
        self.Start = '';
        self.End = '';
        self.Range = '';
        self.Right_Local_min = '';
        self.Max_Min = '';
        self.Mean = 0.0;
        self.state = -1;

class Data4_C:
    def __init__(self):
        self.Range = 0.0;
        self.Right_Local_min   = 0.0;
        self.Max_Min = 0.0;
        self.Mean = 0.0;
        self.events = deque();

class Data10:
    def __init__(self):
        self.Start = '';
        self.End = '';
        self.Range = '';
        self.Right_Local_min  = '';
        self.Max_Min = '';
        self.Mean = 0.0;
        self.Stdv = 0.0;
        self.state = -1;

class Data10_C:
    def __init__(self):
        self.Range = 0.0;
        self.Right_Local_min  = 0.0;
        self.Max_Min = 0.0;
        self.Mean = 0.0;
        self.Stdv = 0.0;
        self.events = deque();

