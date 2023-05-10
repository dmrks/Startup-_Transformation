# Startup-_Transformation

Startup Transformation
In this project, you’ll work as a data analyst for a tech startup that is looking to improve its operations after a global pandemic has taken the world by storm.

You will apply data transformation techniques to make better sense of the company’s data and help answer important questions such as:

Is the company in good financial health?
Does the company need to let go of any employees?
Should the company allow employees to work from home permanently?
Let’s get started!


Analyzing Revenue and Expenses
1.
The management team of the company you work for is concerned about the status of the company after a global pandemic.

The CFO (Chief Financial Officer) asks you to perform some data analysis on the past six months of the company’s financial data, which has been loaded in the variable financial_data.

First, examine the first few rows of the data using print() and .head().



2.
Notice that financial_data has three columns – Month, Revenue, and Expenses.

Store each column in three separate variables called month, revenue, and expenses.



3.
Next, use the following code to create a plot of revenue over the past six months:

plt.plot(month,revenue)
plt.show()

4.
On the right, you should now see a plot of revenue over time. You can label and format the figure using the following functions:

plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
These should be added before plt.show(). Add the labels to your plot.

5.
Repeat steps 3 and 4 for monthly expenses. In other words, create a second plot of monthly expenses over the past 6 months. Note that you’ll need to use the function plot.clf() prior to creating this new plot. Otherwise, it will be plotted on-top of the revenue plot. The code should look something like this:

plt.clf()
#insert code to create plot here
#add labels to the plot here
plt.show()
How are monthly expenses changing over time?



6.
As shown, revenue seems to be quickly decreasing while expenses are increasing. If the current trend continues, expenses will soon surpass revenues, putting the company at risk.

After you show this chart to the management team, they are alarmed. They conclude that expenses must be cut immediately and give you a new file to analyze called expenses.csv.

Use pandas to read in expenses.csv and store it in a variable called expense_overview.

Print the first seven rows of the data.



Pie Chart and Collapsing Categories
7.
Notice that there are two columns:

Expense: indicates the expense category
Proportion: indicates how much of the overall expenses a specific category takes up
Store the Expense column in a variable called expense_categories and the Proportion column in a variable called proportions.



8.
Next, we want to create a pie chart of the different expense categories. Use plt.clf() again to clear the previous plot, then create a pie chart using the plt.pie() method, passing in two arguments:

proportions
labels = expense_categories
Give your pie chart a title using plt.title(), then use plt.show() at the end to show the plot.



9.
Notice that the pie chart currently looks deformed.

Above plt.show(), add in the following two lines of code to set the axis and adjust the spacing:

plt.axis('Equal')
plt.tight_layout()
Take a moment to look at the pie chart. Which expense categories make up most of the data, and which ones aren’t so significant?



10.
It seems that Salaries, Advertising, and Office Rent make up most of the expenses, while the rest of the categories make up a small percentage.

Before you hand this pie chart back to management, you would like to update the pie chart so that all categories making up less than 5% of the overall expenses (Equipment, Utilities, Supplies, and Food) are collapsed into an “Other” category.

Update the pie chart accordingly.



11.
You should now see four categories in your updated pie chart:

Salaries
Advertising
Office Rent
Other
This simplified pie chart helps the management team see a big picture view of the company’s expenses without getting distracted by noisy data.

If the company wants to cut costs in a big way, which category do you think they should focus on? Put your answer in a string variable called expense_cut.



Employee Productivity
12.
Salaries make up 62% of expenses. The management team determines that to cut costs in a meaningful way, they must let go of some employees.

Each employee at the company is assigned a productivity score based on their work. The management would like to keep the most highly productive employees and let go of the least productive employees.

First, use pandas to load in employees.csv and store it in a variable called employees.

Print the first few rows of the data.



13.
Notice that there is a Productivity column, which indicates the productivity score assigned to that employee.

Sort the employees data frame (in ascending order) by the Productivity column and store the result in a variable called sorted_productivity.





14.
You should now see the employees with the lowest productivity scores at the top of the data frame.

The company decides to let go of the 100 least productive employees.

Store the first 100 rows of sorted_productivity in a new variable called employees_cut and print out the result.

Unfortunately, this batch of employees won’t be so lucky.



15.
Your colleague Sarah, a data scientist at the company, would like to explore the relationship between Income and Productivity more in depth, but she points out that these two features are on vastly different scales.

For example, productivity is a feature that ranges from 0-100, but income is measured in the thousands of dollars.

Moreover, there are outliers in the data that add an additional layer of complexity.

She asks you for advice on how she should transform the data. Should she perform normalization, standardization, log transformation, or something else?

Put your answer in a string in a variable called transformation.


Commute Times and Log Transformation
16.
The COO (Chief Operating Officer) is debating whether to allow employees to continue to work from home post-pandemic.

He first wants to take a look at roughly how long the average commute time is for employees at the company. He asks for your help to analyze this data.

The employees data frame has a column called Commute Time that stores the commute time (in minutes) for each employee.

Create a variable called commute_times that stores the Commute Time column.



17.
Let’s do some quick analysis on the commute times of employees.


What are the average and median commute times? Might it be worth it for the company to explore allowing remote work indefinitely so employees can save time during the day?



18.
Let’s explore the shape of the commute time data using a histogram.

First, use plt.clf() to clear the previous plots. Then use plt.hist() to plot the histogram of commute_times. Finally, use plt.show() to show the plot. Feel free to add labels above plt.show() if you would like to practice!

What do you notice about the shape of the data? Is it symmetric, left skewed, or right skewed?


19.
The data seems to be skewed to the right. To make it more symmetrical, we might try applying a log transformation.

Right under the commute_times variable, create a variable called commute_times_log that stores a log-transformed version of commute_times.




20.
Replace the histogram for commute_times with one for commute_times_log.

Notice how the shape of the data changes from being right skewed to a more symmetrical (and even slightly left-skewed) in shape. After applying log transformation, the transformed data is more “normal” than before.
