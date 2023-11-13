import random

def getnum(min, max):
    return random.randint(min, max)
#Random integer

def getsym():
    return random.choice(['+', '-', '*'])
#Random operation symbol


def prob_result(n1, n2, o):
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
        n1 = getnum(1, 10); n2 = getnum(1, 7); o = getsym()

        PROBLEM, ANSWER = prob_result(n1, n2, o)
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



