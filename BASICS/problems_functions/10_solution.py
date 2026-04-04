def factoriels(n):
    if n == 0:
        return 1
    else:
        return n * factoriels(n-1)
    
print(factoriels(5))