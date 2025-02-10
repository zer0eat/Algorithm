# Favorite Number_BOJ10570

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 테스트 케이스를 input 받고
for n in range(N):                  # 테스트 케이스를 반복해서
    V = int(input())                # 숫자의 수를 input 받고
    ans = dict()                    # 딕셔너리를 생성해서
    for v in range(V):              # 숫자의 수를 반복하고
        num = int(input())          # 숫자를 input 받아서
        if ans.get(num) == None:    # 처음나온 숫자라면
            ans[num] = 1            # 딕셔너리에 추가하고
        else:                       # 처음나온 숫자가 아니라면
            ans[num] += 1           # 숫자의 개수를 추가한다
    maxN = [0, 1000]                # 정답을 저장할 리스트를 생성하고
    for a in ans:                   # 딕셔너리를 반복해서
        if maxN[0] == ans[a]:       # 개수가 같으면
            if maxN[1] > a:         # 숫자가 더 작을 때
                maxN[1] = a         # 그 값으로 바꿔주고
        elif maxN[0] < ans[a]:      # 개수가 더 많을 때
            maxN[0] = ans[a]        # 개수를 바꿔주고
            maxN[1] = a             # 숫자도 바꿔준다
    print(maxN[1])                  # 가장 많이 나온 최소값을 출력한다