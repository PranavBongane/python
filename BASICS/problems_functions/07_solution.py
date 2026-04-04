def summ_all(*args):

    for i in args:
        print(i**2)
    return sum(args)



print(summ_all(1,2))
print(summ_all(1,2,3))
print(summ_all(1,2,4))
