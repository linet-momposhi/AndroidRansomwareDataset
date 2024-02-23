# Combine 3 CSV files into one dataset called Android_Ransomware.csv

import pandas as pd
import numpy as np

# Load the datasets
data1 = pd.read_csv('Android_Ransomware_part_1.csv')
data2 = pd.read_csv('Android_Ransomware_part_2.csv')
data3 = pd.read_csv('Android_Ransomware_part_3.csv')

# Combine the datasets
data = pd.concat([data1, data2, data3], ignore_index=True)

# Save the combined dataset
data.to_csv('Android_Ransomware.csv', index=False)

# Print the shape of the combined dataset
print(data.shape)

#End of code