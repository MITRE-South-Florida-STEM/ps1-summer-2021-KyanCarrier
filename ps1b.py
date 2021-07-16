#PS1B.PY
#Get the inputs

print ("Enter your annual salary:")
annual_salary = float(input())
print ("Enter the percent of your salary to save, as a decimal:")
portion_saved = float(input())
print ("Enter the cost of your dream home:")
total_cost = float(input())
print ("Enter the semi-annual raise, as a decimal:")
semi_annual_raise = float(input())
#Setup some variables
portion_down_payment = 0.25
current_savings = 0
#This is the annual interest rate
r = 0.04
num_months = 0
down_payment_needed = total_cost*portion_down_payment
monthly_contribution = (annual_salary*portion_saved)/12

#print("num_month mod 6", num_months&6)

#Loop while you don't have enough money
while(current_savings < down_payment_needed):
 current_savings += monthly_contribution 
 current_savings += (current_savings*r/12)  
 num_months += 1
#When number of months % 6 == 0 then time for a raise
 if ((num_months % 6) == 0):  
    annual_salary += (annual_salary*semi_annual_raise)
    monthly_contribution = (annual_salary*portion_saved)/12
print("Number of months: ", num_months)