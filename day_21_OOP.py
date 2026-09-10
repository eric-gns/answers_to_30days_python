# Day 21: Classes and Objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday! {self.name} is now {self.age}.")


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(self.balance)
            return self.balance
        else:
            print("Insufficient Funds!")