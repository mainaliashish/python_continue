import random

def flip_coin():
  number = random.randint(0, 1)
  if number == 0:
    toss = 'HEAD'
  else:
    toss = 'TAIL'
  return toss

for _ in range(10):
  result = flip_coin()
  print(result)

