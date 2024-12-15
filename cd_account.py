"""Import the Account class from the Account.py file."""
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    #balance = float(input("Enter the current CD account balance: "))
    #interest_rate = float(input("Enter the APR interest rate: "))
    #months = int(input("Enter the length of months for the CD: "))

    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    cd_account = Account(balance, interest_rate)

    # Calculate interest earned
    earned_interest = balance * (interest_rate / 100) * (months / 12)

    # Update the CD account balance by adding the interest earned
    balance += earned_interest

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    cd_account.set_balance(balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    cd_account.set_interest(earned_interest)

    # Return the updated balance and interest earned.
    return  balance, earned_interest

# Call the create_cd_account function and pass the required arguments.
#updated_cd_balance, earned_interest = create_cd_account()
#print(f"Updated balance: ${updated_cd_balance:.2f}")
#print(f"Interest earned: ${earned_interest:.2f}")