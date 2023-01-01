print("Welcome to the shopping cart list".upper())
shopping_cart = []
running = True

while running:
    item_list = input("Add something to the cart? Type q to quit : ")
    if item_list.lower() == 'q':
        # running = False
        break
    else:
        shopping_cart.append(item_list)

print("\n")
print("YOUR FINAL GROCERY LIST : ")
for _item in shopping_cart:
    print(f"- {_item}")

# Demo List

demo_list = [1, 'a', 'Wine', '2.5']
# print(demo_list.__len__())

for idx, _item in enumerate(demo_list):
    print(idx, _item)

greet = "hello how are you doing?"

reverse_greet = greet[::-1]
print(reverse_greet)

print(greet.reverse())
topics = ['Physics', 'Computer Science', 'Algebra', 'Arts']
print(topics[::-1])
print(topics)
print(type(topics))
print(dir(topics))

colors = ['red', 'orange', 'green']
colors.append('white')
# colors.extend('gray')
# colors[5] = 'yellow'
colors.append('blue')
print(colors)