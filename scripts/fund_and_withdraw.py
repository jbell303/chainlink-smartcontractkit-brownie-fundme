from brownie import FundMe
from scripts.helpful_scripts import get_account

def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print("Entrance fee: {}".format(entrance_fee))
    print("funding...")
    fund_me.fund({"from": account, "value": entrance_fee})

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("withdrawing funds...")
    fund_me.withdraw({"from": account})
    print("funds withdrawn to: {}".format(account))

def main():
    fund()
    withdraw()