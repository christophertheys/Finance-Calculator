# Compulsory Task 1
import math

# This program will allow the user to make use of two financial calculators, an investment or a home loan repayment
# calculator.

# The user will first have to choose between the investment or bond repayment option

print("Welcome to 'Amaze Financial Calculator !' \n"
      "\n"
      "The calculator which is able to forecast and assist you in making the correct financial decision \n   "
      "Choose between 'investment' or 'bond' from the menu below to proceed \n"
      "\n"
      "Type in 'investment' or 'bond' to make your selection \n "
      "\n"
      " Investment    - Used to calculate the amount of interest you'll earn on investment \n"
      " Bond          - Used to calculate the capital portion and interest portion on your home loan \n ")

user_selection_option = input("Type in the option which you would like to make use of: ")

# The user will input the selection of their choice alongside their relevant information

if len(user_selection_option) == 10:

    print("You have selected investment calculator", "\n")

    amount_of_funds_for_user = float(input("Enter the amount of money that you would like to deposit :"))
    interest_rate_for_user = float(input("Enter the interest rate that will be applicable (as a percentage) :"))
    number_of_years_for_user = float(input("Enter the number of years that you plan to invest your funds for :"))
    simple_interest_formula = amount_of_funds_for_user * (1 + (interest_rate_for_user / 100) * number_of_years_for_user)
    compound_interest_formula = amount_of_funds_for_user * math.pow(1 + interest_rate_for_user / 100,
                                                                    number_of_years_for_user)
    print("\n")

    # I've made another condition applicable where the user has to input their choice between simple or compound
    # interest
    #  to get to their final future value.

    # If the user does not enter the correct key word then the program will prompt them to try again.

    interest = input("Input which type of rate will be applicable. 'Simple' or 'Compound' interest :")

    if len(interest) == 6:
        print("You have selected a 'Simple Interest' rate calculation ", "\n")
        print("The future value of your investment, based on the initial amount of funds deposited of R{} \n"
              "Is equal to R{} in {} years time".format(amount_of_funds_for_user, simple_interest_formula,
                                                        number_of_years_for_user))

    elif len(interest) == 8:
        print("You have selected a 'Compound Interest' rate calculation ", "\n")
        print("The future value of your investment, based on the initial amount of funds deposited of R{} \n"
              "Is equal to R{} in {} years time".format(amount_of_funds_for_user, compound_interest_formula,
                                                        number_of_years_for_user))
    else:
        print("Invalid Entry, please try again!")

# The second option available to the user was a bond repayment calculation

elif len(user_selection_option) == 4:

    print("You have selected the bond calculation ", "\n")

    present_value_of_home = float(input("Please enter the present value of your home :"))
    bond_interest_rate = float(input("Please enter the applicable interest rate (as a percentage) :")) / 100
    months_for_bond = float(input("Please enter the number of months that you plan to take to repay the bond"))
    bond_repayment_formula = (bond_interest_rate / 12) * present_value_of_home / (1 - (1 + bond_interest_rate)
                                                                                  ** (-1 * months_for_bond))
    print("\n")

    print("Based on the present value of your home of R{} \n The monthly repayments applicable will "
          "equal to R{}, payable per month".format(present_value_of_home, bond_repayment_formula))

else:
    print("Unfortunately that's an invalid input... \n Please type in 'Investment' or 'Bond' to make your selection "
          "and proceed further \n \n The road to your financial freedom is one-click away !")
