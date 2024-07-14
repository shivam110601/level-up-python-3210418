import re

def is_palindrome(sent: str) -> bool:
  sent = "".join(re.findall(r"[a-z]+", sent.lower()))
  rev = sent[::-1]
  return sent == rev

print(is_palindrome("Race car.!!"))
print(is_palindrome("name IS ie man"))
print(is_palindrome("najknfoiahg"))