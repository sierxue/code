'''
Exercise
'''

def even_or_odd(b):

    if b % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':

    b = input('Your Number Please: ')
    b = float(b)

    if b.is_integer():
        eo = even_or_odd(b)
        if eo == True:
            print('Even nubmer')
        else:
            print('Odd number')

        for i in range(10):
            print(b+2*i)
    else:
        print('Please enter an integer')
