# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:12:05 2024

@author: stylelev
"""
from scipy.io import loadmat
import pandas as pd
import os
import numpy as np

# Set the input and output directories
input_dir = "C:\\..\\.." # Input folder path here
output_dir = "C:\\..\\.." # Output folder path here, make sure the folder exist

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to process each .mat file
def process_mat_file(file_path, output_dir):
    intit_name = os.path.splitext(os.path.basename(file_path))[0]
    mat = loadmat(file_path)

    # Assuming 'X' is a field in the loaded data
    X = mat[intit_name]['X']
    time_df = pd.DataFrame(columns=['Name', 'Type', 'Data', 'Unit', 'Raster'])

    for time_element in X:
        for item in time_element:
            name = item['Name'][0] if item['Name'].size > 0 else None
            Type = item['Type'][0] if item['Type'].size > 0 else None
            data = item['Data'][0].flatten().tolist() if item['Data'].size > 0 else None
            unit = item['Unit'][0] if item['Unit'].size > 0 else None
            raster = item['Raster'][0] if item['Raster'].size > 0 else None
            time_df = pd.concat([time_df, pd.DataFrame({'Name': [name], 'Type': [Type], 'Data': [data], 'Unit': [unit], 'Raster': [raster]})], ignore_index=True)

    expanded_time_data_df = pd.DataFrame()
    for index, row in time_df.iterrows():
        if row['Data'] is not None:
            temp_df = pd.DataFrame({'Data': row['Data']})
            temp_df['Name'] = row['Name']
            temp_df['Type'] = row['Type']
            temp_df['Unit'] = row['Unit']
            temp_df['Raster'] = row['Raster']
            expanded_time_data_df = pd.concat([expanded_time_data_df, temp_df], ignore_index=True)

    times = []
    for idx, data_row in expanded_time_data_df.iterrows():
        data = data_row['Data']
        if isinstance(data, np.ndarray):
            data = data.flatten()
        new_df = pd.DataFrame({'Time': data})
        times.append(new_df)

    # Process Y
    Y = mat[intit_name]['Y']
    df_Y = pd.DataFrame(columns=['Name', 'Type', 'Data', 'Unit', 'Raster', 'Device', 'XIndex', 'DownSampling', 'Description', 'DisplayIdentifier', 'Path', 'Flags', 'Min', 'Max', 'MinWeak', 'MaxWeak'])

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

    df_data = []
    for idx, data_row in expanded_data_df.iterrows():
        data = data_row['Data']
        name = data_row['Name']
        name = str(name[0])
        if isinstance(data, np.ndarray):
            data = data.flatten()
        new_df = pd.DataFrame({name: data})
        df_data.append(new_df)

    # Process Description
    Descr = mat[intit_name]['Description']
    df_desc = pd.DataFrame(columns=['General', 'Recording', 'Measurement'])

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

    df_desc = []
    for idx, data_row in expanded_desc_df.iterrows():
        data = data_row['General']
        if isinstance(data, np.ndarray):
            data = data.flatten()
        new_df = pd.DataFrame({'General': data})
        df_desc.append(new_df)

    df_desc_1 = df_desc[0]

    for row in df_desc_1['General']:
        if row is not None:
            user = row[0] if len(row) > 0 else None
            datetime = row[1] if len(row) > 1 else None
            origin = row[2] if len(row) > 2 else None
            description = row[3] if len(row) > 3 else None
            datetime = pd.to_datetime(datetime, format='%d.%m.%Y %H:%M:%S')

    # Process Info
    info = mat[intit_name]['Info']
    element = info[0]
    element_dict = element[0].tolist()

    revision_major = element[0][0][0]['RevisionMajor'][0][0]
    revision_minor = element[0][0][0]['RevisionMinor'][0][0]
    measurement_id = element[0][0][0]['MeasurementID'][0][0]

    # Final DataFrame
    df_final = pd.DataFrame()
    df_final = pd.concat([times[1], df_data[1], df_data[2]], axis=1)

    df_final = df_final.drop(df_final.columns[0], axis=1)
    time_stamp = datetime[0]
    time_stamp = time_stamp.strftime("%Y-%m-%d %H-%M-%S")
    file_name = f"{intit_name}_{time_stamp}.csv"
    file_path = os.path.join(output_dir, file_name)
    df_final.to_csv(file_path, index=False, header=False)
    print(f"CSV file saved as: {file_path}")

# Iterate over all .mat files in the input directory
for file_name in os.listdir(input_dir):
    if file_name.endswith(".mat"):
        file_path = os.path.join(input_dir, file_name)
        process_mat_file(file_path, output_dir)