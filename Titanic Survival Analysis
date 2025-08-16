import warnings
warnings.filterwarnings('ignore')
# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the Titanic dataset
df = pd.read_csv('Titanic.csv')

# Data cleaning
# Fill missing values in Age with median and Embarked with mode
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop Cabin column (too many missing values)
df.drop(columns=['Cabin'], inplace=True)

# Fill missing Fare values with median
df['Fare'].fillna(df['Fare'].median(), inplace=True)

# Exploratory Data Analysis (EDA)

# Display the first few rows of the dataset
print(df.head())

# Check the dimensions of the dataset
print(df.shape)

# Get summary statistics of numerical variables
print(df.describe())

# Check the data types of variables
print(df.dtypes)

# Check for missing values
print(df.isnull().sum())
print(df.groupby(['Sex', 'Survived'])['Survived'].count())

#Let's group the median age by sex, pclass and title, to have any idea and maybe input in Age NAN's
age_group = df.groupby(["Sex","Pclass"])["Age"]

interval = (0, 5, 12, 18, 25, 35, 60, 120)

#same as the other df train
cats = ['babies', 'Children', 'Teen', 'Student', 'Young', 'Adult', 'Senior']

# same that we used above in df train
df["Age_cat"] = pd.cut(df.Age, interval, labels=cats)
#Describe of categorical Age

# Using pd.crosstab to understand the Survived rate by Age Category's
print(pd.crosstab(df.Age_cat, df.Survived))

#printing the variabe that we created by median
print(age_group.median())

# Correlation analysis
correlation = df[['Age', 'Fare']].corr()
print(correlation)

# Cross-tabulation
cross_tab = pd.crosstab(df['Pclass'], df['Survived'])
print(cross_tab)

print(pd.crosstab([df.Sex, df.Survived], [df.SibSp, df.Pclass], margins=True))
print(pd.crosstab([df.Sex, df.Survived], [df.Parch, df.Pclass], margins=True))
numeric_df = df.select_dtypes(include=['float64', 'int64'])
print(numeric_df.corr())

print(pd.crosstab([df.Sex, df.Survived], df.Pclass, margins=True))

#survived by age
print(df.groupby('Survived').describe()['Age'])

#rate of survival by gender
women = df.loc[df.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)
men = df.loc[df.Sex == 'male']["Survived"]
rate_men = sum(men)/len(men)
print("% of men who survived:", rate_men)
print("% of women who survived:", rate_women)

#visualization
#Seting the figure size
plt.figure(figsize=(12,10))

#Plotting the result
#plot1
sns.countplot(x="Age_cat",data=df,hue="Survived", palette="hls")
plt.ylabel("Count", fontsize=18)
plt.xlabel("Age Categorys", fontsize=18)
plt.title("Age Distribution ", fontsize=20)
plt.show()
#plot2
sns.swarmplot(x='Age_cat',y="Fare",data=df,
              hue="Survived", palette="hls", )
plt.ylabel("Fare Distribution", fontsize=18)
plt.xlabel("Age Categorys", fontsize=18)
plt.title("Fare Distribution by Age Categorys ", fontsize=20)
plt.show()

# plot3 Survival by Gender
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Sex', hue='Survived', palette='Set2')
plt.title('Survival by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Survived')
plt.grid(True)
plt.show()

# plot4 Survival by Passenger Class
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Pclass', hue='Survived', palette='Set1')
plt.title('Survival by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.legend(title='Survived')
plt.grid(True)
plt.show()

# plot5 Survival by Age
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Survived', y='Age')
plt.title('Survival by Age')
plt.xlabel('Survived')
plt.ylabel('Age')
plt.grid(True)
plt.show()

# plot6 Fare Distribution by Survival
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Fare', hue='Survived', kde=False, bins=30, palette='viridis')
plt.title('Fare Distribution by Survival')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# plot7 Survival by Embarked Port
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Embarked', hue='Survived', palette='pastel')
plt.title('Survival by Embarked Port')
plt.xlabel('Embarked Port')
plt.ylabel('Count')
plt.legend(title='Survived')
plt.grid(True)
plt.show()

# plot8 Multivariate Analysis: Survival by Class, Gender, and Age
plt.figure(figsize=(8, 6))
sns.catplot(data=df, x='Pclass', hue='Sex', col='Survived', kind='count', height=6, aspect=1)
plt.title('Survival by Class, Gender, and Age')
plt.grid(True)
plt.show()

# plot9 Correlation Heatmap
# Compute and plot correlation matrix
plt.figure(figsize=(8, 6))
corr_matrix = df[['Survived', 'Pclass', 'Age', 'Fare']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# plot10 Age Distribution with KDE Plot
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], kde=True, bins=20, color='blue')
plt.title('Age Distribution with KDE')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# plot11 Bar plot
sns.countplot(x='Survived', data=df)
plt.xlabel('Survival Status')
plt.ylabel('Count')
plt.title('Survival Count')
plt.show()

