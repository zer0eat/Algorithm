# 단풍잎 이야기_BOJ16457

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M, K = map(int, input().split())     # N 키의 개수 / M 퀘스트의 수 / K 퀘스트당 사용하는 스킬의 수를 input 받고
skill = set()                           # 스킬의 종류를 저장할 set을 생성한 후
quests = []                             # 퀘스트에 필요한 키를 저장할 리스트를 생성한다
for _ in range(M):                      # 퀘스트의 수를 반복해서
    A = list(map(int, input().split())) # 퀘스트에 필요한 키를 input 받고
    for a in A:                         # 필요한 키를 반복해서
        skill.add(a)                    # skill에 add한 후
    quests.append(A)                    # 퀘스트에 필요한 키 리스트를 quest에 append한다
skill = list(skill)                     # 필요한 skill이 담긴 set을 list로 변경한 후
ans = 0                                 # 정답을 저장할 변수를 생성한다

def recur(dep, start, key):
    global ans                          # ans를 global 변수로 선언하고
    if dep == N or dep == len(skill):   # dep이 키의 개수나 필요한 스킬의 수와 같아졌다면
        tmp = 0                         # 깰 수 있는 quest를 저장할 변수를 생성하고
        for quest in quests:            # 퀘스트를 반복해서
            for q in quest:             # 퀘스트별 필요한 키를 반복하고
                if q not in key:        # 해당 키가 key 리스트에 없다면
                    break               # break하고
            else:                       # 필요한 모든 키가 key 리스트에 있다면
                tmp += 1                # tmp를 1 추가한다
        ans = max(ans, tmp)             # ans와 tmp 중 더 큰 값을 저장해 최대로 깰 수 있는 퀘스트의 수를 저장한다
        return                          # return한다
    for i in range(start, len(skill)):  # start부터 키를 반복해서
        key.append(skill[i])            # i번째 키를 key에 담고
        recur(dep+1, i+1, key)          # 깊이 dep+1, i+1번 인덱스부터 key 배치를 탐색한다
        key.pop()                       # i번째 키를 pop한다

recur(0, 0, [])                         # 깊이 0, 0번 인덱스부터 key 배치를 탐색한다
print(ans)                              # 가장 최적의 키배치를 했을 때 최대로 깰 수 있는 퀘스트의 개수를 출력한다