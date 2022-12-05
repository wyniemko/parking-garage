# -*- coding: utf-8 -*-
"""
Original file is located at
    https://colab.research.google.com/drive/16O_Qx6Fx_IS9Y2_5bSHO_NHkk746x0Sc
"""

import csv

# Open the garage.csv file and read the data into a list of dictionaries
with open('garage.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)

# Initialize a dictionary to store the minimum values and column names for each time/day
min_values = {}

# Iterate over the rows in the data
for row in data:
    # Get the time/day for the current row
    time_day = row['Time'] + '/' + row['Day']

    # If this time/day has not been seen before, initialize its minimum value and column name
    if time_day not in min_values:
        min_values[time_day] = {'value': float('inf'), 'column': ''}

    # Update the minimum value and column name, if necessary
    if float(row['Northwestern']) < min_values[time_day]['value']:
        min_values[time_day]['value'] = float(row['Northwestern'])
        min_values[time_day]['column'] = 'Northwestern'
    if float(row['University']) < min_values[time_day]['value']:
        min_values[time_day]['value'] = float(row['University'])
        min_values[time_day]['column'] = 'University'
    if float(row['Grant']) < min_values[time_day]['value']:
        min_values[time_day]['value'] = float(row['Grant'])
        min_values[time_day]['column'] = 'Grant'
    if float(row['Wood']) < min_values[time_day]['value']:
        min_values[time_day]['value'] = float(row['Wood'])
        min_values[time_day]['column'] = 'Wood'

# Print a header row for the table
print('Time/Day\tMinimum\tColumn')

# Print the minimum value and column for each time/day in a tab-separated table
for time_day, values in min_values.items():
    print(f'{time_day}\t{values["value"]}\t{values["column"]}')
