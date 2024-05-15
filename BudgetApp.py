class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item["amount"]
    return balance

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {category.name}")
      category.deposit(amount, f"Transfer from {self.name}")
      return True
    return False

  def check_funds(self, amount):
    return amount <= self.get_balance()

  def __str__(self):
    title = f"{'*' * 13}{self.name.center(0)}{'*' * 13}\n"
    items = ""
    total = 0
    for item in self.ledger:
      items += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
      total += item['amount']
    output = title + items + f"Total: {total:.2f}"
    return output


def create_spend_chart(categories):
  # Calculate the percentage spent in each category
  spent_percentages = []
  total_withdrawals = 0
  for category in categories:
    withdrawals = sum(item['amount'] for item in category.ledger
                      if item['amount'] < 0)
    total_withdrawals += withdrawals
    spent_percentages.append(withdrawals)

  spent_percentages = [(percentage / total_withdrawals) * 100
                       for percentage in spent_percentages]

  # Create the chart
  chart = "Percentage spent by category\n"
  for percentage in range(100, -10, -10):
    chart += f"{percentage:3}| {' '.join('o ' if round(p, -1) >= percentage else ' ' for p in spent_percentages)} \n"
  chart += "    ----------\n"

  # Determine the longest category name
  max_length = max(len(category.name) for category in categories)

  # Add category names below the chart
  for i in range(max_length):
    chart += "     "
    for category in categories:
      if i < len(category.name):
        chart += f"{category.name[i]}  "
      else:
        chart += "   "
    chart += "\n"

  return chart