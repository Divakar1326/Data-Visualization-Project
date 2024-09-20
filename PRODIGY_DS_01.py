import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('C:/Users/diva1/OneDrive/Documents/u.csv')
# Create figure for bar graphs
fig, axes = plt.subplots(2, 2, figsize=(16, 12))  # 2x2 grid of bar charts
fig.suptitle('Bar Graphs', fontsize=16)
# Bar Graph 1: Gender Distribution
gender_counts = df['gender'].value_counts()
gender_counts.plot(kind='bar', color=['blue', 'pink'], ax=axes[0, 0])
axes[0, 0].set_xlabel('Gender')
axes[0, 0].set_ylabel('Count')
axes[0, 0].set_title('Gender Distribution')
axes[0, 0].grid(axis='y')
# Bar Graph 2: Occupation Distribution
occupation_counts = df['occupation'].value_counts()
occupation_counts.plot(kind='bar', color='teal', ax=axes[0, 1])
axes[0, 1].set_xlabel('Occupation')
axes[0, 1].set_ylabel('Count')
axes[0, 1].set_title('Occupation Distribution')
axes[0, 1].tick_params(axis='x', rotation=90)
axes[0, 1].grid(axis='y')
# Bar Graph 3: Average Age by Occupation
avg_age_by_occupation = df.groupby('occupation')['age'].mean()
avg_age_by_occupation.plot(kind='bar', color='coral', ax=axes[1, 0])
axes[1, 0].set_xlabel('Occupation')
axes[1, 0].set_ylabel('Average Age')
axes[1, 0].set_title('Average Age by Occupation')
axes[1, 0].tick_params(axis='x', rotation=90)
axes[1, 0].grid(axis='y')
# Bar Graph 4: Gender Distribution by Age Group
bins = [0, 18, 30, 40, 50, 60, 100]
labels = ['0-18', '19-30', '31-40', '41-50', '51-60', '60+']
df['AgeGroup'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
age_gender_counts = df.groupby(['AgeGroup', 'gender']).size().unstack()
age_gender_counts.plot(kind='bar', stacked=True, color=['blue', 'pink'], ax=axes[1, 1])
axes[1, 1].set_xlabel('Age Group')
axes[1, 1].set_ylabel('Count')
axes[1, 1].set_title('Gender Distribution by Age Group')
axes[1, 1].tick_params(axis='x', rotation=0)
axes[1, 1].grid(axis='y')
# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Leave space for the suptitle
plt.show()
# Create figure for histograms
fig, axes = plt.subplots(2, 2, figsize=(16, 12))  # 2x2 grid of histograms
fig.suptitle('Histograms', fontsize=16)
# Histogram 1: Age Distribution
axes[0, 0].hist(df['age'], bins=15, edgecolor='black', color='skyblue')
axes[0, 0].set_xlabel('Age')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].set_title('Age Distribution')
axes[0, 0].grid(True)
# Histogram 2: Age Distribution by Gender (Overlaid)
for gender in df['gender'].unique():
    subset = df[df['gender'] == gender]
    axes[0, 1].hist(subset['age'], bins=15, alpha=0.5, label=gender, edgecolor='black')
axes[0, 1].set_xlabel('Age')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].set_title('Age Distribution by Gender')
axes[0, 1].legend(title='Gender')
axes[0, 1].grid(True)
# Histogram 3: Age Distribution with KDE
sns.histplot(df['age'], kde=True, bins=15, color='blue', ax=axes[1, 0])
axes[1, 0].set_xlabel('Age')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].set_title('Age Distribution with Density Plot')
axes[1, 0].grid(True)
# Histogram 4: Age Group Distribution
df['AgeGroup'].value_counts(sort=False).plot(kind='bar', ax=axes[1, 1], color='purple', edgecolor='black')
axes[1, 1].set_xlabel('Age Group')
axes[1, 1].set_ylabel('Count')
axes[1, 1].set_title('Age Group Distribution')
axes[1, 1].grid(True)   
# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
