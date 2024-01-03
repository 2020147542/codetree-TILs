inputs = input().split()

a = int(inputs[0])
o = inputs[1]
c = int(inputs[2])


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def divide(a, b):
    return a // b


def multiple(a, b):
    return a * b


if o == "+":
    print(a, o, c, "=", plus(a, c))
elif o == "-":
    print(a, o, c, "=", minus(a, c))
elif o == "/":
    print(a, o, c, "=", divide(a, c))
elif o == "*":
    print(a, o, c, "=", multiple(a, c))
else:
    print("False")