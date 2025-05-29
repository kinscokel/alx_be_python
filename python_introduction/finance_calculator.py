# variables
monthly_income = int(input("Enter your monthly income:"))
total_monthly_expenses = int(input("Enter your total monthly expenses:"))

# calculate monthly_savings
monthly_savings = monthly_income - total_monthly_expenses

# calculate one_year_savings
one_year_savings = monthly_savings * 12


# calculate projected_annual_savings_of one_year_with_interest
(projected_savings := monthly_savings * 12 + (monthly_savings * 12 * 0.05))

# Display the result
print("monthly savings are $", monthly_savings)
print("projected savings after one year, with interest, is: $", projected_savings)