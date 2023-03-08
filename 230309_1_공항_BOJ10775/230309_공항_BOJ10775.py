# 공항_BOJ10775

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
G = int(input())                    # G 게이트의 수
P = int(input())                    # P 비행기의 수
airport = dict()                    # 게이트의 번호를 저장할 딕셔너리 생성
for a in range(G+1):                # 게이트의 수를 반복해서
    airport[a] = a                  # key와 value가 같은 게이트번호로 원소를 생성한다

def find(x):                        
    if airport[x] == x:             # key값과 value가 모두 같은 게이트번호라면 
        return x                    # x를 reutrn
    airport[x] = find(airport[x])   # 다르다면 x가 key일 때 value값으로 다시 find 함수를 탐색해 key값과 value가 모두 같은 게이트번호를 찾은 후 value에 저장한다
    return airport[x]               # 저장한 value 값을 return

cnt = 0                             # 공항에 도착할 수 있는 비행기의 수를 셀 변수를 만들고
for p in range(P):                  # 비행기의 수를 반복해서
    airplane = int(input())         # 비행기가 착률할 수 있는 최대 게이트 번호를 input 받는다
    x = find(airplane)              # airplane에 저장한 비행기가 착률할 수 있는 게이트번호 이하의 숫자 중 가장 큰 수를 find 함수로 찾아 x에 저장하고 
    if x == 0:                      # 착륙할 수 있는 게이트가 없다면
        break                       # 반복을 중단하고 공항을 폐쇄한다
    airport[x] = airport[x-1]       # 착륙할 수 있는 게이트가 있다면 해당게이트에 착륙하고 해당게이트에는 더이상 착륙할 수 없으므로 value를 x보다 하나 작은 게이트번호로 저장한다
    cnt += 1                        # 착륙 완료 했으므로 cnt에 1을 추가한다
print(cnt)                          # 반복문이 끝났다면 공항에 착륙한 비행기의 수를 출력한다