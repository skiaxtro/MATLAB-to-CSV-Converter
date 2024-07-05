# -*- coding: utf-8 -*-
"""
Created on Fri Jul 05 12:12:05 2024

@author: Eleftheriadis Stylianos
"""
from scipy.io import loadmat
import pandas as pd
import os
import numpy as np

# Your file's path here
os.chdir("") 

##############################################################################################################################################

######################################################### DATA X #####################################################################
#                                                      ACHIEVE TIME
# Load the .mat file
# Set name
intit_name = "N09_M07_F10_K001_1"
mat = loadmat(intit_name + ".mat")

# Check the keys in the loaded data
print(mat.keys())

# Assuming 'X' is a field in the loaded data
X = mat['N09_M07_F10_K001_1']['X']

# Print the names of the fields in 'X', if None check the elements
# print(X.dtype.names)

# # Accessing elements from the NumPy array X
# time_element = X[0]  # Access the first time_element
# print(time_element)

# If X is a multi-dimensional array, access elements like this
time_element = X[0, 0]  # Access the time_element at the first row and first column
# print(time_element)

# Create an empty DataFrame with name collumns from X elements
time_df = pd.DataFrame(columns=['Name', 'Type', 'Data', 'Unit', 'Raster'])

# Iterate through each time_element in X and append its content to the DataFrame
for time_element in X:
    for item in time_element:
        name = item['Name'][0] if item['Name'].size > 0 else None
        Type = item['Type'][0] if item['Type'].size > 0 else None
        data = item['Data'][0].flatten().tolist() if item['Data'].size > 0 else None
        unit = item['Unit'][0] if item['Unit'].size > 0 else None
        raster = item['Raster'][0] if item['Raster'].size > 0 else None
        time_df = pd.concat([time_df, pd.DataFrame({'Name': [name], 'Type': [Type], 'Data': [data], 'Unit': [unit], 'Raster': [raster]})], ignore_index=True)



# Create a new DataFrame with expanded "Data" values
expanded_time_data_df = pd.DataFrame()
for index, row in time_df.iterrows():
    if row['Data'] is not None:
        temp_df = pd.DataFrame({'Data': row['Data']})
        temp_df['Name'] = row['Name']
        temp_df['Type'] = row['Type']
        temp_df['Unit'] = row['Unit']
        temp_df['Raster'] = row['Raster']
        expanded_time_data_df = pd.concat([expanded_time_data_df, temp_df], ignore_index=True)

# Print the expanded DataFrame
# print(expanded_time_data_df)


# Assuming expanded_time_data_df contains the expanded DataFrame
times = []

# Iterate through each time_element in expanded_time_data_df['Data']
for idx, data_row in expanded_time_data_df.iterrows():
    data = data_row['Data']
    if isinstance(data, np.ndarray):
        data = data.flatten()
    new_df = pd.DataFrame({'Time': data})
    times.append(new_df)

# Print each DataFrame
# for i, time_df in enumerate(times, 1):
#     print(f"DataFrame {i}:")
#     print(time_df)
#     print('\n')
    
######################################################### DATA Y #####################################################################
#                                                      ACHIEVE DATA
# Set name
Y = mat['N09_M07_F10_K001_1']['Y']

# Print the names of the fields in 'Y'
# print(Y.dtype.names)

# If Y is a multi-dimensional array,access elements like this
element = Y[0, 0]  # Access the element at the first row and first column
# print(element)

# Create an empty DataFrame with column's names of elements in Y
df_Y = pd.DataFrame(columns=['Name', 'Type', 'Data', 'Unit', 'Raster', 'Device', 'Xindex', 'DownSampling', 'Description', 'DisplayIdentifier', 'Path', 'Flags', 'Min', 'Max', 'MinWeak', 'MaxWeak'])

