def even_generater(limit):
    for i in range(2,limit+1,2):
        yield i

for i in even_generater(10):
    print(i)