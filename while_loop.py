# msg = input("Whats the secret password : ")

# while msg != 'bananas':
#   print("Wrong Password!")
#   msg = input("Whats the secret password : ")

# print("Correct Password!")

# number = 1
# while number < 11:
#   print(number)
#   number += 1

# for i in range(1, 11):
#   print(i)

# msg = ''
# while msg != 'stop copying me':
#   msg = input("Say something : ")
#   print(msg)

times = int(input("How many times do you want to clean the room :"))

for time in range(times):
  print("Cleaning the room..")
  if time >= 5:
    print("Do you want to clean the room more?")
    break