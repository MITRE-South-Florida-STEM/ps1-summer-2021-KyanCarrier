#PS1A.PY
#Obtain the inputs needed
print ("Enter your annual salary:")
annual_salary = float(input())
print ("Enter the percent of your salary to save, as a decimal:")
portion_saved = float(input())
print ("Enter the cost of your dream home:")
total_cost = float(input())
#Initialize some variables
portion_down_payment = 0.25
current_savings = 0
r = 0.04
num_months = 0
down_payment_needed = total_cost*portion_down_payment
monthly_contribution = (annual_salary*portion_saved)/12 
#Loop until enough money is saved
while(current_savings < down_payment_needed):
  current_savings += monthly_contribution
  current_savings += (current_savings*r/12)
  num_months += 1
print("Number of months: ", num_months)

#For some reason I am getting 182 months while the test results are saying 183 on the .PDF