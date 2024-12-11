"""Import the Account class from the Account.py file."""
from Account import Account

# Define a function for the Savings Account
def create_savings_account():
    """Creates a savings account, calculates interest earned, and updates the account balance.
    
    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    balance = float(input("Enter the current account balance: "))
    interest_rate = float(input("Enter the APR interest rate: "))
    months = int(input("Enter the length of months to determine the amount of interest: "))

    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    account = Account(balance, interest_rate)

    # Calculate interest earned
    earned_interest = balance * (interest_rate / 100) * (months / 12)

    # Update the savings account balance by adding the interest earned
    balance += earned_interest

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    account.set_balance(balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    account.set_interest(earned_interest)

    # Return the updated balance and interest earned.
    return balance, earned_interest

# Call the create_savings_account function and pass the required arguments.
updated_balance, earned_interest = create_savings_account()
print(f"Updated balance: ${updated_balance:.2f}")
print(f"Interest earned: ${earned_interest:.2f}")