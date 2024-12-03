# No Encapsulation
# 😔 Allows direct changes of intenals


class BankAccount:
    def __init__(self, balance: int) -> None:
        self.balance = balance

    def __repr__(self) -> str:
        return f"Account(balance={self.balance}"
