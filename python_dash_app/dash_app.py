import numpy as np
import pandas as pd
import logging
import subprocess





def calculate_distance(array1, array2):
    # Create the input string for the C++ program
    input_data = f"{len(array1)}\n"
    input_data += " ".join(map(str, array1)) + "\n"
    input_data += " ".join(map(str, array2)) + "\n"

    # Execute the C++ program, provide the input and get the output
    result = subprocess.run(["cpp_scripts/euclidean.cpp"], input=input_data, text=True, capture_output=True)
    
    # Return the result as a float
    return float(result.stdout.strip())

# Test the function
array1_df = pd.read_csv('data/trainingset.csv')
array2_df = pd.read_csv('data/testingset.csv')
array1 = np.array(array1_df)
array2 = np.array(array2_df)


distance = calculate_distance(array1, array2)
print(f"Euclidean Distance: {distance}")