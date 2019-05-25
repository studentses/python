# Python Program - Check Armstrong Numbers

print("Enter 'x' for exit.");
num = input("Enter any number to check for armstrong: ");
if num == 'x':
    exit();
else:
    number = int(num);
    tot = 0;
    temp = number;
    while temp > 0:
        dig = temp % 10;
        tot += dig ** 3;
        temp //= 10;
    if number == tot:
        print(number,"is an Armstrong Number.");
    else:
        print(number,"is not an Armstrong Number.");