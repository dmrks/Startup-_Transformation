import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')

# 1
print(financial_data.head())

#2
month = financial_data.Month
revenue = financial_data.Revenue
expenses = financial_data.Expenses

#3+4
plt.plot(month,revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.show()
plt.clf()

#5
plt.plot(month,expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')
plt.show()
plt.clf()

#6
expense_overview = pd.read_csv("expenses.csv")
print(expense_overview.head())

#7
expense_categories = expense_overview.Expense
proportions =expense_overview.Proportion

#8+9+10
expense_categories = ["Salaries","Advertising","Office Rent","Other"]
proportions =[0.62,0.15,0.15,0.08]
plt.pie(proportions,labels = expense_categories)
plt.title('Expense Categories')
plt.axis('Equal')
plt.tight_layout()
plt.show()
plt.clf()

#11
expense_cut = "Salaries"

#12
employees = pd.read_csv('employees.csv')
print(employees.head())

#13
sorted_productivity = employees.sort_values(by=["Productivity"])
#print(sorted_productivity.head())

#13
employees_cut = sorted_productivity[0:100]
#print(employees_cut)

#15 Because of the Outlier, she should use Standardization
transformation = "standardization"

#16
commute_times = employees["Commute Time"]

#17 What are the average and median commute times? = mean	33.4417, Median = 31.060000000000002
print(commute_times.describe())

#18 Shape = Right-Skewed
plt.clf()
plt.hist(commute_times)
plt.xlabel('Amount of Time')
plt.ylabel('Frequency')
plt.title('Commute Times')
plt.show()
plt.clf()

#19 Shape = Right-Skewed

commute_times_log = np.log(commute_times)
plt.hist(commute_times_log)
plt.xlabel('Amount of Time')
plt.ylabel('Frequency')
plt.title('Commute Times')
plt.show()
plt.clf()

