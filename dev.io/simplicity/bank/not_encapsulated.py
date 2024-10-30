# No Encapsulation
# 😔 Allows direct changes of intenals


class BankAccount:
    def __init__(self, balance: int) -> None:
        self.balance = balance

    def __repr__(self) -> str:
        return f"Account(balance={self.balance}"


def main() -> None:
    account = BankAccount(100)
    account.balance -= 50  # potential issue of overwithdrawing e.g. 150
    account.balance += 100  # depositing negative amount
    print(account.balance)


if __name__ == "__main__":
    main()
