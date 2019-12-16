# Name:                 Rojan Khatri
# Course:               DSC 510
# Assignment:           3.1
# Date:                 12/14/2019
# Purpose/Description:  This is a program to calculates the total cost for fiber optic installation based on user input.

# Applies bulk discount.
####################################################################################################

greeting_message = "Welcome to Installation Cost Calculation."  # initializing greeting message
discount_message = "" # initializing discount message

company_name = input("Enter the name of your company: ")  # Getting company name from user
desired_length = float(
    input(
        "Enter desired length of fiber optic cable (in ft): "))  # Getting length from user and converting input to float

# installation rate based length. Bulk discount applies.
if desired_length > 500:
    rate_per_feet = .50

elif desired_length > 250:
    rate_per_feet = .70

elif desired_length > 100:
    rate_per_feet = .80

else:
    rate_per_feet = .87

# Total installation cost calculation
installation_cost = desired_length * rate_per_feet

# Setting discount message for bulk discount
if desired_length > 100:
    discount_message = '(Applies Bulk Discount)'

# Generating  receipt for the customer

print("\n\n########################################################\n\n"
      " ********* Installation Receipt for {} *********\n\n"
      " Total Length: {} feet\n"
      " Cost per feet: ${} {}\n\n"
      " Total Installation cost: ${:,.2f}\n\n"
      "########################################################"
      .format(company_name, desired_length, rate_per_feet, discount_message, installation_cost))
