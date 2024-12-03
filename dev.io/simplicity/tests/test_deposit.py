import pytest
from encapsulated import BankAccount, Account


def test_good_deposit():
    # Arrange
    account = BankAccount(Account(100))

    # Act
    account.balance += 50

    # Assert
    assert account.balance == 150


def test_bad_withdraw():
    # Arrange
    account = BankAccount(Account(120))

    with pytest.raises(ValueError) as e:
        # Act
        account.balance += -150

    # Assert
    assert "Negative deposit" in str(e.value)
