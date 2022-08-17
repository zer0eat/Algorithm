def func(a, N):          # a = 현재단계 N = 목표단계
    if a == N:
        print(a)
        return
    else:
        print(a)
        func(a+1, N)

func(0, 1000)

# 크기가 N인 배열의 모든 원소에 접근하는 재귀함수
def f(i,N):
    if i == N:      # 배열을 벗어남
        return
    else:           # 남은 원소가 있는 경우
        B[i] = A[i]
        f(i+1, N)

N = 3
A =[1, 2, 3]
B = [0] * N
print(B)
f(0, N)             # 0번 원소부터 N개의 원소에 접근
print(B)