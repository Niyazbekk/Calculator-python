def calc(num1, num2, operation):
    """
    :param num1: number 1
    :param num2: number 2
    :param operation: Operation
    :return: The answer
    """
    if operation not in '+-/*':
        return 'Choose one type of these chr: "+ , - ,* ,/" ! '

    if operation == '+':
        return str(num1) + ' ' + operation + ' ' + str(num2) + ' = ' + str(num1 + num2)

    if operation == '-':
        return str(num1) + ' ' + operation + ' ' + str(num2) + ' = ' + str(num1 - num2)

    if operation == '*':
        return str(num1) + ' ' + operation + ' ' + str(num2) + ' = ' + str(num1 * num2)

    if operation == '/':
        return str(num1) + ' ' + operation + ' ' + str(num2) + ' = ' + str(num1 / num2)


def main():
    num1 = float(input('First number :'))

    num2 = float(input('Second number :'))

    operation = input('What kind of operation would you like to do?\nChoose between "+, -, *, /" : ')

    print(calc(num1, num2, operation))


if __name__ == '__main__':
    main()
