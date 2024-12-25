import pickle
import numpy as np
import matplotlib.pyplot as plt

from HybridAStar import HybridAStar

# 提取data
with open('data.pkl', 'rb') as f:
    data = pickle.load(f)
    map_bev = data['map_bev']
    start_xyt = data['start_xyt']
    end_xyt = data['end_xyt']

