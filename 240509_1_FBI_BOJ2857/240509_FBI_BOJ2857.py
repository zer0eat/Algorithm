# FBI_BOJ2857

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = []                    # 정답을 저장할 리스트를 생성하고
for n in range(1, 6):       # 1부터 5까지 반복해서
    word = input().strip()  # 첩보원명을 input 받고
    if 'FBI' in word:       # 첩보원명에 FBI가 들어있다면
        ans.append(n)       # 첩보원명의 순서를 ans에 append한다
if ans:                     # 첩보원이 있다면
    print(*ans)             # 첩보원의 순서를 출력하고
else:                       # 첩보원이 없다면
    print('HE GOT AWAY!')   # HE GOT AWAY!를 출력한다