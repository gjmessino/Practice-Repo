import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

top_speeds = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86, 100, 105, 84, 105, 90, 99, 90, 95,
              94, 100, 79, 112, 91, 80, 85]
ages = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6, 2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12]

plt.scatter(top_speeds, ages) #create the scatter plot
plt.xlabel('Top speeds (mph)') #create the horizontal axis label
plt.ylabel('Age (years)') #create the vertical axis label
plt.title('Age vs top speeds of cars') #create the title
plt.show() #show the plot

number_of_people = [54, 84, 41, 19, 12] #y values
mode_of_transport = ['Bus', 'Subway', 'Car', 'Walking', 'Biking'] #x values
plt.bar(mode_of_transport, number_of_people) #create the bar chart
plt.title('Customer survey results') #title
plt.xlabel('Mode of transport') #x label
plt.ylabel('Number of people') #y label
plt.show() #show the graph

data = {
    "SUV Price (USD)": [64000, 66000, 68000, 72000, 74000],
    "SUV Units Sold": [2100, 2230, 2100, 1900, 2500],
    "Sedan Price (USD)": [54000, 57000, 60000, 62000, 63000],
    "Sedan Units Sold": [5600, 5700, 5600, 5200, 6200],
    "Pickup Price (USD)": [39000, 42000, 38000, 45000, 46000],
    "Pickup Units Sold": [4200, 4400, 4800, 5200, 5500],
    "Break-Even Point (000,000 USD)": [600, 650, 750, 800, 900]
}
df = pd.DataFrame(data, index = ["2018", "2019", "2020", "2021", "2022"])
df

break_even = df['Break-Even Point (000,000 USD)'] * 1000000 #column name goes in square brackets
years = ['2018', '2019', '2020', '2021', '2022'] #years go on the horizontal axis

rev_suv = df['SUV Price (USD)'] * df['SUV Units Sold'] #revenues for SUV
rev_sedan = df['Sedan Price (USD)'] * df['Sedan Units Sold'] #revenues for sedan
rev_pickup = df['Pickup Price (USD)'] * df['Pickup Units Sold'] #revenues for pickup
rev_total = rev_suv + rev_sedan + rev_pickup #calculate total revenue

plt.plot(years, break_even, marker='o') #line chart. break even points on vertical axis, years on horizontal axis
plt.plot(years, rev_total, marker='o') #revenue points on vertical axis, years on horizontal axis
plt.xlabel('Years') #horizontal label
plt.ylabel('USD') #vertical label
plt.title('Total Revenue and Break-Even Amounts from 2018 to 2022') #title
plt.legend(['Break-Even Points', 'Total Revenue']) #legend
plt.show()

number_employees = [2431, 1987, 2231, 2732, 2900] #vertical axis
years = ['2018', '2019', '2020', '2021', '2022'] #horizontal axis

plt.plot(years, number_employees, marker = "o")
plt.ylabel("Number of Employees")
plt.xlabel("Years")
plt.title("Number of Employees over 5 Years")
plt.show()

revenue = [23, 56, 12, 98, 141, 431, 298, 255, 42, 67]
employees = [1988, 2013, 652, 3002, 5421, 7341, 6098, 6721, 4533, 6211]

plt.scatter(revenue, employees)
plt.xlabel("Revenue in Billions")
plt.ylabel("Number of Employees")
plt.title("Revenue vs Employee Number")
plt.show()

def temp_convert(F):
  C = (F - 32) * 5/9
  return C

C_values = temp_convert(F_values)
plt.plot(F_values,C_values)
plt.xlabel("Degrees Fahrenheit")
plt.ylabel("Degrees Celsius")
plt.title("Tempurature Conversion")
plt.show()

x = np.linspace(0, 100)
c = 2**(x/10)
plt.plot(x,c)
plt.xlabel("Days Gone By")
plt.ylabel("Number of Cases")
plt.title("Flu Cases by Day")
plt.show()

heights = np.random.randint(190, 230, 100) #creating an array of 100 random numbers between 190 and 230 cm

plt.hist(heights)
plt.xlabel("Heights(cm)")
plt.ylabel("Frequency")
plt.title("Basketball Player Heights")
plt.show()