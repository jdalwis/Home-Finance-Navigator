def main():
    opt = True

    while opt:
        print("=" * 50)
        print("Welcome to the Housing Information Program")
        print("=" * 50)
        print("1. Calculate max monthly housing spend")
        print("2. Total down payment estimator")
        print("3. Find current property tax by state")
        print("4. Compare Interest Rates over set amount of time")
        print("5. Exit")
        print("=" * 50, "\n")
        option = str(input("Please select an option: "))

        if option == "1":
            income = int(input("Enter your monthly income: "))
            monthlySpend = income * 0.3
            print("It is recommended that your monthly spend on housing should be no greater than $", monthlySpend,
                  "\n")
        elif option == "2":
            housePrice = int(input("Enter the house price: "))
            status = str(input("Are you a first time homebuyer? (Yes/No) "))
            if status == "Yes":
                totalDownPayment = 0.08 * housePrice
                print("Your down payment will be approximately", totalDownPayment, "\n")
            elif status == "No":
                totalDownPayment = 0.19 * housePrice
                print("Your down payment will be approximately", totalDownPayment, "\n")
            else:
                print("Invalid!")
                print("Please enter Yes or No")
                return
        elif option == "3":
            # Assuming tax rates are provided in a list as before
            tax_rates = [0.0032, 0.004, 0.0055, 0.0056, 0.0056, 0.0057, 0.0057, 0.0057, 0.0059, 0.0061, 0.0062, 0.0063,
                         0.0064, 0.0067, 0.0067, 0.0067, 0.0067, 0.0074, 0.0075, 0.0082, 0.0083, 0.0084, 0.0087, 0.0087,
                         0.0089, 0.0091, 0.0092, 0.0093, 0.0098, 0.0101, 0.0104, 0.0105, 0.0111, 0.0114, 0.0117, 0.0124,
                         0.0134, 0.0138, 0.0140, 0.0140, 0.0149, 0.0152, 0.0159, 0.0161, 0.0163, 0.0168, 0.0179, 0.0183,
                         0.0193, 0.0208, 0.0223]

            state_to_tax_index = {
                "Hawaii": 0,
                "Alabama": 1,
                "Colorado": 2,
                "Wyoming": 3,
                "Louisiana": 4,
                "South Carolina": 5,
                "West Virginia": 6,
                "Utah": 7,
                "Nevada": 8,
                "Delaware": 9,
                "District of Columbia": 10,
                "Arizona": 11,
                "Arkansas": 12,
                "Idaho": 13,
                "Tennessee": 14,
                "Mississippi": 15,
                "New Mexico": 16,
                "Montana": 17,
                "California": 18,
                "North Carolina": 19,
                "Kentucky": 20,
                "Indiana": 21,
                "Washington": 22,
                "Virginia": 23,
                "Oklahoma": 24,
                "Florida": 25,
                "Georgia": 26,
                "Oregon": 27,
                "North Dakota": 28,
                "Missouri": 29,
                "Alaska": 30,
                "Maryland": 31,
                "Minnesota": 32,
                "Massachusetts": 33,
                "South Dakota": 34,
                "Maine": 35,
                "Kansas": 36,
                "Michigan": 37,
                "Rhode Island": 38,
                "New York": 39,
                "Pennsylvania": 40,
                "Iowa": 41,
                "Ohio": 42,
                "Wisconsin": 43,
                "Nebraska": 44,
                "Texas": 45,
                "Connecticut": 46,
                "Vermont": 47,
                "New Hampshire": 48,
                "Illinois": 49,
                "New Jersey": 50
            }

            state = input("Enter the state: ")
            house_price = int(input("Enter the house price: "))

            if state in state_to_tax_index:
                tax_rate = tax_rates[state_to_tax_index[state]]
                property_tax = house_price * tax_rate
                print(f"Your yearly property tax in {state} will be approximately: ${property_tax:.2f}","\n")
            else:
                print("Tax rate for this state is not defined.")
        elif option == "4":
            e = 2.718281828459045
            principle = int(input("Enter the principle: "))
            interestRate1 = float(input("Enter the first interest rate: "))
            interestRate2 = float(input("Enter the second interest rate: "))
            timeSpan = int(input("Enter the length of time in years: "))
            r1 = interestRate1 / 100
            r2 = interestRate2 / 100
            t = timeSpan
            if interestRate1 > interestRate2:
                varInter1 = principle * (e ** (r1 * t))
                varInter2 = principle * (e ** (r2 * t))
                total = varInter1 - varInter2
                print("The higher interest rate will cost you", round(total, 2), "more over the time span of", timeSpan, "years.")
            elif interestRate2 > interestRate1:
                varInter2 = principle * (e ** (r2 * t))
                varInter1 = principle * (e ** (r1 * t))
                total = varInter2 - varInter1
                print("The higher interest rate will cost you", round(total, 2), "more over the time span of", timeSpan, "years.")
        elif option == "5":
            print("Thank You!")
            print("Have a great day!")
            break
        else:
            print("Invalid!")
            print("Please enter a number between 1 and 5")
            return


main()


