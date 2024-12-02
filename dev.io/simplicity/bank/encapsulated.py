# Encapsulation
# 😊 Allows direct changes of intenals

from typing import Self


class Account:
    def __init__(self, balance):
        self.balance = balance

    def __repr__(self) -> str:
        return f"Account(blance={self.balance})"

    @property
    def balance(self) -> int:
        return self._balance

    @balance.setter
    def balance(self, amount: int) -> None:
        if amount < 0:
            raise ValueError(f"Cannot set {amount} amount. Amount cannot be negative.")
        self._balance = amount

    def __iadd__(self, amount: int) -> Self:
        if amount < 0:
            raise ValueError(
                f"Transaction failed. Negative depositing. Amount={amount}."
            )
        self.balance += amount

        return self

    def __isub__(self, amount: int) -> Self:
        if self.balance < amount:
            raise ValueError(
                f"Transaction failed. Overdrawing. Balance cannot be {self.balance - amount}."
            )
        self.balance -= amount

        return self


class BankAccount:
    def __init__(self, balance: Account):
        self.balance = balance

    def __repr__(self) -> str:
        return f"Account(balance={self.balance}"


def main() -> None:
    account = BankAccount(Account(100))
    account.balance -= 50  # potential issue of overwithdrawing e.g. 150
    account.balance += 100  # depositing negative amount
    print(account.balance)


if __name__ == "__main__":
    main()
