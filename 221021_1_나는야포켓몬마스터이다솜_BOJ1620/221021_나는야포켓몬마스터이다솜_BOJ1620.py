# 나는야포켓몬마스터이다솜_BOJ1620

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, M = map(int, sys.stdin.readline().split())           # N 도감에 등록할 포켓몬의 수 / M 검색할 포켓몬의 수

pocketmonNum = dict()                                   # 숫자를 key로 사용하는 도감을 딕셔너리로 생성

cnt = 1                                                 # cnt에 1번을 저장하고
for n in range(N):                                      # N마리의 포켓몬을 반복해서
    A = sys.stdin.readline().rstrip()                   # A에 포켓몬 이름을 받아주고
    pocketmonNum[cnt] = A                               # 번호를 키로 이름을 밸류로 하는 요소를 딕셔너리에 저장한다
    cnt += 1                                            # 저장후에 번호를 다음번호로 변경한다

pocketmonName = {v:k for k,v in pocketmonNum.items()}   # 키 - 밸류가 바뀐 딕셔너리를 생성한다

for m in range(M):                                      # 검색할 포켓몬을 반복해서
    B = sys.stdin.readline().rstrip()                   # 포켓몬의 정보를 input 받고

    try:                                                # 입력받은 정보가 정수라면
        B = int(B)                                      # B를 정수로 변환한 후
        print(pocketmonNum[B])                          # 번호에 맞는 포켓몬 이름을 출력한다
    except:                                             # 입력받은 정보가 포켓몬 이름이라면
        print(pocketmonName[B])                         # 포켓몬 이름에 맞는 번호를 출력한다
