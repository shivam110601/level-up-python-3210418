def get_prime_factors(n):
  divisor = 2
  op = []

  while(n != 1):
    if n%divisor == 0:
      n /= divisor
      op.append(divisor)
    else:
      divisor += 1

  return op

n = int(input())
print(get_prime_factors(n))