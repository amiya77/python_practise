# fh = open('lines.txt')
# for line in fh.readlines():
#     print(line)



# ab = open('lines.txt')

# for line in ab.readlines():
#     print(line, end= '')

#enumerate iterator
my_list = ['apple', 'grapes', 'guava', 'orange']
for fruit, value in enumerate(my_list):
    print(f"Fruit: {fruit}, Value: {value}")