# 수 나누기 게임_BOJ27172

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 플레이어 수를 input 받고
lst = list(map(int, input().split()))   # 플레이어의 카드를 리스트로 input 받는다
M = max(lst)                            # 가장 높은 카드를 M에 저장하고
dic = dict()                            # 카드 번호를 저장할 딕셔너리를 생성한다
for l in lst:                           # 카드번호를 반복해서
    dic[l] = 0                          # 카드번호를 key로 하는 원소를 생성한다
for i in lst:                           # 카드번호를 반복해서
    for j in range(i*2, M+1, i):        # i카드의 배수를 M까지 반복해서
        if dic.get(j) != None:          # i의 배수가 딕셔너리에 있다면
            dic[i] += 1                 # i의 승리점수를 추가하고
            dic[j] -= 1                 # j의 패배점수를 추가한다
for a in lst:                           # 카드번호를 반복해서
    print(dic[a], end=' ')              # 획득한 점수를 출력한다