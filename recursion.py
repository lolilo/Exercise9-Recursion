# Multiply all the elements in a list
def multiply_list(l):
    # print l
    if len(l) == 1:
        return l[0] 
    else: 
        # print "multiplying %r and %r" %(multiply_list(l[1:]), l[0])
        return multiply_list(l[1:]) * l[0]

# Return the factorial of n
def factorial(n):
    if n == 1:
        return 1
    else: 
        return factorial(n - 1) * n

# Count the number of elements in the list l
def count_list(l):
    if len(l) == 1:
        return 1
    else: 
        return count_list(l[1:]) + 1

# Sum all of the elements in a list
def sum_list(l):
    if len(l) == 1:
        return l[0]
    else:     
        return sum_list(l[1:]) + l[0]

# Reverse a list without slicing or loops
def reverse(l):
    if len(l) == 1:
        return l # same as [l[0]]
    else:     
        # print "appending %r to %r" %(reverse(l[:-1]), l[-1])
        last_value = l.pop()
        return [last_value] + reverse(l)
        # .extend(reverse(l[:-1]))
        # return l

        # pop can also be used in previous recursive functions for another solution
        # BUT POP MUTATES L. I THINK THIS IS BAD, PURPLE!NICK.

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    # i = 0
    if n == 1:
        return 1
    elif n == 2:
        return 1 
    else:  
        return fibonacci(n - 1) + fibonacci(n - 2)

# Finds the item i in the list l.... RECURSIVELY
# if the item i doesn't exist, return NONE
def find(l, i):
    # print "the list is ", l
    if len(l) == 0:
        # return "%r does not exist in the list" % i
        return None
    elif i == l[0]:
        # return "%r exists in the list" % i
        return i
    else: 
        return find(l[1:], i)

# Determines if a string is a palindrome
def palindrome(some_string):

    if not some_string: # if string is empty
        return True
    elif some_string[0] != some_string[-1]:
        return False
    elif some_string[0] == some_string[-1]:
        return palindrome(some_string[1:-1])

# Given the width and height of a sheet of paper, 
# and the number of times to fold it, 
# return the final dimensions of the sheet as a tuple. 
# Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    if folds == 0:
        return width, height
    elif width > height: 
        return fold_paper(width/2, height, folds-1)
    else:
    # elif height > width: -- this did not account for if width = height
        return fold_paper(width, height/2, folds-1)

# Count up
# Print all the numbers from 0 to target
# n is the start number -- need a variable to keep track of the number to print
def count_up(target, n):
    if n == target:
        return target
    else: 
        print n
        return count_up(target, n + 1)

l = [1, 2, 3, 4, 5]
print "l = ", l
print "multiplied_list: ", multiply_list(l)
print "factorial: ", factorial(5)
print "count_list: ", count_list(l)
print "sum_list: ", sum_list(l)
print "reverse: ", reverse(l)
print "fibonacci: ", fibonacci(10) #this should equal 55
l = [1, 2, 3, 4, 5]
print "find: ", find(l, 3)
print "palindrome: ", palindrome('girafarig')
print "fold_paper: ", fold_paper(100, 50, 2)
print "count_up: ", count_up(30, 0)

