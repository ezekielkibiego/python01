a = 6
b = 5


print(a != b) # a is not equal to b
print(b > a) # a is greater than b
print(a >= b) 
print(a < b)
print(a <= b)
print(a is b) # a == b
print(a is not b) # a != b


# Logical Operators
print(a > b and a == b)
print(a > b or a == b)

# a is not equal to b
print(not(a == b))


# Conditionals ~ if and else

x = 5
# indent

if x >= 10: 
    print('x is greater than 10')

else:
    print('x is less than 10')
    
    
if x % 2 == 0:
    print('x is even.')
else: 
    print('x is odd.')
    
