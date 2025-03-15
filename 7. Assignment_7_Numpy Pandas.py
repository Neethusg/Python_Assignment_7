***Assignment 7_ Numpy Pandas***


# Exercise 1

import numpy as np

arr = np.arange(1, 11)
matrix = arr.reshape(2, 5)

print(matrix)

# Exercise 2

import numpy as np
arr = np.arange(1, 21)
extracted = arr[5:15]

print(extracted)

# Exercise 3

import pandas as pd
fruits = pd.Series({'apples': 3, 'bananas': 2, 'oranges': 1})
fruits['pears'] = 4    # Adding a new item

print(fruits)

# Exercise 4

import pandas as pd

data = {
    'name': ['Ann', 'Boby', 'Charlie', 'Davood', 'Elsa',
             'Denny', 'Grace', 'Honey', 'Ivan', 'John'],
    'age': [21, 30, 32, 28, 25, 35, 39, 24, 26, 31],
    'gender': ['Female', 'Male', 'Male', 'Male', 'Female',
               'Male', 'Female', 'Female', 'Male', 'Male']
}

df = pd.DataFrame(data)
print(df)

# Exercise 5

import pandas as pd

data = {
    'name': ['Ann', 'Boby', 'Charlie', 'Davood', 'Elsa',
             'Denny', 'Grace', 'Honey', 'Ivan', 'John'],
    'age': [21, 30, 32, 28, 25, 35, 39, 24, 26, 31],
    'gender': ['Female', 'Male', 'Male', 'Male', 'Female',
               'Male', 'Female', 'Female', 'Male', 'Male']
}

df = pd.DataFrame(data)
df['occupation'] = ['Programmer', 'Manager', 'Analyst', 'Programmer', 'Manager',
                     'Analyst', 'Programmer', 'Manager', 'Analyst', 'Programmer']
print(df)

# Exercise 6

import pandas as pd

data = {
    'name': ['Ann', 'Boby', 'Charlie', 'Davood', 'Elsa',
             'Denny', 'Grace', 'Honey', 'Ivan', 'John'],
    'age': [21, 30, 32, 28, 25, 35, 39, 24, 26, 31],
    'gender': ['Female', 'Male', 'Male', 'Male', 'Female',
               'Male', 'Female', 'Female', 'Male', 'Male']
}

df = pd.DataFrame(data)
df['occupation'] = ['Programmer', 'Manager', 'Analyst', 'Programmer', 'Manager',
                     'Analyst', 'Programmer', 'Manager', 'Analyst', 'Programmer']

df1 = df[df['age'] >= 30]
print(df1)

# Exercise 7

import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma',
             'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
    'age': [25, 30, 22, 28, 27, 35, 29, 24, 26, 31],
    'gender': ['Female', 'Male', 'Male', 'Male', 'Female',
               'Male', 'Female', 'Female', 'Male', 'Male'],
    'occupation': ['Programmer', 'Manager', 'Analyst', 'Programmer', 'Manager',
                   'Analyst', 'Programmer', 'Manager', 'Analyst', 'Programmer']
}

df = pd.DataFrame(data)

# Convert the DataFrame to a CSV file
df.to_csv('employee_data.csv', index=False)

# Read the CSV file back into a DataFrame
df_from_csv = pd.read_csv('employee_data.csv')
print(df_from_csv)

