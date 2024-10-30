# Encapsulation
# 😊 Disallows direct changes of intenals (balance)


class BankAccount:
    def __init__(self, balance: int) -> None:
        self._balance = balance

    @property
    def balance(self) -> int:
        return self._balance

    def withdraw(self, amount: int) -> None:
        if amount > self._balance:
            raise ValueError("Insuffient funds")
        self._balance -= amount

    def deposit(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def __repr__(self) -> str:
        return f"Account(balance={self.balance}"


def main() -> None:
    account = BankAccount(100)
    account.withdraw(50)  #  solves potential issue of over withdrawing
    account.deposit(100)  # solves depositing negative amount
    print(account.balance)


if __name__ == "__main__":
    main()
