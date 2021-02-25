# This is a sample Python script.
def sum_and_duplication(a, b):
    return (a + b) * 2


def print_result(data):
    print('Result is: ' + str(data))


if __name__ == '__main__':
    var_a = int(input('Input first number: '))
    var_b = int(input('Input second number: '))
    temp = sum_and_duplication(var_a, var_b)
    print_result(temp)
