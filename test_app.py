import pytest
from app import BankAccount
def test_initial_balance():
    acc = BankAccount()
    assert acc.check_balance() == 0.0
def test_deposit():
    acc = BankAccount()
    acc.deposit(100.0)
    assert acc.check_balance() == 100.0
def test_invalid_deposit():
    acc = BankAccount()
    with pytest.raises(ValueError):
        acc.deposit(-50.0)
