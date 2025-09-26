# Anscombe's Quartet dataset

import pandas as pd
import seaborn as sns
import os

print("Starting the download process...")

# Anscombe's Quartet is a single dataset in seaborn with a 'dataset' column
# that identifies which of the four subsets (I, II, III, IV) each row belongs to.
try:
    # 1. Load the main dataset from seaborn's online repository
    anscombe_df = sns.load_dataset("anscombe")
    print("Successfully loaded the Anscombe's Quartet dataset.")

    # 2. Find the unique identifiers for each subset
    dataset_names = anscombe_df['dataset'].unique() # This will be ['I', 'II', 'III', 'IV']

    # 3. Loop through each subset and save it as a separate CSV file
    for name in dataset_names:
        # Filter the dataframe to get only the data for the current subset
        subset_df = anscombe_df[anscombe_df['dataset'] == name]
        
        # Define the filename
        file_name = f"anscombe_dataset_{name}.csv"
        
        # Save the subset to a CSV file. index=False prevents pandas from writing row indices into the file.
        subset_df.to_csv(file_name, index=False)
        
        print(f"-> Saved '{file_name}' to directory: {os.getcwd()}")

    print("\n✅ All 4 datasets have been saved successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
    print("Please check your internet connection and ensure you have the required libraries installed.")