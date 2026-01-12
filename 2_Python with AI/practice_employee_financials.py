print("........Welcome to Employee Financials Insights System........")

# Collect User Input
name = input("Enter Full Name: ")
department = input("Enter Department: ")
experience = int(input("Enter Years of Experience: "))
salary = float(input("Enter Monthly Salary: "))

# Convernt numical values
experience = int(experience)
salary = float(salary)

# Perform Salary Calculations
annual_salary = salary * 12 # Calculate annual salary
tax_rate = 0.20  # Assuming a flat tax rate of 20%
tax_deduction = annual_salary * tax_rate
take_home_salary = annual_salary - tax_deduction # Calculate take-home salary after tax

# Estimate salary growth over the next 5 years based on experience
growth_rate = 0.05  # 5% growth for less than 2 years of experience
year_1 = salary * (1 + growth_rate)
year_2 = year_1 * (1 + growth_rate)
year_3 = year_2 * (1 + growth_rate)
year_4 = year_3 * (1 + growth_rate)
year_5 = year_4 * (1 + growth_rate)

# Calculate potential savings assuming 20% of take-home salary is saved
savings_rate = 0.20
annual_savings = take_home_salary * savings_rate    
total_savings_5_years = annual_savings * 5

# Display collected data
print("\nEmployee Financial Summary for:", name)
print("Department:", department)
print("Years of Experience:", experience)
print("Monthly Salary: ${:.2f}".format(salary))
print("Annual Salary: ${:.2f}".format(annual_salary))
print("Tax Deduction (20%): ${:.2f}".format(tax_deduction))
print("Take-Home Salary after Tax: ${:.2f}".format(take_home_salary))
print("\nEstimated Salary Growth Over Next 5 Years:")
print("Year 1 Salary: ${:.2f}".format(year_1 * 12))
print("Year 2 Salary: ${:.2f}".format(year_2 * 12))
print("Year 3 Salary: ${:.2f}".format(year_3 * 12))
print("Year 4 Salary: ${:.2f}".format(year_4 * 12))
print("Year 5 Salary: ${:.2f}".format(year_5 * 12))
print("\nEstimated Total Savings Over 5 Years: ${:.2f}".format(total_savings_5_years))  
print("........Thank you for using Employee Financials Insights System........")
# End of Employee Financials Insights System in Python
# Employee Financials Insights System Reference:
# 1. Collect user input for employee details such as name, department, years of experience, and monthly salary.
# 2. Perform calculations to determine annual salary, tax deductions, take-home salary, estimated salary growth over the next 5 years, and potential savings.
# 3. Display the collected data and calculated insights in a formatted manner.
# Employee Financials Insights System Examples:
# Example Input:
# Enter Full Name: John Doe
# Enter Department: IT      
# Enter Years of Experience: 3
# Enter Monthly Salary: 5000
# Example Output:
# Employee Financial Summary for: John Doe
# Department: IT
# Years of Experience: 3
# Monthly Salary: $5000.00
# Annual Salary: $60000.00
# Tax Deduction (20%): $12000.00
# Take-Home Salary after Tax: $48000.00 
# Estimated Salary Growth Over Next 5 Years:
# Year 1 Salary: $63000.00
# Year 2 Salary: $66150.00
# Year 3 Salary: $69457.50
# Year 4 Salary: $72930.38
# Year 5 Salary: $76576.90
# Estimated Total Savings Over 5 Years: $48000.00   
# End of Employee Financials Insights System Examples

# Employee Financials Insights System Reference:
# 1. User Input - Collecting data from the user through input prompts.
# 2. Data Conversion - Converting input data to appropriate types (e.g., integer, float) for calculations.
# 3. Salary Calculations - Performing arithmetic operations to calculate annual salary, tax deductions, take-home salary, salary growth, and savings.
# 4. Formatted Output - Displaying results in a user-friendly format using formatted strings.   
# Employee Financials Insights System Types Examples:
# 1. Basic Salary Calculation - Calculating annual salary and tax deductions based on user input.
# 2. Salary Growth Estimation - Estimating future salary based on a fixed growth rate.
# 3. Savings Calculation - Estimating potential savings based on a percentage of take-home salary.
# End of Employee Financials Insights System Types Examples
# Employee Financials Insights System Types Reference:
# 1. Basic Salary Calculation - Involves simple arithmetic operations to calculate annual salary and tax deductions.
# 2. Salary Growth Estimation - Involves applying a growth rate to estimate future salary over multiple years.
# 3. Savings Calculation - Involves calculating a percentage of take-home salary to estimate potential savings.
# End of Employee Financials Insights System Types Reference    
# Functional Programming Methods in Python
from functools import reduce    
# 1. map() - Transforms each item in an iterable using a specified function.
# 2. filter() - Filters items in an iterable based on a specified condition.
# 3. reduce() - Reduces an iterable to a single value by applying a binary function cumulatively.   
# Examples of Functional Programming Methods:
# 1. map() Example
original_list = [10, 20, 30, 40]
doubled = list(map(lambda x: x * 2, original_list))
print("Doubled List using map():", doubled)     # Output: Doubled List using map(): [20, 40, 60, 80]
# 2. filter() Example
greater_than_25 = list(filter(lambda x: x > 25, original_list))
print("Numbers Greater than 25 using filter():", greater_than_25) # Output: Numbers Greater than 25 using filter(): [30, 40]
# 3. reduce() Example
sum_of_list = reduce(lambda x, y: x + y, original_list)
print("Sum of List using reduce():", sum_of_list) # Output: Sum of List using reduce(): 100
# End of Functional Programming Methods Examples in Python
# Functional Programming Methods Types Reference:
# 1. map() - Used for transforming data in an iterable.
# 2. filter() - Used for filtering data in an iterable based on conditions.
# 3. reduce() - Used for aggregating data in an iterable to a single value.
# End of Functional Programming Methods Types Reference 
# End of Employee Financials Insights System in Python  
# Employee Financials Insights System in Python

# Employee Financials Insights System Reference:
# 1. User Input - Collecting data from the user through input prompts.
# 2. Data Conversion - Converting input data to appropriate types (e.g., integer, float) for calculations.
# 3. Salary Calculations - Performing arithmetic operations to calculate annual salary, tax deductions, take-home salary, salary growth, and savings.
# 4. Formatted Output - Displaying results in a user-friendly format using formatted strings.   
# Employee Financials Insights System Types Examples:
# 1. Basic Salary Calculation - Calculating annual salary and tax deductions based on user input.
# 2. Salary Growth Estimation - Estimating future salary based on a fixed growth rate.
# 3. Savings Calculation - Estimating potential savings based on a percentage of take-home salary.
# End of Employee Financials Insights System Types Examples
# Employee Financials Insights System Types Reference:
# 1. Basic Salary Calculation - Involves simple arithmetic operations to calculate annual salary and tax deductions.
# 2. Salary Growth Estimation - Involves applying a growth rate to estimate future salary over multiple years.
# 3. Savings Calculation - Involves calculating a percentage of take-home salary to estimate potential savings.
# End of Employee Financials Insights System Types Reference    
# End of Employee Financials Insights System in Python      

