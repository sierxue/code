'''
Enhanced multiplication table printer
'''


def multi_table(a, b):
    for i in range(1, b+1):
        print('{0} x {1} = {2}'.format(a, i, i*a))


if __name__ == '__main__':
    a = input('Please input a number: ')
    b = input('Please input nunbmer of Multiplication: ')
    multi_table(float(a), b)
