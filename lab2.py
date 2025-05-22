import unittest

class BankAccount:
    MIN_BALANCE = 0
    TRANSACTION_LIMIT = 1

    def __init__(self, owner, balance=0):
        """Ініціалізація банківського рахунку"""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Поповнення рахунку"""
        if not self.is_valid_transaction(amount):
            return "Сума повинна бути додатньою"
        
        self.balance += amount
        return self.success_message("Рахунок поповнено", amount)

    def withdraw(self, amount):
        """Зняття грошей з рахунку"""
        if not self.is_valid_transaction(amount):
            return "Недостатньо коштів або сума неправильна"
        
        if amount > self.balance:
            return "Недостатньо коштів"
        
        self.balance -= amount
        return self.success_message("Знято", amount)

    def get_balance(self):
        """Отримання поточного балансу"""
        return f"Баланс {self.owner}: {self.balance}"

    def transfer(self, other_account, amount):
        """Передача коштів на інший рахунок"""
        if not self.is_valid_transaction(amount):
            return "Переказ не завершений"
        
        withdrawal_result = self.withdraw(amount)
        if "Знято" in withdrawal_result:
            other_account.deposit(amount)
            return f"Переведено {amount} на рахунок {other_account.owner}"
        
        return "Переказ не виконано"

    def is_valid_transaction(self, amount):
        """Перевірка правильності суми транзакції"""
        return amount >= self.TRANSACTION_LIMIT

    def success_message(self, action, amount):
        """Формування повідомлення про успішну операцію"""
        return f"{action} {amount}. Новий баланс: {self.balance}"

if __name__ == "__main__":
    account1 = BankAccount("Олексій", 100)
    account2 = BankAccount("Марія", 50)

    print(account1.deposit(50))
    print(account1.withdraw(30))
    print(account1.transfer(account2, 50))
    print(account1.get_balance())
    print(account2.get_balance())

# Тестування класу BankAccount
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount("Олексій", 100)
        self.account2 = BankAccount("Марія", 50)

    def runTest(self, method, description):
        print(f"\n*** Запуск тесту: {description}")
        try:
            method()
            print(f"+++ [Успішно] {description}")
        except AssertionError as e:
            print(f"--- [Помилка] {description}\n   {e}")

    def test_deposit(self):
        self.runTest(lambda: self.assertEqual(self.account1.deposit(50), "Рахунок поповнено 50. Новий баланс: 150"), "Поповнення рахунку")
    
    def test_withdraw(self):
        self.runTest(lambda: self.assertEqual(self.account1.withdraw(30), "Знято 30. Новий баланс: 70"), "Зняття коштів")

    def test_withdraw_insufficient_funds(self):
        self.runTest(lambda: self.assertEqual(self.account1.withdraw(200), "Недостатньо коштів"), "Зняття більшої суми, ніж на рахунку")
    
    def test_transfer(self):
        self.runTest(lambda: self.assertEqual(self.account1.transfer(self.account2, 50), "Переведено 50 на рахунок Марія"), "Переказ коштів")

    def test_transfer_insufficient_funds(self):
        self.runTest(lambda: self.assertEqual(self.account1.transfer(self.account2, 200), "Переказ не виконано"), "Переказ коштів при недостатньому балансі")

    def test_get_balance(self):
        self.runTest(lambda: self.assertEqual(self.account1.get_balance(), "Баланс Олексій: 100"), "Отримання балансу")

    def test_deposit_invalid(self):
        self.runTest(lambda: self.assertEqual(self.account1.deposit(-10), "Сума повинна бути додатньою"), "Поповнення рахунку некоректною сумою")

    def test_withdraw_invalid(self):
        self.runTest(lambda: self.assertEqual(self.account1.withdraw(0), "Недостатньо коштів або сума неправильна"), "Зняття некоректної суми")

    def test_transfer_invalid(self):
        self.runTest(lambda: self.assertEqual(self.account1.transfer(self.account2, 0), "Переказ не завершений"), "Переказ некоректної суми")

    def test_balance_update_after_transfer(self):
        self.account1.transfer(self.account2, 50)
        self.runTest(lambda: self.assertEqual(self.account1.get_balance(), "Баланс Олексій: 50"), "Оновлення балансу після переказу")
        self.runTest(lambda: self.assertEqual(self.account2.get_balance(), "Баланс Марія: 100"), "Оновлення балансу отримувача після переказу")

if __name__ == "__main__":
    unittest.main()
