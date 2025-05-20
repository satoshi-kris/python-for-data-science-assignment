# Task 1: Prime Number Check

# Pseudocode:
# 1. Start
# 2. Input number
# 3. If number <= 1: Not Prime
# 4. For i from 2 to sqrt(number):
#      If number % i == 0: Not Prime
# 5. If no divisors found: Prime
# 6. End

# Flowchart Steps:
# [Start] -> [Input Number] -> [Is number <= 1?]
#   Yes -> [Not Prime] -> [End]
#   No -> [i = 2 to sqrt(n): Is n % i == 0?]
#     Yes -> [Not Prime] -> [End]
#     No -> [Prime] -> [End]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print("The number is Prime.")
else:
    print("The number is Not Prime.")