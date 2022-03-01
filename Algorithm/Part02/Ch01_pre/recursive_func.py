def recursive_function(i):
    if i == 100:
        return
    print("print recursive function", i, "->", i + 1)
    recursive_function(i+1)
    print(i, "function finish")

recursive_function(1)

def factorial_iterative(n):
    result = 1
    for i in range (1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print("iterative:", factorial_iterative(5))
print("recursive:", factorial_recursive(5))