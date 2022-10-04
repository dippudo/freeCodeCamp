# Feel free to download this code and comment out the original code to see how much better and faster the USING MEMORISATION code works


## ORIGINAL CODE
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


## USING MEMORISATION
# memorisation: store duplicate sub-problems so we can reuse solution later on
#   python dictionary (hashmap): keys = argument to function, value = return value

def fib(n, memo = {}):
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    memo[n] =  fib(n-1, memo) + fib(n-2, memo)
    print(memo) # this is to better visualise how Python is building the dictionary
    return memo[n]


## TEST CASES
print(fib(6)) # answer: 8
print(fib(7)) # answer: 13
print(fib(8)) # answer: 21

print(fib(50)) # answer: 12586269025
# ^ fib(50) is pretty slow in the original code because the code has to generate the numbers
