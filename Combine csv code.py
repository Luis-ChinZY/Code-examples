import pandas as pd
import glob

# Change file path here (contains all csv downloaded)
filenames = glob.iglob(r'filepath\*.csv')


all_data = []

for file in filenames:
    df = pd.read_csv(file)
    df.columns.values[2] = "Sales"  
    df.columns.values[3] = "ID"
    all_data.append(df)


df_all = pd.concat(all_data, axis=0) #final data (csv)

# Example data manipulation 
df_all = df_all.drop(['Useless'], axis=1)
df_final = df_all.groupby(['User Name'], as_index= False)['All direct points'].sum()

df_final.to_csv("final-data.csv")