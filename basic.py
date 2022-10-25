# x =10

# def foo():
#     x = 20

#     def bar():
#         print("dsnfnjkdsbfjkndsj")
#         global x
#         x = x + 25
        
#     print("Before calling bar: ", x)
#     print("Calling bar now")
#     bar()
#     print("dfdfd")
#     print("After calling bar: ", x)



# foo()
# print("x in main: ", x)

# def fib(n):
#    p, q = 0, 1
#    while(p < n):
#        yield p
#        p, q = q, p + q
# x = fib(10)    # create generator object 
# print(x.__next__())
## iterating using __next__(), for Python2, use next()
# x.__next__()    # output => 0
# x.__next__()    # output => 1
# x.__next__()    # output => 1
# x.__next__()    # output => 2
# x.__next__()    # output => 3
# x.__next__()    # output => 5
# x.__next__()    # output => 8
# x.__next__()    # error
 
# def simple_generator():
#     x = 1
#     yield x
#     yield x + 1
#     yield x + 2

# generator_object = simple_generator()

# print(generator_object.__next__())
# print(generator_object.__next__())
# print(generator_object.__next__())

# class Calculator:

#     # create addNumbers static method
#     @staticmethod
#     def addNumbers(x, y):
#         return x + y

# print('Product:', Calculator.addNumbers(15, 110))



# sum = 0
# while(True):
#     userInput = input("Enter the price : \n")
#     if (userInput!='q'):
#         sum = sum + int(userInput)
#         print(sum)
#     else:
#         print("thanks for using our calculator")
#         print(sum)
#         break



























# a = 1

# Uses global because there is no local 'a'
# def f():
# 	print('Inside f() : ', a)

# # Variable 'a' is redefined as a local
# def g():
# 	a = 2
# 	print('Inside g() : ', a)

# # Uses global keyword to modify global 'a'
# def h():
# 	global a
# 	a = 3
# 	print('Inside h() : ', a)


# # Global scope
# print('global : ', a)
# f()
# print('global : ', a)
# g()
# print('global : ', a)
# h()
# print('global : ', a)



# stud = 'Joshua' # Global variable
# roll_no = 26    # Global variable

# def display():
#     global roll_no
#     roll_no = roll_no + 4
#     # Updating 1 global variable in local function
#     print('Inside display() student roll_no value:', roll_no)

# display()
# print('Global variable roll_no value:', roll_no)


# def func():
#     val = 20   
#     def change():
#          global val
#          val = 50
#          print('Inside change():', val)       
#     print('Inside func():', val)
#     print('Calling change() nested function')
#     change()
#     print('After calling change():', val)

# func()
# print('Global variable value now:', val)

def gen_func(x):
    for i in range(x):
        yield i