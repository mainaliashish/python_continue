# for number in range(1, 8):
#   if number % 2 == 0:
#     print(number)

# number_of_times = input("How many times do I have to tell you : ")
# number_of_times = int(number_of_times)

# for _ in range(number_of_times):
#   print("CLEAN UP YOUR ROOM!")

# teams = ['a', 'b', 'c', 'd', 'e']

# for alphabet in teams:
#     print(alphabet.title())

# make a Copy list

list_one = [1,2,3,4,5]
# Method : 1
list_two = list_one[:]
# Method : 2
list_three = list_one.copy()

# the zip() function
names = ['ram', 'ashish', 'ashok', 'hari']
ages = [24,26,27,28]

# for name, age in zip(names, ages):
#     print(name, age)

for _i in range(len(names)):
    print(f"{names[_i].title()} : {ages[_i]}")

# for number in 5:
#     print(number)