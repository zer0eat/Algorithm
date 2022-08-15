# 쇠막대기자르기_5432

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    laser = list(input())
    print(*laser)

    laser_cnt = []
    cnt = 0
    for l in laser:
        if l == '(':
            laser_cnt.append(cnt)
            cnt += 1
        elif l == ')':
            cnt -= 1
            laser_cnt.append(cnt)
    print(*laser_cnt)

    for c in range(len(laser_cnt)-1):
        if laser_cnt[c] == laser_cnt[c+1]:
            laser_cnt[c] = 'l'
            laser_cnt[c+1] = 'l'
            print(*laser_cnt)
        elif laser_cnt[c] != laser_cnt[c + 1]:
            pass

    print(*laser_stick)