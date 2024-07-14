from random import randint
from collections import Counter

def roll_dice(*args, trails=1_000_000):
  count = Counter()
  for _ in range(trails):
    count[sum(randint(1, dice) for dice in args)] += 1
  return count


dn = roll_dice(4, 6, 6)
print("OUTCOME PROBABILITY\n")
for key in dn:
  print(f"{key} \t\t {dn[key]*100/1_000_000}%")


