import seaborn as sns
import pandas as pd

# Load the dataset
df = sns.load_dataset("anscombe")

# You can see the four datasets are marked by the 'dataset' column
print(df.head())

# To work with just the first dataset, for example:
df_I = df[df['dataset'] == 'I']