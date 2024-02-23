# Combine 3 CSV files into one dataset called Android_Ransomware.csv

import pandas as pd
import numpy as np

# Load the datasets
data1 = pd.read_csv('Android_Ransomware_part_1.csv')
data2 = pd.read_csv('Android_Ransomware_part_2.csv')
data3 = pd.read_csv('Android_Ransomware_part_3.csv')

# Combine the datasets
android = pd.concat([data1, data2, data3], ignore_index=True)

# Rest of your code goes here