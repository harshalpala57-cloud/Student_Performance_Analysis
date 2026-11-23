import pandas as pd
df = pd.read_csv("data/students.csv")
print(df)
print("Display First 10 Students from the Datset:")
print(df.head(10))

print("Display Last 10 Students from the Datset:")
print(df.tail(10))

# Information Of Dataset
print(df.info())

# Total Number of Data in Dataset
print(len(df))

# Number of Rows and Columns
print(f'Rows & Columns:{df.shape}')

# Name OF Each Columns
print(f'Column Names:{df.columns}')

# Selecting Columns
subset = df[["student_id", "name", "age"]]
print(subset)

# Filtering Rows 
Maths_Score = df[df['maths']>85][['student_id','name','gender','maths']]
print('Marks in Maths Greater than 85')
print(Maths_Score)
print('Total Number of Student In Maths Scoring Marks Greater Then 85:',len(Maths_Score))

Age = df[df['age']<21][['student_id','name','age','gender']]
print('\nStudent with Age Less Then 21')
print(Age)
print('Total Number of Students with Age Less Then 21 is',len(Age))

# Is Null
print(df.isnull().sum())

# # Duplicate Values
print('Duplicate Values',df.duplicated().sum())

# Data Cleaning
clean_df = df.copy() # clean_df is variable name and .copy is for copying original datase for cleaning

print('\nDuplicates before cleaning')
print(clean_df.duplicated().sum()) #.sum() counts how many duplicate rows exists

clean_df = clean_df.drop_duplicates() # This will remobve the duplicate rows if exists

print('\n Missing Values before Cleaning:')
print(clean_df.isnull().sum())

# Coverting Marks into Numeric 
subjects=['maths','science','english','computer'] # Creating the List for subjects 

for subject in subjects: # USing For Loop
    clean_df[subject] = pd.to_numeric(  
    clean_df[subject],errors="coerce"
    ) # converting values in a column into  umeric values and "coerce" continues the For loop 
      # without error for values that cannot be converted and NaN is replaced

# Identifying invalid marks
for subject in subjects:
    clean_df.loc[
    (clean_df[subject]<0) | (clean_df[subject]>100),
     subject
     ]=pd.NA  
    
# Average Marks
clean_df["Average_Marks"] = clean_df[subjects].mean(axis=1)
print(clean_df)

clean_df.to_csv("data/cleaned_students.csv", index=False)

print("Cleaned dataset saved successfully!")

# Statistical Analysis
print(clean_df[subjects].describe())

print('\n Mean Marks')
print(clean_df[subjects].mean())

print('\n Median marks')
print(clean_df[subjects].median())

print('\n Mode marks')
print(clean_df[subjects].mode().iloc[0])

print('\n Standard Deviation')
print(clean_df[subjects].std())

Sorted_Dataset = clean_df[['student_id','name','gender','Average_Marks']].sort_values(
    by="Average_Marks",
    ascending=False
)
print(Sorted_Dataset)

Top_10_Students = Sorted_Dataset.head(10)
print(Top_10_Students)

Top_10_Students = Top_10_Students.copy()  

Top_10_Students["Rank"]=(
    Top_10_Students["Average_Marks"].rank(method="min",ascending=False)
    .astype(int)
)

print(Top_10_Students)

Top_10_Students.to_csv("data/Top_10_Students.csv", index=False)

print("Cleaned dataset saved successfully!")
