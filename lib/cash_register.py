#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.total = 0
    self.discount = discount
    self.items = []
    self.transactions = []

  @property
  def total(self):
    return self._total
  
  @total.setter
  def total(self, total):
    self._total = total

  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, discount):
    if type(discount) in [int, float]:
      self._discount = discount
    else:
      print("Discount must be a number.")
  
  def add_item(self, title, price, quantity=1):
    self.total += (price * quantity)
    self.transactions += [(price, quantity)]
    self.items += ([title] * quantity)

  def apply_discount(self):
    if (self.discount):
      self.total *= (100 - self.discount) / 100
      self.total = int(self.total)
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")
  
  def void_last_transaction(self):
    amount = self.transactions[-1][0]
    quantity = self.transactions[-1][1]

    for i in range(quantity):
      del self.items[-1]

    self.total -= (amount * quantity)
    del self.transactions[-1]