# Iterate through each element in T and append its content to the DataFrame
for element in Y:
    for item in element:
        Name = item['Name'][0] if item['Name'].size > 0 else None
        Type = item['Type'][0] if item['Type'].size > 0 else None
        Data = item['Data'][0].flatten().tolist() if item['Data'].size > 0 else None
        Unit = item['Unit'][0] if item['Unit'].size > 0 else None
        Raster = item['Raster'][0] if item['Raster'].size > 0 else None
        Device = item['Device'][0] if item['Device'].size > 0 else None
        XIndex = item['XIndex'][0] if item['XIndex'].size > 0 else None
        DownSampling = item['DownSampling'][0] if item['DownSampling'].size > 0 else None
        Description = item['Description'][0] if item['Description'].size > 0 else None
        DisplayIdentifier = item['DisplayIdentifier'][0] if item['DisplayIdentifier'].size > 0 else None
        Path = item['Path'][0] if item['Path'].size > 0 else None
        Flags = item['Flags'][0] if item['Flags'].size > 0 else None
        Min = item['Min'][0] if item['Min'].size > 0 else None
        Max = item['Max'][0] if item['Max'].size > 0 else None
        MinWeak = item['MinWeak'][0] if item['MinWeak'].size > 0 else None
        MaxWeak = item['MaxWeak'][0] if item['MaxWeak'].size > 0 else None



        df_Y = pd.concat([df_Y, pd.DataFrame({'Name': [Name], 'Type': [Type], 'Data': [Data], 'Unit': [Unit], 'Raster': [Raster], 'Device': [Device], 'XIndex': [XIndex], 'DownSampling': [DownSampling], 'Description': [Description], 'DisplayIdentifier': [DisplayIdentifier], 'Path': [Path], 'Flags': [Flags], 'Min': [Min], 'Max': [Max], 'MinWeak': [MinWeak], 'MaxWeak': [MaxWeak]})], ignore_index=True)
        
        
expanded_data_df = pd.DataFrame()
for index, row in df_Y.iterrows():
    if row['Data'] is not None:
        temp_df = pd.DataFrame({'Data': row['Data']})
        temp_df['Name'] = row['Name']
        temp_df['Type'] = row['Type']
        temp_df['Unit'] = row['Unit']
        temp_df['Raster'] = row['Raster']
        temp_df['Device'] = row['Device']
        temp_df['XIndex'] = row['XIndex']
        temp_df['DownSampling'] = row['DownSampling']
        temp_df['Description'] = row['Description']
        temp_df['DisplayIdentifier'] = row['DisplayIdentifier']
        temp_df['Path'] = row['Path']
        temp_df['Flags'] = row['Flags']
        temp_df['Min'] = row['Min']
        temp_df['Max'] = row['Max']
        temp_df['MinWeak'] = row['MinWeak']
        temp_df['MaxWeak'] = row['MaxWeak']

        
        
        expanded_data_df = pd.concat([expanded_data_df, temp_df], ignore_index=True)

# Print the expanded DataFrame
# print(expanded_data_df)
 
        
# Assuming expanded_data_df contains the expanded DataFrame
df_data = []

# Iterate through each element in expanded_data_df['Data']
for idx, data_row in expanded_data_df.iterrows():
    data = data_row['Data']
    name = data_row['Name']
    name = str(name[0])
    if isinstance(data, np.ndarray):
        data = data.flatten()
    new_df = pd.DataFrame({name: data})
    df_data.append(new_df)

# Print each DataFrame
# for i, time_df in enumerate(df_data, 1):
#     print(f"DataFrame {i}:")
#     print(df_data)
#     print('\n')
    
 
######################################################### DATA DESCRIPTION ###########################################################
#                                                      ACHIEVE TIMESTAMP

# Set name
Descr = mat['N09_M07_F10_K001_1']['Description']
# print(Descr.dtype.names)

# If DESCRIPTION is a multi-dimensional array, access elements like this
element = Descr[0, 0]  # Access the element at the first row and first column
# print(element)

# Create an empty DataFrame with column's names of elements in Descr
df_desc = pd.DataFrame(columns=['General', 'Recording', 'Measurement'])

