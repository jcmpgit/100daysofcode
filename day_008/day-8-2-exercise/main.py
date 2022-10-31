#Write your code below this line 👇
# # my solution
# def prime_checker(number):
#     if (n % 2 != 0) and (n % 3 != 0):
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")

# Teachers solution
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else: 
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



