'''
P.16 Multiplication table printer
'''


def multi_table(a):
    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(a, i, i*a))


if __name__ == '__main__':
    a = input('Please input a number: ')
    multi_table(a)
