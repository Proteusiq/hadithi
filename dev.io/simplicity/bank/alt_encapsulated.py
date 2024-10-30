# Encapsulation
# 😊 Disallows direct changes of intenals keeping original main
from __future__ import annotations


class BankAccount:
    def __init__(self, balance: int) -> None:
        self._balance = balance

    def __iadd__(self, amount: int):
        print("I am here")
        if amount < 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount

        return self

    def __isub__(self, amount: int):
        print("I am negative")
        if amount > self._balance:
            raise ValueError("Insuffient funds")

        self._balance -= amount
        return self

    def __repr__(self) -> str:
        return f"Account(balance={self._balance})"


def main() -> None:
    balance = BankAccount(100)
    balance += 50  #  solves potential issue of over withdrawing
    balance -= 190  # solves depositing negative amount
    print(balance)


if __name__ == "__main__":
    main()
