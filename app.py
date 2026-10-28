class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance
    def check_balance(self):
        return self.balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance
def main():
    account = BankAccount()
    while True:
        print("\n--- Simple Banking Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            print(f"Current Balance: ${account.check_balance():.2f}")
        elif choice == "2":
            try:
                amt = float(input("Enter deposit amount: "))
                account.deposit(amt)
                print(f"Deposited ${amt:.2f}. New Balance: ${account.check_balance():.2f}")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
