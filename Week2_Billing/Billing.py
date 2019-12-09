# Name:                 Rojan Khatri
# Course:               DSC 510
# Assignment:           2.1
# Purpose/Description:  This is a program to calculates the total cost for fiber optic installation.
####################################################################################################

greeting_message = "Welcome to Installation Cost Calculation."  # initializing greeting message
company_name = input("Enter the name of your company: ")  # Getting company name from user
fiberoptic_length = float(
    input("Enter desired length of fiber optic cable (in feet): "))  # Getting length from user and converting input to float
cost_per_feet = 0.87  # initializing cost per feet

total_cost = fiberoptic_length * cost_per_feet  # Total cost calculation


print("\n\n########################################################\n\n"
      " ********* Invoice for {} *********\n\n"
      " Total Length: {} feet\n"
      " Cost per feet: ${}\n\n"
      " Total installation cost: ${:,.2f}\n\n"
      "########################################################"
      .format(company_name, fiberoptic_length, cost_per_feet, total_cost))
