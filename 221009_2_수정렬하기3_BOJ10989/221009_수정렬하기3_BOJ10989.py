# 수정렬하기3_BOJ10989

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())       # N 정렬할 숫자의 개수
ans = dict()                        # 정렬할 숫자를 저장할 빈 딕셔너리 생성
for n in range(N):                  # 정렬할 숫자만큼 반복할 때
    a = int(sys.stdin.readline())   # a에 정렬할 숫자를 input 받고
    try:                            # 딕셔너리에 이미 a가 키인 값이 있다면
        ans[a] = ans.get(a) + 1     # 키가 a인 밸류에 1을 더해준다
    except:                         # 딕셔너리에 a가 키인 값이 없다면
        ans[a] = 1                  # a가 키이고 밸류가 1인 값을 생성해서 넣어준다

ans = sorted(ans.items())           # ans 딕셔너리를 키값의 오름차순으로 정렬해주고

for a in ans:                       # 정렬한 숫자를 반복해서
    for b in range(a[1]):           # 중복된 숫자의 개수만큼
        print(a[0])                 # 숫자를 출력해준다