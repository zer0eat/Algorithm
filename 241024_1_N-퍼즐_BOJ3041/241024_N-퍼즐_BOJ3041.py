# N-퍼즐_BOJ3041

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
puzzle1 = [['A','B','C','D'],['E','F','G','H'],['I','J','K','L'],['M','N','O','.']] # 초기 퍼즐을 저장하고
puzzle2 = [list(input().strip()) for _ in range(4)]                                 # 변형된 퍼즐을 input 받고
origin = {
    'A' : [0, 0],
    'B' : [0, 1],
    'C' : [0, 2],
    'D' : [0, 3],
    'E' : [1, 0],
    'F' : [1, 1],
    'G' : [1, 2],
    'H' : [1, 3],
    'I' : [2, 0],
    'J' : [2, 1],
    'K' : [2, 2],
    'L' : [2, 3],
    'M' : [3, 0],
    'N' : [3, 1],
    'O' : [3, 2],
    '.' : [3, 3],
}                                                                                   # 퍼즐의 위치를 저장한 딕셔너리를 생성하고
ans = 0                                                                             # 정답을 저장할 변수를 생성하고
for n in range(4):                                                                  # 행을 반복하고
    for m in range(4):                                                              # 열을 반복해서
        if puzzle2[n][m] != '.' and puzzle1[n][m] != puzzle2[n][m]:                 # .이 아니고 위치가 다르다면
            tmp = origin[puzzle2[n][m]]                                             # 초기 위치를 저장하고
            ans += abs(tmp[0]-n)+abs(tmp[1]-m)                                      # 움직인 만큼 거리를 더해준다
print(ans)                                                                          # 움직인 총 거리를 출력한다