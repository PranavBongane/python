is_not_prime = True
while is_not_prime:
    num = int(input("input prime number: "))
    if num > 1:
        for i in range(2,num):
            if (num%i) == 0:
                print("given number is not prime🦩")
                break
        else:
                is_not_prime = False
                print('given number is prime🥳')
    else:
         print("please enter number grater than 1")
           



