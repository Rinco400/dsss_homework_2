import random


def random_interger_A(min, max):
    """
    Genarate a random integer between min & max
    """
    return random.randint(min, max)


def random_operator_B():

    """
    Genarate a random operator
    """
    return random.choice(['+', '-', '*'])


def result_calculation_C(n1, n2, o):
    """
    Calculate the result operator defined by n1, n2 & o.
    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def get_user_amswer():
    """
    Calculation Part
    """
    while True:

        try:
            user_input = input("Your answer: ")
            user_amswer = int(user_input)
            return user_amswer
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def math_quiz():
    Count = 0
    total_question = 8

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_question):
        n1 = random_interger_A(1, 10); 
        n2 = random_interger_A(1, 10); 
        o = random_operator_B()

        PROBLEM, ANSWER = result_calculation_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            Count += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {Count}/{total_question}")

if __name__ == "__main__":
    math_quiz()
