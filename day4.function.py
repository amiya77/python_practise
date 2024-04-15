#Function
# def main():
#     testfunc(42)

# def testfunc(number, digit=None, numeric=None):
#     if digit is None:
#         digit = 50 
#     if numeric is None:
#         numeric = 100
#     print('this is a test function', number, digit, numeric)

# if __name__=='__main__':main()

#Arguments--------------------------------------------------
# def main():
#     testfunc(1, 2, 5, 10, 12, 15, 18)
# def testfunc(digit1, digit2, digit3, *args):
#     print(digit1, digit2, digit3, args)
#     for n in args: print (n, end=' ')
# if __name__=='__main__':main()

#Using Named Function Arguments------------------------------
# def main():
#     testfunc(one=1, two=2, three=3, four=4)
# def testfunc(**kwargs):
#     #print('this is a test function', kwargs['one'], kwargs['two'], kwargs['three'])
#     for k in kwargs: print(k, kwargs[k])
# if __name__=="__main__":main()

#Returning the value from functions--------------------------
# def main():
#     print(testfunc())
# def testfunc():
#     return 'this is a test func'

# if __name__=='__main__':main()

#Ex-1------------------------------------

# def main():
#     for n in testfunc(): print(n, end=' ')
# def testfunc():
#     return range(30)

# if __name__=='__main__':main()

#create a sequence with generator function
#Function with arguments-----------------------------
# def main():
#     def add_3_with_args(start, end):
#         result=[]
#         for num in range(start, end+1):
#             result.append(num + 3)
#         return result

#Generator Function----------------------------------
def add_3_generator(start, end):
    current = start
    while current <= end:
        yield current
        current += 3``
print("\n using generator function : ")
generator = add_3_generator(8, 25)
for num in generator:
    print (num)
    

    





if __name__=='__main__':main()

