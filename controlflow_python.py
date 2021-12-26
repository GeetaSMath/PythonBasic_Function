# for loop
# example
employee_list = [('geeta', 1), ('Anu', 2)]
for i in employee_list:
    print(i)
# for loop using break
student_records = ["aaaa", "bbb", "cccc", "dddd"]
for n in student_records:
    print(n)
    if n == " ":
        continue

# while loop
i = 0
while i < 6:
  i += 1
  if i == 3:
    # break
    continue
  print(i)

# lambda function
# syntax of lambda expression (arguments : expression)
add = lambda a: a+20
print(add(30))

# create list with all square numbers from list
# using for loop

numbers = [1, 3, 4, 5]                 # created list
square_nums = []                       # created empty list
square = lambda n: n ** 2               # using lambda expression taken list in square number
for num in numbers:                     # for loop taken new varible to strore into empty list
    square_nums.append(square(num))     # here appending list into empty list, num is arguments it pass to numbers
print(square_nums)

# to overcome this methode to make more elegant of code
# create list
# using map type we can take lambda function to perform on given condition

numbers = [2, 3, 4, 5]
square_nums =list(map(lambda x: x ** 2, numbers))
print(square_nums)

# filter function
# syntax: filter(function, iterable)
# create two list
item1 = [2, 3, 5, 6, 7]
item2 = [2, 4, 6, 7, 0, 8]
print("iterated items")
item3 = list(filter(lambda n: n in item1, item2))
print(item3)

# reduce function
# syntax: reduce(function, iterable)
from functools import reduce    # import reduce library
a = reduce((lambda x, y: x * y), [1, 2, 4, 4, 5])  # reduced items
# itereted items
print(a)


