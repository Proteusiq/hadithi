import pytest
from encapsulated import Account


def test_good_account():
    # Arrange
    account = Account(0)

    
    # Act
    account.balance = 42
    

    # Assert
    assert account.balance == 42


def test_bad_account():
      # Arrange
    account = Account(0)

    with pytest.raises(ValueError) as e:
    
         # Act
        account.balance = -42  

    # Assert
    assert "Amount cannot be negative" in str(e.value)


