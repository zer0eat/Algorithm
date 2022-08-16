# 쇠막대기자르기_5432_시간 줄이기

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    laser = list(input()) # 레이저와 쇠막대기가 표시된 리스트 받기

    laser_cnt = [] # laser 리스트에서 레이저가 표시된 부분은 'z'로 막대기가 표시된 부분은 양끝이 같은 숫자로 표시
    cnt = 0 # 막대기의 양 끝을 나타내기 위한 숫자
    maxV = 1 # 막대기가 겹치는 최대 수
    # 레이저와 쇠막대기가 표시된 리스트를 반복할 때
    for l in range(len(laser)):
        # 레이저 부분은 'z'로 표시한다
        if laser[l] == '(' and laser[l + 1] == ')':
            laser_cnt.append('z')
        # 쇠막대의 시작부분은 cnt의 숫자를 입력한 후 다음 막대를 위해 1을 더해주고, 가장 큰 수일 땐 maxV에 저장한다.
        elif laser[l] == '(' and laser[l + 1] == '(':
            laser_cnt.append(cnt)
            if cnt > maxV:
                maxV = cnt
            cnt += 1
        # 레이저 부분은 'z'로 표시한다
        elif laser[l] == ')' and laser[l - 1] == '(':
            pass
        # 쇠막대의 끝 부분은 cnt를 1 빼준 후 cnt의 숫자를 입력한다
        elif laser[l] == ')' and laser[l - 1] == ')':
            cnt -= 1
            laser_cnt.append(cnt)
    # 쇠막대기 자른 숫자 세기
    piece = 0 # 쇠막대기 조각 수
    stick = 0 # 레이저로 잘릴 쇠막대기의 수
    for c in range(len(laser_cnt)):
        # 쇠막대기가 시작되면 잘릴 조각 수와 잘린 조각수를 1씩 추가한다
        if laser_cnt[c] == stick:
            stick += 1
            piece += 1
        # 쇠막대기가 끝나면 잘릴 조각 수를 1씩 감소한다
        elif laser_cnt[c] == stick - 1:
            stick -= 1
        # laser 조사시 잘릴 수 만큼 조각 수에 추가한다.
        elif laser_cnt[c] == 'z':
            piece += stick

    print(f'#{t+1}', piece)