# Iterate through each element in Descr and append its content to the DataFrame
for element in Descr:
    for item in element:
        General = item['General'][0] if item['General'].size > 0 else None
        Recording = item['Recording'][0] if item['Recording'].size > 0 else None
        Measurement = item['Measurement'][0].flatten().tolist() if item['Measurement'].size > 0 else None

        df_desc = pd.concat([df_desc, pd.DataFrame({'General': [General], 'Recording': [Recording], 'Measurement': [Measurement]})], ignore_index=True)


expanded_desc_df = pd.DataFrame()
for index, row in df_desc.iterrows():
    if row['General'] is not None:
        temp_df = pd.DataFrame({'General': row['General']})
        temp_df['Recording'] = row['Recording']
        temp_df['Measurement'] = row['Measurement']
        
        
        expanded_desc_df = pd.concat([expanded_desc_df, temp_df], ignore_index=True)

# Print the expanded DataFrame
# print(expanded_desc_df)
 

# Assuming expanded_desc_df contains the expanded DataFrame
df_desc = []

# Iterate through each element in expanded_desc_df['General']
for idx, data_row in expanded_desc_df.iterrows():
    data = data_row['General']
    # name = data_row['Name']
    # name = str(name[0])
    if isinstance(data, np.ndarray):
        data = data.flatten()
    new_df = pd.DataFrame({'General': data})
    df_desc.append(new_df)

# Print each DataFrame
# for i, time_df in enumerate(df_desc, 1):
#     print(f"DataFrame {i}:")
#     print(df_desc)
#     print('\n')



df_desc_1 = df_desc[0]
# print(df_desc_1['General'].dtype)

# print(type(df_desc_1['General'].iloc[0]))


# # Define lists to store the extracted information
# users = []
# datetimes = []
# origins = []
# descriptions = []

# Iterate over each row in the DataFrame
for row in df_desc_1['General']:
    # Check if the row is not None
    if row is not None:
        # Extract information from the tuple
        user = row[0] if len(row) > 0 else None
        datetime = row[1] if len(row) > 1 else None
        origin = row[2] if len(row) > 2 else None
        description = row[3] if len(row) > 3 else None
        
        # Convert datetime string to pandas Timestamp object
        datetime = pd.to_datetime(datetime, format='%d.%m.%Y %H:%M:%S')
        

    #     # Append the extracted information to the respective lists
    #     users.append(user)
    #     datetimes.append(datetime)
    #     origins.append(origin)
    #     descriptions.append(description)
    # else:
    #     # If the row is None, append None values to all lists
    #     users.append(None)
    #     datetimes.append(None)
    #     origins.append(None)
    #     descriptions.append(None)
# print(datetime)

######################################################### DATA INFO ###########################################################
#                                                      ACHIEVE Revisions and Measurement ID

# Set name
# Assuming 'X' is a field in the loaded data
info = mat['N09_M07_F10_K001_1']['Info']

# Accessing the first element in the 'info' array
element = info[0]
print(element)

# Convert structured array to dictionary
element_dict = element[0].tolist()

# Extracting values from 'element'
revision_major = element[0][0][0]['RevisionMajor'][0][0]
revision_minor = element[0][0][0]['RevisionMinor'][0][0]
measurement_id = element[0][0][0]['MeasurementID'][0][0]

print("RevisionMajor:", revision_major)
print("RevisionMinor:", revision_minor)
print("MeasurementID:", measurement_id)

############################################################## FINAL DF ########################################################
#                                                              CURRENT
df_final = pd.DataFrame()

# Append dataframes
df_final = pd.concat([times[1], df_data[1], df_data[2]], axis=1)

time_stamp = datetime[0]
time_stamp = time_stamp.strftime("%Y-%m-%d %H-%M-%S")
print(time_stamp)

# EXPORT AS CSV

file_name = f"{intit_name}_{time_stamp}.csv"
df_final.to_csv(file_name, index=False)
print(f"CSV file saved as: {file_name}")




