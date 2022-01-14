def RPS(P1, P2):
    if P1 == "바위":
        if P2 == "바위":
            return "비겼습니다."
        elif P2 == "가위":
            return "{}가 이겼습니다!".format(P1)
        else:
            return "{}가 이겼습니다!".format(P2)

    elif P1 == "가위":
        if P2 == "가위":
            return "비겼습니다."
        elif P2 == "보":
            return "{}가 이겼습니다!".format(P1)
        else:
            return "{}가 이겼습니다!".format(P2)
    else:
        if P2 == "보":
            return "비겼습니다."
        elif P2 == "바위":
            return "{}가 이겼습니다!".format(P1)
        else:
            return "{}가 이겼습니다!".format(P2)

def get_P1_name():
    P1_name = input()
    return P1_name
def get_P2_name():
    P2_name = input()
    return P2_name
def get_P1():
    P1_RPS = input()
    return P1_RPS
def get_P2():
    P2_RPS = input()
    return P2_RPS

P1_name = get_P1_name()
P2_name = get_P2_name()
P1_RPS = get_P1()
P2_RPS = get_P2()

print(RPS(P1_RPS,P2_RPS))