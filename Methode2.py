number = input('Enter Any Number ')
for i in range(2, int(number)):
        if int(number) % i == 0:
            print('It is not a prime Number So -1 ')
            break
        else:
            totals = 0
            for total in range(int(number) + 1):
                totals += total
            print(f'It is a prime Number and the Sum is {totals}')
            break