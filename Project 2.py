"""Text-based Calculator"""

def get_number(number):
    while True:
        operand1 = input('Number: ' + str(number) + ': ')
        try:
            return float(operand1) #because return kills the function we do not need 'break' unless you type wrong thing
        except:
            print('invalid input asshole')


operand1 = get_number(1)
operand2 = get_number(2)
sign = input('Sign: ')

if sign == '+':
    result = operand1 + operand2
    print(operand1, sign, operand2)
elif sign == '-':
    result = operand1 - operand2
    print(operand1, sign, operand2)
elif sign == '*':
    result = operand1 * operand2
    print(operand1, sign, operand2)

elif sign == '/':
    result = operand1 / operand2
    print(operand1, sign, operand2)
    
print(result)

