def deposit(balance, money):
    print("입금이 완료 되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balacne, money): 
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원 입니다".format(balance))
        return balance

def withdraw_night(balance, money):
    commmission = 100 # 수수료
    return commmission, balance - money - commmission # 튜플, 여러 값을 반환

balance = 0
balance = deposit(balance, 1000)
balance = deposit(balance, 1000)

balance = withdraw(balance, 3000) # 실패

commmission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commmission, balance))