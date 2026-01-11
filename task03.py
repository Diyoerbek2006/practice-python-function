def deposit(balance: float, amount: float) -> float:
    if amount > 0:
        return balance + amount
    return balance


def can_withdraw(balance: float, amount: float) -> bool:
    return amount > 0 and balance >= amount


def withdraw(balance: float, amount: float) -> float:
    if can_withdraw(balance, amount):
        return balance - amount
    return balance
    
balance = 1000
print("Boshlang'ich balans:", balance)

balance = deposit(balance, 500)
print("Pul qo'shilgandan keyin:", balance)

balance = withdraw(balance, 200)
print("Pul yechilgandan keyin:", balance)

balance = withdraw(balance, 2000)
print("Yana yechishga urinish:", balance)
