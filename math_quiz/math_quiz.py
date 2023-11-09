import random

def function_A(min, max):
    return random.randint(min, max)
#Random integer

def function_B():
    return random.choice(['+', '-', '*'])
#Random operation symbol


def function_C(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 + n2
    elif o == '-': a = n1 - n2
    else : a = n1 * n2
    return p, a
#Create the problem and result

def math_quiz():
    s = 0
    p = 4

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(p):
        n1 = function_A(1, 10); n2 = function_A(1, 7); o = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)#input the answer and convert to integer
        except ValueError:
            print("Please enter A NUMBER!")

        if useranswer == ANSWER:#for correct answer
            print("Correct! You earned a point.")
            s += 1
        else:#for wrong answer
            print(f"Wrong answer. The correct answer is {ANSWER}.")
    print(f"\nGame over! Your score is: {s}/{p}")

if __name__ == "__main__":
    math_quiz()
