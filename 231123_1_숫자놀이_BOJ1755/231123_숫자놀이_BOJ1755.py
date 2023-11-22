# 숫자놀이_BOJ1755

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())    # N이상 M이하의 숫자를 확인하기 위해 input 받고
ans = []                            # 정답을 저장할 리스트를 생성한다
num = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}  # 숫자를 영어로 바꿀 딕셔너리를 생성하고
for i in range(N, M+1):             # N부터 M까지 반복해서
    tmp = ''                        # 숫자를 영어로 저장할 문자열을 생성하고
    for j in str(i):                # 숫자를 한자리씩 반복해서
        tmp += num[int(j)]          # tmp에 영어로 바꾼 숫자를 더한다
    else:                           # 숫자 반복을 마쳤다면
        ans.append([tmp, i])        # ans에 영어로 바꾼 숫자와 바꾸기 전 숫자를 append한다
ans.sort()                          # ans를 오름차순 정렬하고
cnt = 0                             # 10개씩 세기 위한 변수를 생성한 뒤
for i in ans:                       # 정답을 반복해서
    if cnt == 9:                    # cnt가 9라면
        print(i[1])                 # 숫자만 출력하고
        cnt = 0                     # cnt를 초기화한다
    else:                           # cnt가 9가 아니라면
        print(i[1], end=' ')        # 숫자를 출력하고 다음 출력문을 한 칸 띄고 출력하기 위한 end 조건을 설정한 후
        cnt += 1                    # cnt를 1 추가한다