# plot12 Histogram
plt.hist(df['Age'], bins=10)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Age')
plt.show()

# plot13 Scatter plot
plt.scatter(df['Age'], df['Fare'])
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Age vs. Fare')
plt.show()

# plot14 Box plot
sns.boxplot(x=df['Survived'], y=df['Fare'])
plt.xlabel('Survival Status')
plt.ylabel('Fare')
plt.title('Survival Status vs. Fare')
plt.show()

# plot15 
df.groupby(['Survived','Sex'])['Survived'].count()
df[df['Sex'] == 'male'].Survived.groupby(df.Survived).count().plot(kind='pie', figsize=(6, 6),explode=[0,0.05],autopct='%1.1f%%')
plt.axis('equal')
plt.legend(["Perished","Survived"])
plt.title("Male survival rate")
plt.show()

# PLOT16
df[df['Sex'] == 'female'].Survived.groupby(df.Survived).count().plot(kind='pie',autopct='%1.1f%%',figsize=(6, 6),explode=[0,0.05])
plt.axis('equal')
plt.title("Female survival rate")
plt.legend(["Perished","Survived"])
plt.show()

#plot17
pd.crosstab(df.Pclass, df.Survived, margins=True)
df[df['Pclass'] == 1].Survived.groupby(df.Survived).count().plot(kind='pie', figsize=(6, 6),explode=[0,0.05],autopct='%1.1f%%')
plt.axis('equal')
plt.legend(["Perished","Survived"])
plt.title("First class survival rate")
plt.show()

#plot18
df[df['Pclass'] == 2].Survived.groupby(df.Survived).count().plot(kind='pie', figsize=(6, 6),explode=[0,0.05],autopct='%1.1f%%')
plt.axis('equal')
plt.legend(["Perished","Survived"])
plt.title("Second class survival rate")
plt.show()

#plot19
df[df['Pclass'] == 3].Survived.groupby(df.Survived).count().plot(kind='pie', figsize=(6, 6),explode=[0,0.05],autopct='%1.1f%%')
plt.axis('equal')
plt.legend(["Perished","Survived"])
plt.title("Third class survival rate")
plt.show()

#plot20
print(pd.crosstab([df.Sex, df.Survived], df.Pclass, margins=True))
sns.barplot(x='Pclass',y='Survived',hue='Sex', data=df)
plt.show()
sns.countplot(x='Survived', data=df,hue = 'Embarked')
plt.show()

#plot21
sns.barplot(y = "Fare",x = "Pclass",data = df)
plt.show()

#plot22
sns.swarmplot(x='Survived', y='Fare', data=df)
plt.show()

#plot23
sns.boxplot(y = "Fare",x = "Pclass",data = df[df["Fare"] < 200])
plt.show()

#plot24
sns.barplot(y = "Fare",x = "Pclass",data = df[df["Fare"] < 200])
plt.show()

#plot25
sns.pairplot(df.drop("Name",axis = 1).dropna(),hue = "Survived")
plt.show()

#plot26 binary survival
f,ax=plt.subplots(1,2,figsize=(20,20))
df[df['Survived']==0].Age.plot.hist(ax=ax[0],bins=20,edgecolor='black',color='red')
ax[0].set_title('Survived = 0')
x1=list(range(0,85,5))
ax[0].set_xticks(x1)
df[df['Survived']==1].Age.plot.hist(ax=ax[1],bins=20,edgecolor='black',color='green')
x2=list(range(0,85,5))
ax[1].set_xticks(x2)
ax[1].set_title('Survived = 1')
plt.show()

#plot27 survival with age and survived
f,ax=plt.subplots(1,2,figsize=(18,8))
sns.violinplot(x='Pclass',y='Age',hue='Survived',data=df,split=True,ax=ax[0])
ax[0].set_title('PClass and Age vs Survived')
ax[0].set_yticks(range(0,110,10))
sns.violinplot(x="Sex",y="Age", hue="Survived", data=df,split=True,ax=ax[1])
ax[1].set_title('Sex and Age vs Survived')
ax[1].set_yticks(range(0,110,10))
plt.show()

#plot28
sns.catplot(x='Pclass', y='Survived', hue='Sex', data=df)
plt.show()

#plot29 pclass survivers
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('Pclass: Sruvived vs Dead')
plt.show()

#plot30 survived by sex with age
print(df.groupby(['Sex', 'Survived'])['Survived'].count())
sns.FacetGrid(df, hue="Survived") \
   .map(sns.distplot, "Age") \
   .add_legend()
plt.show()

# Key insights from EDA
print("\nKey Insights:")
print("1. Females had significantly higher survival rates compared to males.")
print("2. First-class passengers had better survival chances than lower classes.")
print("3. Children and younger passengers were more likely to survive.")
print("4. Passengers who paid higher fares had higher survival chances.")
print("5. Passengers who embarked at Cherbourg had better survival odds than those from Southampton.")
