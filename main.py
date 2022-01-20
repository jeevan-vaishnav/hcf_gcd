num1 = int(input("Enter first number\n"))
num3 = int(input("Enter second number\n"))

if num1 > num3:
    mn = num1
else:
    mn = num3

for i in range(1, mn+1):
    if num1 % i == 0 and num3 % i == 0:
        hcf = i


print(f"The HCF/GCD of these two number is {hcf}")
