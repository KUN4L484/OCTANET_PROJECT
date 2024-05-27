#!/usr/bin/env python
# coding: utf-8

# In[3]:


import time

def atm_machine():
    print("Please insert Your CARD")
    
    # Simulate card processing
    time.sleep(3)
    
    password = 1234
    
    # Taking ATM pin from the user
    try:
        pin = int(input("Enter your ATM pin: "))
    except ValueError:
        print("Invalid input. Please enter numeric value.")
        return
    
    # User account balance
    balance = 5000
    
    # Checking if the pin is valid or not
    if pin == password:
        # Loop will run until the user exits
        while True:
            # Showing info to the user
            print("""
            1 == Balance
            2 == Withdraw balance
            3 == Deposit balance
            4 == Exit
            """)
            
            try:
                # Taking an option from the user
                option = int(input("Please enter your choice: "))
            except ValueError:
                print("Please enter a valid option.")
                continue
            
            if option == 1:
                print(f"Your current balance is {balance}")
                
            elif option == 2:
                try:
                    withdraw_amount = int(input("Please enter withdraw amount: "))
                except ValueError:
                    print("Invalid input. Please enter numeric value.")
                    continue
                
                if withdraw_amount > balance:
                    print("Insufficient balance.")
                else:
                    balance -= withdraw_amount
                    print(f"{withdraw_amount} is debited from your account.")
                    print(f"Your updated balance is {balance}")
                    
            elif option == 3:
                try:
                    deposit_amount = int(input("Please enter deposit amount: "))
                except ValueError:
                    print("Invalid input. Please enter numeric value.")
                    continue
                
                balance += deposit_amount
                print(f"{deposit_amount} is credited to your account.")
                print(f"Your updated balance is {balance}")
                
            elif option == 4:
                print("Thank you for using our ATM. Have a great day!")
                break
                
            else:
                print("Invalid option. Please try again.")
    else:
        print("Wrong pin. Please try again.")

# Run the ATM machine function
if __name__ == "__main__":
    atm_machine()


# In[ ]:




