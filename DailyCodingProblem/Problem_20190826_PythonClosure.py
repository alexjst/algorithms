"""
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""

"""
My notes: In python, functions are first-class citizens, meaning first-class objects. so functions can be passed around as objects using their names.
The context or environment for that function object is called 'closure', it's just the bunch of variables and whatever other functions (as objects)
that must go together with the function object itself so that function can work. Knowing this, let's look at the function 'cons': it defines a
function called 'pair', whatever pair of parameters are passed to 'cons', it returns a function who is able to take another function (f) that takes
these two parameters.
"""

# so I expect car(pair) to return the first element
def car(pair):
    def return_first(a, b):
        return a
    return pair(return_first)

# why the above should work?
# when calling car(cons(3,4)), the inner 'cons(3,4)' returns the function 'pair' with 3 & 4 being in its closure, and it is able to take in any function and call it with 3 & 4
# that 'any function' here is 'return_first', so it can take 'return_first' and call it with 3 & 4. In other words, car(cons(3,4)) returns 'return_first(3,4)' that will return 3

def cdr(pair):
    def return_second(a, b):
        return b
    return pair(return_second)

# this is quite similar to the above
