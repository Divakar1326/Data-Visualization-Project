Titanic-Data-Visualization
Overview
This repository contains a Python program designed to analyze and visualize data from the Titanic dataset. The analysis aims to explore the factors influencing survival rates among passengers, utilizing libraries such as Pandas, Seaborn, and Matplotlib for data manipulation and visualization.

Features
Data Cleaning:

Handling missing values for Age, Embarked, and Fare.
Dropping the Cabin column due to excessive missing values.
Exploratory Data Analysis (EDA):

Summary statistics of numerical variables.
Cross-tabulations for various attributes.
Correlation analysis.
Visualizations:

Count plots for survival based on Age, Gender, Passenger Class, and Embarked Port.
Box plots and violin plots to analyze age distribution concerning survival.
Histograms and swarm plots for Fare distribution by survival status.
Pie charts for survival rates segmented by gender and passenger class.
Heatmaps for visualizing correlations among numerical variables.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/Titanic-Data-Visualization.git
Navigate to the project directory:

bash
Copy code
cd Titanic-Data-Visualization
Install the required packages:

bash
Copy code
pip install pandas seaborn matplotlib
Ensure you have the Titanic dataset (Titanic.csv) placed in the project directory.

Usage
Run the program:

bash
Copy code
python your_program_file.py
The program will load the Titanic dataset and perform data cleaning, followed by various analyses and visualizations that will be displayed.

Data Format
Ensure that the Titanic.csv file has the following structure:

PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked
1	0	3	...	male	22	1	0	...	7.25	...	S
2	1	1	...	female	38	1	0	...	71.2833	...	C
...	...	...	...	...	...	...	...	...	...	...	...
Key Insights
Females had significantly higher survival rates compared to males.
First-class passengers had better survival chances than those in lower classes.
Children and younger passengers were more likely to survive.
Passengers who paid higher fares had higher survival chances.
Passengers who embarked at Cherbourg had better odds of survival than those from Southampton.
Contributing
Contributions are welcome! If you have suggestions for improvements or features, feel free to create a pull request or open an issue.

This repository contains a Python program designed to visualize demographic data using bar graphs and histograms. The visualizations are created using the popular libraries Pandas, Matplotlib, and Seaborn. The primary goal is to provide insights into the gender and age distribution of individuals, as well as their occupations, through various graphical representations.

Features
Bar Graphs:

Gender Distribution
Occupation Distribution
Average Age by Occupation
Gender Distribution by Age Group
Histograms:

Age Distribution
Age Distribution by Gender (Overlaid)
Age Distribution with Density Plot (KDE)
Age Group Distribution
