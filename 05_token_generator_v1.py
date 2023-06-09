import random

tokens = ("unicorn", "donkey", "zebra", "horse")
balance = 100

for item in range(0,100):
  chosen = random.choice(tokens)
  print(chosen)
  
  if chosen == "unicorn":
    balance += 4
  elif chosen == "donkey":
    balance -= 1
  else:
    balance -= 0.5

#output

print("Final Token: {} , Final Balance: ${}".format(chosen, balance))