# coding=utf-8

# 26.09.16

# 1
###############################################################################

def handle():
    bill = input('Enter the bill sum \n')
    if bill:
        try: 
            res = get_total(float(bill))
            print('Total is {}'.format(res))
        except ValueError as e:
            print('Error. Enter a valid number.')
            handle()

def get_total(bill):
    if bill > 100:
        return bill * 1.2
    elif bill > 50:
        return bill * 1.15
    elif bill > 25:
        return bill * 1.12
    
    return bill * 1.1

if __name__ == '__main__':
    handle()
