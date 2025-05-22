class BankAccount:
    def __init__(self, owner, balance=0):
        """Инициализация банковского счета"""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Пополнение счета"""
        if amount > 0:
            self.balance += amount
            return f"Счет пополнен на {amount}. Новый баланс: {self.balance}"
        return "Сумма должна быть положительной"

    def withdraw(self, amount):
        """Снятие денег со счета"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Снято {amount}. Остаток на счете: {self.balance}"
        return "Недостаточно средств или неверная сумма"

    def get_balance(self):
        """Получение текущего баланса"""
        return f"Баланс: {self.balance}"

    def transfer(self, other_account, amount):
        """Перевод средств на другой счет"""
        if self.withdraw(amount) == f"Снято {amount}. Остаток на счете: {self.balance}":
            other_account.deposit(amount)
            return f"Переведено {amount} на счет {other_account.owner}"
        return "Перевод не выполнен"

# Пример использования
acc1 = BankAccount("Иван", 1000)
acc2 = BankAccount("Мария", 500)

print(acc1.deposit(200))
print(acc1.withdraw(500))
print(acc1.get_balance())
print(acc1.transfer(acc2, 300))
print(acc2.get_balance())
