class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []
  
  
  def deposit(self, amount, description=''):
    self.ledger.append({"amount": amount, "description": description})
  
  
  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False
  

  def get_balance(self):
    total = 0
    for entry in self.ledger:
      total += entry['amount']
    return total
  

  def transfer(self, amount, other):
    if self.check_funds(amount):
      self.withdraw(amount, f'Transfer to {other.name}')
      other.deposit(amount, f'Transfer from {self.name}')
      return True
    else:
      return False
  

  def check_funds(self, amount):
    if self.get_balance() >= amount:
      return True
    else:
      return False
  

  def __str__(self):
    output = self.name.center(30, '*') + '\n'

    for entry in self.ledger:
      output += f"{entry['description'][:23].ljust(23)}{format(entry['amount'], '.2f').rjust(7)}\n"
    output += f"Total: {format(self.get_balance(), '.2f')}"
    return output


def create_spend_chart(categories):
  category_names = []
  spent = []
  spent_percentages = []

  for category in categories:
    total = 0
    for entry in category.ledger:
      if entry['amount'] < 0:
        total -= entry['amount']
    spent.append(round(total, 2))
    category_names.append(category.name)

  for amount in spent:
    spent_percentages.append(round(amount / sum(spent), 2)*100)

  graph = "Percentage spent by category\n"

  labels = range(100, -10, -10)

  for label in labels:
    graph += str(label).rjust(3) + "| "
    for percent in spent_percentages:
      if percent >= label:
        graph += "o  "
      else:
        graph += "   "
    graph += "\n"

  graph += "    ----" + ("---" * (len(category_names) - 1))
  graph += "\n     "

  longest_name_len = 0

  for name in category_names:
    if longest_name_len < len(name):
      longest_name_len = len(name)

  for i in range(longest_name_len):
    for name in category_names:
      if len(name) > i:
        graph += name[i] + "  "
      else:
        graph += "   "
    if i < longest_name_len-1:
      graph += "\n     "    

  return(graph)