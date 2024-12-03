# Encapsulation
# 😊 Disallow direct changes of intenals yet maintaining UI

from typing import Self


class Account:
    def __init__(self, balance):
        self.balance = balance

    def __repr__(self) -> str:
        return f"Account(blance={self.balance})"

    @property
    def balance(self) -> int:
        return self._balancet

    @balance.setter
    def balance(self, amount: int) -> None:
        if amount < 0:
            raise ValueError(f"Cannot set {amount} amount. Amount cannot be negative.")
        self._balance = amount

    def __iadd__(self, amount: int) -> Self:
        if amount < 0:
            raise ValueError(f"Transaction failed. Negative deposit. Amount={amount}.")
        self.balance += amount

        return self

    def __isub__(self, amount: int) -> Self:
        if self.balance < amount:
            raise ValueError(
                f"Transaction failed. Overdraw. Balance cannot be {self.balance - amount}."
            )
        self.balance -= amount

        return self

    def __eq__(self, other) -> bool:
        amount = getattr(other, "amount", other)

        return self.balance == amount


class BankAccount:
    def __init__(self, balance: Account):
        self.balance = balance

    def __repr__(self) -> str:
        return f"Account(balance={self.balance})"


