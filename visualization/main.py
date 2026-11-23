import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os # Allows us to manage folders and files
os.makedirs("visualization",exist_ok=True)
clean_df=pd.read_csv("data/cleaned_students.csv")

subjects=['maths','science','english','computer']
subject_avg=clean_df[subjects].mean()
print(subject_avg)

plt.style.use("dark_background")
colors=["Blue","Pink","Yellow","Orange"]
plt.title("Average marks By Subjects")
plt.bar(subjects,subject_avg,color=colors)
plt.savefig("visualization/Subject_average_Marks.png")
plt.show()


colors=[]
subject_average=clean_df[subjects].mean(axis=1)
for marks in subject_average:
    if marks >=80:
        colors.append("green")
    elif marks >=50:
        colors.append("Orange")
    else:
        colors.append("red")    
plt.title("Average Marks By Each Students")
plt.bar(clean_df["student_id"],subject_average,color=colors)
plt.savefig("visualization/Studend_id_Sub_Avg.png")
plt.show()

# Grade Distribution
def assign_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >=70:
        return"B"
    elif marks >=60:
        return"C"
    elif marks >=35:
        return"D"
    else:
        return"F"

clean_df["Grade"]=clean_df["Average_Marks"].apply(assign_grade)
print(clean_df)

grade_counts=clean_df["Grade"].value_counts().reindex(
    ["A","B","C","D","F"],fill_value=0
)
colour = ["Pink", "Green", "Red", "Yellow", "Blue"]
plt.pie(grade_counts.values,labels=grade_counts.index,colors=colour,autopct="%1.1f%%")
plt.title("Student Grade Distribution")
plt.savefig("visualization/Student_Grade_Distribution.png")
plt.show()

if "gender" in clean_df.columns:
 gender_avg=clean_df.groupby("gender")[subjects].mean()
 print(gender_avg)

gender_avg.T.plot(
 kind="bar",
 color=["Purple","Orange"]
) 
plt.title("Genderwise_Subject_Performance")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.legend(title="gender")
plt.savefig("visualization/Genderwise_Subject_Performance.png")
plt.show()

sns.histplot(
 clean_df["Average_Marks"],
 bins=10,
 color="Maroon",
 edgecolor="Black",
 kde=True
)
plt.title("Distribution of Subject Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.savefig("visualization/Distri_sub_avg_Marks")
plt.show()
