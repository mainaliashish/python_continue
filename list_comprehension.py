# Syntax [ _1_ for _2_ in _3_ ]
# 3 Components
# 1 --> method or function
# 2 --> iterator
# 3 --> list

numbers = [1, 2, 3]

result = [ num * 2 for num in numbers ]

print(result)

friends = ['ram', 'saroj', 'saurab', 'samrat']

f_results = [ friend.title() for friend in friends ]

print(f_results)

numbers = list(range(1,10))
odd_numbers = [ num for num in numbers if num % 2 == 1 ]
print(odd_numbers)
even_numbers = [num for num in numbers if num % 2 == 0 ]
print(even_numbers)
