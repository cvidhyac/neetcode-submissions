class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts : int =0
    total_balance : int =0

    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance


# TODO: Create two accounts
bank_acc_one = BankAccount("Alice", 1000)
bank_acc_two = BankAccount("Bob", 2000)

# TODO: Print the information using the mentioned format
print(f"Alice's balance: ${bank_acc_one.balance}")
print(f"Bob's balance: ${bank_acc_two.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")