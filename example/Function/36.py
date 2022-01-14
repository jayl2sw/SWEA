def get_number():
    n = int(input())
    return n

def judge_prime(number):
    k = 0
    for i in range(number):
        if number % (i+1) == 0:
            k += 1
    if k == 2:
        print("소수입니다.")
    else:
        print("소수가 아닙니다.")
n = get_number()
judge_prime(n)
