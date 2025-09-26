def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def power(a, b):
    return a ** b


def main():
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '^': power
    }

    while True:
        try:
            print("Wow. Doing math, huh? Fine, I'll help you")
            first_num = int(input("What is the first number? "))
            second_num = int(input("What is the second number? "))
            operation = input("What would you like to do (+, -, *, /, ^)? ")
            if operation not in operations.keys():
                print("By the way, that is not an operation. I don't even know how you thought that was a thing")
                print()
                continue
            print()

            print(operations[operation](first_num, second_num))
        except ValueError:
            print("You know you can't do math on words, right?")
        except ZeroDivisionError:
            print("You just divided by 0. Thanks to you, the world will now end")
        finally:
            if input("Would you like to try again (Y/n)? ").lower() == 'n':
                break


if __name__ == "__main__":
    main()
