# 점수계산_BOJ2822

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
cnt = 0                                     # 점수의 순서를 정할 변수를 생성하고
ans = []                                    # 점수를 담을 리스트를 생성한다
for _ in range(8):                          # 8문제를 반복해서
    cnt += 1                                # 문제 번호를 1 올리고
    A = int(sys.stdin.readline().strip())   # A에 점수를 input 받는다
    if len(ans) < 5:                        # ans에 정답의 개수가 5보다 작을 때는
        ans.append([A, cnt])                # ans에 점수와 문제번호를 리스트 형태로 append하고
    else:                                   # 5가 넘는다면
        ans.sort()                          # 정렬해서
        if A > ans[0][0]:                   # A가 가장 작은 점수보다 크다면
            ans.pop(0)                      # 가장 작은 점수를 갖는 문제를 빼고
            ans.append([A, cnt])            # A와 문제번호를 리스트형태로 append한다
else:                                       # 8문제 반복을 모두 마쳤다면
    tmp = []                                # 5문제의 문제번호를 저장할 리스트를 생성하고
    sumN = 0                                # 5문제의 점수의 합을 저장할 변수를 생성한다
    for a in ans:                           # 정답을 담은 리스트를 반복해서
        sumN += a[0]                        # 점수는 sumN에 더하고
        tmp.append(a[1])                    # 문제번호는 tmp에 append한다
    else:                                   # 반복이 모두 끝났다면
        tmp.sort()                          # 문제번호를 오름차순으로 정렬하고
        print(sumN)                         # 점수의 총합을 출력하고
        print(*tmp)                         # 문제번호를 출력한다
