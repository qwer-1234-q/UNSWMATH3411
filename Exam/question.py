from test1 import ISBN, LZ78, codewordByLengths
from test3 import asymmetric, baseA, fermat, gcd, Markov, \
    prime, ShannonFano, humman
import arithmeticMore


end = "q: exit the question"
q0 = "0: arithmetic"
q1 = "1: Shannon-Fano"
q2 = "2: humman "
q3 = "3: gcd/Euler theorem/Unit/GF"
q4 = "4: fermat/square of a & b"
q5 = "5: ISBN"
q6 = "6: asymmetric"
q7 = "7: base for pseudo prime"
q8 = "8: 2-symbol Markov source"
q9 = "9: is prime or not"
q10 = "10: LZ78 encode/decode message"
q11 = "11: I-code with codeword lengths"
questions = [q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, end]


def askQue():
    print("*" * 80)
    for i in questions:
        print(i)
        
    t = input("Enter the question number: ")
    calQue(t)


def calQue(t):
    try:
        if str(t) == 'q' or t == "" or t is None:
            print("exit the function")
        else:
            t = int(t)
            if 0 <= t <= 9:
                question0_9(t)
            elif 10 <= t <= 19:
                question10_19(10)
            askQue()
    except ValueError:
        askQue()
        print("enter error: retype again plz.")
        print("if you want to exit, please type 'q' or 'Enter'")
    except ArithmeticError:
        print("arithmetic error: exit the system")


def question0_9(t):
    if t == 0:
        arithmeticMore.cal()
    elif t == 1:
        ShannonFano.cal()
    elif t == 2:
        humman.cal()
    elif t == 3:
        gcd.questionList()
    elif t == 4:
        fermat.cal()
    elif t == 5:
        ISBN.cal()
    elif t == 6:
        asymmetric.cal()
    elif t == 7:
        baseA.cal()
    elif t == 8:
        Markov.cal()
    elif t == 9:
        prime.cal()


def question10_19(t):
    if t == 10:
        LZ78.cal()
    elif t == 11:
        codewordByLengths.cal()


if __name__ == "__main__":
    print("Start to solve the questions!")
    askQue()