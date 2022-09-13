# 사칙연산_1232

# 후위 순회를 위한 함수
def postorder(A):
    global ans
    if A:
        postorder(ch1[A])                       # 왼쪽 자식을 탐색하고
        postorder(ch2[A])                       # 오른쪽 자식을 탐색하고
        ans.append(word[A])                     # 나를 ans에 append한다

# input.txt 열기
import sys
sys.stdin = open('input.txt')
import math

# input 받기
T = 10                                          # 테스트 케이스
for t in range(T):                              # 테스트 케이스를 반복할 때
    N = int(input())                            # N에 트리의 노드의 수를 input 받고
    ch1 = [0] * (N + 1)                         # 왼쪽 자식의 인덱스를 저장할 리스트를 만들고
    ch2 = [0] * (N + 1)                         # 오른쪽 자식의 인덱스를 저장할 리스트를 만든다
    ans = []                                    # 후위 순회를 했을 때 결과를 저장할 리스트를 만들고
    word = [0] * (N + 1)                        # 해당 인덱스의 알파벳을 저장할 리스트를 만든다

    for n in range(N):                          # 노드의 숫자만큼 반복 했을 때
        node = list(input().split())            # 노드의 정보(0:부모노드/1:노드의성질/2:왼쪽자식노드/3:오른쪽자식노드) input 받은 후
        try:                                    # 시도할 수 있다면
            ch1[int(node[0])] = int(node[2])    # ch1 리스트의 부모노드 인덱스에 왼쪽자식노드 인덱스를 입력하고
            ch2[int(node[0])] = int(node[3])    # ch2 리스트의 부모노드 인덱스에 오른쪽자식노드 인덱스를 입력하고
            word[int(node[0])] = node[1]        # word 리스트의 부모노드 인덱스에 노드의 성질을 입력한다
        except:                                 # 시도할 수 없다면
            word[int(node[0])] = int(node[1])   # word 리스트의 부모노드 인덱스에 노드의 성질만 입력한다
    else:                                       # 반복이 끝났다면
        postorder(1)                            # 후위 순회를 하고

        calculation = []                        # 계산 값을 저장할 빈리스트를 만들고고

        while ans:                              # ans 리스트가 빌때까지 반복할 때
            A = ans.pop(0)                      # ans의 맨 앞 요소를 꺼냈을 때
            if A == '+':                        # +라면
                C = calculation.pop()           # calculation 맨 뒤에서 하나 꺼내 C라고 저장
                B = calculation.pop()           # calculation 맨 뒤에서 하나 꺼내 B라고 저장
                calculation.append(B + C)       # calculation B + C 연산을 append
            elif A == '-':                      # -라면
                C = calculation.pop()           # calculation 맨 뒤에서 하나 꺼내 C라고 저장
                B = calculation.pop()           # calculation 맨 뒤에서 하나 꺼내 B라고 저장
                calculation.append(B - C)       # calculation B - C 연산을 append
            elif A == '*':                      # *라면
                C = calculation.pop()           # calculation 맨 뒤에서 하나 꺼내 C라고 저장
                B = calculation.pop()           # calculation 맨 뒤에서 하나 꺼내 B라고 저장
                calculation.append(B * C)       # calculation B * C 연산을 append
            elif A == '/':                      # /라면
                C = calculation.pop()           # calculation 맨 뒤에서 하나 꺼내 C라고 저장
                B = calculation.pop()           # calculation 맨 뒤에서 하나 꺼내 B라고 저장
                calculation.append(B / C)       # calculation B / C 연산을 append
            else:                               # 숫자라면
                calculation.append(A)           # calculation에 append

        print(f'#{t+1}', math.ceil(*calculation))

