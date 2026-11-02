import pandas as pd

# Load student data
df = pd.read_csv("data/student_data.csv")

# Display the first rows
print("Student Data:")
print(df.head())

# Display basic information
print("\nDataset Information:")
print(df.info())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())
# Calculate the average final score
average_score = df["Final_Score"].mean()

print("\nAverage Final Score:")
print(average_score)
# Find the highest and lowest final scores
highest_score = df["Final_Score"].max()
lowest_score = df["Final_Score"].min()

print("\nHighest Final Score:")
print(highest_score)

print("\nLowest Final Score:")
print(lowest_score)
# Calculate correlation between study hours and final scores
correlation = df["Study_Hours"].corr(df["Final_Score"])

print("\nCorrelation between Study Hours and Final Score:")
print(correlation)
import matplotlib.pyplot as plt

# Create a scatter plot
plt.scatter(df["Study_Hours"], df["Final_Score"])

# Add labels and title
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Study Hours vs Final Score")

# Display the plot
plt.savefig("images/study_hours_vs_score.png")
print("Graphique enregistré avec succès !")
plt.show()
# Calculate correlation between attendance and final scores
attendance_correlation = df["Attendance"].corr(df["Final_Score"])

print("\nCorrelation between Attendance and Final Score:")
print(attendance_correlation)
# Attendance vs Final Score
plt.figure()
plt.scatter(df["Attendance"], df["Final_Score"])
plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.title("Attendance vs Final Score")
plt.savefig("images/attendance_vs_score.png")

print("Deuxième graphique enregistré avec succès !")
