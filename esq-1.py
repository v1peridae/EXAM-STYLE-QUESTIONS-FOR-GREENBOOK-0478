user_num = int(input("Enter your number of choice >>>"))
for i in range (user_num):
    print(i+1)
if user_num % 5 == 0:
    print("The number is divisible by five.")

elif user_num % 7 == 0:
    print("The number is divisible by seven.")