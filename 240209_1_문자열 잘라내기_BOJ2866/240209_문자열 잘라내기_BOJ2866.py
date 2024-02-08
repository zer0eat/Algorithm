# 문자열 잘라내기_BOJ2866

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
R, C = map(int, input().split())                    # R 문자열의 수 / C 문자열의 길이를 input 받고
words = [list(input().strip()) for _ in range(R)]   # 문자열을 리스트로 input 받는다
ans = 0                                             # 정답을 저장할 변수를 생성하고
l = 0                                               # 이분탐색의 맨 앞지점을 나타내는 변수를 생성하고
r = R-1                                             # 이분탐색의 맨 뒷지점을 나타내는 변수를 생성한다
while l <= r:                                       # 맨 앞지점이 맨 뒷지점 이상이 될 때까지 반복해서
    mid = (l+r)//2                                  # 중점을 저장하고
    tmp = dict()                                    # 단어를 저장할 딕셔너리를 생성한다
    for y in range(C):                              # 단어의 길이를 반복하고
        w = ''                                      # 단어를 저장할 변수를 생성하고
        for x in range(mid, R):                     # mid 이후의 행을 반복해서
            w += words[x][y]                        # 행을 반복하며 알파벳을 더해준다
        else:                                       # 한 열의 단어가 모두 반복되었다면
            if tmp.get(w):                          # 단어가 딕셔너리에 있다면
                r = mid - 1                         # 맨 뒷지점을 앞으로 당기고
                break                               # for문을 break한다
            else:                                   # 단어가 딕셔너리에 없다면
                tmp[w] = 1                          # 딕셔너리에 단어를 추가한다
    else:                                           # 모든 단어가 중복되는 것이 없다면
        l = mid + 1                                 # 맨 앞지점을 뒤로 밀어주고
        ans = mid                                   # 지운 행의 길이를 저장한다
print(ans)                                          # 지울 수 있는 최대 행을 길이를 출력한다