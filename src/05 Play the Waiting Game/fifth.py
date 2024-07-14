import random
import time

def waiting_game():
  t = random.randint(1, 5)
  print(f"Your target time is {t} seconds")
  input(" ---Press Enter to Begin--- ")
  start = time.perf_counter()

  input(f'\n...Press Enter again after {t} seconds...')
  end = time.perf_counter()-start

  print(f'\nElapsed time: {end :.3f} seconds')
  if end == t:
    print('(Unbelievable! Perfect timing!)')
  elif end < t:
    print(f'({t - end :.3f} seconds too fast)')
  else:
    print(f'({end - t :.3f} seconds too slow)')




waiting_game()