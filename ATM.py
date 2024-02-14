# ATM Machine (RBI)
print('Welcome to RBI ATM')
p = int(input('Enter your 4 digit ATM Pin:')) # Pin = 4321
m = 25000
if (p == 4321):
    print('1-Withdraw Cash')
    print('2-Balance Enquiry')
    print('3-Quick Withdraw')
    c = int(input('Please choose transactions:'))
    if (c == 1):
        print('Only 500, 200 & 100 Rupee Notes available')
        w = int(input('Enter amount to withdraw:'))
        if (w < m and w%100 == 0):
            print('Please collect your cash:',w)
            print('Available balance:',m - w)
        else:
            print('Invalid Amount')
    elif(c==2):
        print('Your Account Balance is:',m)
    elif (c == 3):
        print('1-5,000')
        print('2-10,000')
        print('3-15,000')
        print('4-20,000')
        f = int(input('Select amount to withdraw:'))
        if (f == 1 and 5000 < m):
            print('please take cash 5000')
            print('Available balance:',m - 5000)
        elif (f == 2 and 10000 < m):
            print('please take cash 10000')
            print('Available balance:',m - 10000)
        elif (f == 3 and 15000 < m):
            print('please take cash 15000')
            print('Available balance:',m - 15000)
        elif (f == 4 and 20000 < m):
            print('please take cash 20000')
            print('Available balance:',m - 20000)
        else:
            print('Invalid account balance')
    else:
        print('Wrong choice')
else:
    print('Wrong pin number')