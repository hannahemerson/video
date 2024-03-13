import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

#df = pd.read_csv("ar.csv")

income= float(input("What is your total income?: "))
goal = int(input("Enter the amount you'd like to save: "))
save = int(input("Enter how much you will save per week: "))

prediction = goal/save
print ("It will take you " , prediction , "weeks to save your goal! Good luck")

print ("-----------------------")
#What if question1
print ("What if question 1")
# Question 1 is what if the user doubles what they save per week. How long would it take to save then?
print ("Question = What if the user doubles the amount they save? How long would it take to save then?")

double = save * 2
double_prediction = goal/double
print ("It would take you " , double_prediction , "weeks to save your goal! Good luck")

print ("-----------------------")
#What if question2
print ("What if question 2")
# Question 2 is what if the user halves what they save per week. How long would it take to save then?
print ("Question = What if the user halves the amount they save? How long would it take to save then?")

half = save / 2
half_prediction = goal/half
print ("It would take you " , half_prediction , "weeks to save your goal! Good luck")

print ("-----------------------")
#What if question3
print ("What if question 3")
#What if I increase my weekly savings by 10%? How long would it take to save then?

print("What if question 3 = What if I increase my weekly savings by 10%? How long would it take to save then?")
increase = (save / 100) * 110
increase_prediction = goal/increase
print ("It would take you " , increase_prediction , "weeks to save your goal! Good luck")

# User can view data and results in a graphical format which displays information such as their progress
# using the system or the results of a ‘what if’ scenario.
# Data: names of the variables and their values for the chart
variable_names = ['Time if saving x2 ', 'Time if saving / 2','Time is saving + 10%']
values = [double_prediction, half_prediction,increase_prediction]

# Creating the bar chart
plt.bar(variable_names, values)

# Show the plot
plt.show()
 
