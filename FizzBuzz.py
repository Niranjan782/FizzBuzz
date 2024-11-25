
                                                # FIZZBUZZ Program #

                                         #This is a simple FizzBuzz Program in python

#This is the FizzBuzz Program for the values upto 100 with a condation that it gives 'Fizz' for the multiples of 3 and 'Buzz' for the multiples of 5
#if the number is like multiple of both 3 and 5 it will 'FizzBuzz'

for num in range(1,101):
    if num%3==0 and num%5==0:
        print('FizzBuzz')
    elif num%3==0:
        print('Fizz')
    elif num%5==0:
        print('Buzz')
    else:
        print(num)



#This code can be used if we need to manually enter the starting and ending range for the 'FizzBuzz' program

Starting = int(input("Enter the starting number: "))
Ending= int(input("Enter the ending number: "))
for num in range(Starting,Ending+1):
    if num%3==0 and num%5==0:
        print('FizzBuzz')
    elif num%3==0:
        print('Fizz')
    elif num%5==0:
        print('Buzz')
    else:
        print(num)


