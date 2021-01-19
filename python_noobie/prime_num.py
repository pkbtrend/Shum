from sys import argv
app, param = argv
param = int(argv[1])

if param < 10000:
    param = 10000

print("Prime numbers to natural numbers ratio in range from 1 to", param)

# range which includes also the latest member
def inclusive_range(start, end, step):
    return range(start, end+1, step)

# list of prime numbers    
prime_numbers_list = []

# amount of prime numbers
prime_numbers_amount = 0

# we will indicate progress in 10s of %
progress_val = 0
progress_indicator = [">          |  0%", "$>         | 10%",\
                      "$$>        | 20%", "$$$>       | 30%",\
                      "$$$$>      | 40%", "$$$$$>     | 50%",\
                      "$$$$$$>    | 60%", "$$$$$$$>   | 70%",\
                      "$$$$$$$$>  | 80%", "$$$$$$$$$> | 90%",\
                      "$$$$$$$$$$>|100%",]

for num in inclusive_range(2, param, 1):
    prime_flag = 1
    factor = 2
    
    #we can check only prime factors due all other factors are composition of primes
    for factor in prime_numbers_list:
    
        # if factor > num/2, then answer will be not natural
        if(factor > num/2):
            break

        # one founded factor is enough
        if num%factor == 0:
            prime_flag = 0
            break

    # store the prime number
    if prime_flag == 1:
        prime_numbers_amount += 1
        prime_numbers_list.append(num)

    # progress indicator
    if ((num*10)/param) - 1 > progress_val:
        progress_val += 1
        print(progress_indicator[progress_val], end = "\r")

print(progress_indicator[10])

print ("is", prime_numbers_amount/param)
