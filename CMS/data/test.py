import pandas as pd 


### big data file ~220mb 
df = pd.read_csv('CMS/MIPS_data/Quality_Payment_Program_Experience_2021.csv')

## clean column names - removing white space and replacing with underscore, and lowercasing
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

## keep only where state or us territory is NY 
df = df[df['practice_state_or_us_territory'] == 'NY']
len(df)



