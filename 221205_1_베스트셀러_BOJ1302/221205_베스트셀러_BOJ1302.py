# 베스트셀러_BOJ1302

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())   # 팔린 책의 수
ans = dict()                    # 팔린 책의 이름과 숫자를 저장할 딕셔너리 생성

for n in range(N):              # 팔린 책의 수만큼 반복해서
    A = input()                 # 팔린 책의 이름을 input 받고
    if ans.get(A):              # 팔린 책의 이름이 key인 딕셔너리가 이미 있다면
        ans[A] += 1             # value에 한 권 더 더해주고
    else:                       # 팔린 책의 이름이 딕셔너리에 없다면
        ans[A] = 1              # 새로 만들고 value를 1로 해준다

cnt = 0                         # 판매된 책의 수를 저장할 변수를 만들고
book = []                       # 가장 많이 팔린 책을 저장할 빈 리스트를 만든다
for a in ans:                   # 딕셔너리를 반복해서
    if ans[a] > cnt:            # 더 많이 팔린 책이 나왔다면
        cnt = ans[a]            # cnt에 팔린 책의 수를 저장하고
        book = []               # book 리스트를 초기화 한 후
        book.append(a)          # book 리스트에 책 이름을 append 한다
    elif ans[a] == cnt:         # 판매된 책의 수가 같다면
        book.append(a)          # book 리스트에 책 이름을 append 하고
        book.sort()             # 오름차순으로 정렬하여
        book.pop()              # 사전상 뒤에 있는 책 이름을 pop 한다
print(*book)                    # 가장 많이 팔린 책을 출력한다