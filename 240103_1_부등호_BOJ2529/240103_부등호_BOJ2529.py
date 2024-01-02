# 부등호_BOJ2529

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
K = int(input())                    # 부등호의 개수를 input 받고
lst = list(input().split())         # 부등호를 list로 input 받는다
ans = []                            # 부등호를 만족하는 숫자를 저장할 리스트를 생성하고

def inequality(K, tmp):
    cnt = len(tmp)                  # tmp에 저장된 개수를 cnt에 저장하고
    if cnt > K:                     # cnt의 수가 K보다 커지면
        ans.append(tmp[:])          # ans에 부등호를 만족하는 숫자를 append한다
        return                      # 함수를 return한다
    for i in range(10):             # 0부터 9까지 반복해서
        if cnt:                     # cnt가 비어있지 않다면
            if lst[cnt - 1] == '<' and tmp[-1] < i and i not in tmp:    # 앞 숫자보다 i가 더크며, i가 tmp에 없다면
                tmp.append(i)       # i를 tmp에 append하고
                inequality(K, tmp)  # inequality를 통해 다음 숫자를 탐색한다
                tmp.pop()           # i를 tmp에서 pop한다
            elif lst[cnt - 1] == '>' and tmp[-1] > i and i not in tmp:  # 앞 숫자보다 i가 더 작으며, i가 tmp에 없다면
                tmp.append(i)       # i를 tmp에 append하고
                inequality(K, tmp)  # inequality를 통해 다음 숫자를 탐색한다
                tmp.pop()           # i를 tmp에서 pop한다
        else:                       # cnt가 비어있다면
            tmp.append(i)           # i를 tmp에 append하고
            inequality(K, tmp)      # inequality를 통해 다음 숫자를 탐색한다
            tmp.pop()               # i를 tmp에서 pop한다

inequality(K, [])                   # inequality를 부등호에 맞는 숫자를 탐색한다
ans.sort()                          # 저장된 정답을 오름차순으로 정렬해서
for a in ans[-1]:                   # 부등호를 만족하며 사전순으로 가장 큰 숫자를
    print(a, end='')                # 공백없이 출력한다
print()                             # 줄을 바꿔주고
for b in ans[0]:                    # 부등호를 만족하며 사전순으로 가장 작은 숫자를
    print(b, end='')                # 공백없이 출력한다