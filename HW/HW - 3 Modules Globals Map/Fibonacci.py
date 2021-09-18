numFibCalls = 0

def myFib(n: int):
    """This function takes an integer n and calculates and returns the 
    resulting fibonacci number.  The function also updates a global
    variable numFibCalls that tracks the number of calls to the myFib
    function.  *** Note to correctly use the numFibCalls global variable
    user must reset the global variable to 0 at the beginning of the first
    use of the function to calculate the nth Fibonacci number. *** """    
    
    global numFibCalls 
    numFibCalls += 1

    if n == 0 or n == 1: 
        return 1
    else:
        return myFib(n-1) + myFib(n-2)


#def printNumRecursions() :
#    print('Number of fib calls: ', numFibCalls)