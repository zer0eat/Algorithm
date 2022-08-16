# 쇠막대기자르기_5432

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    laser = list(input()) # 레이저와 쇠막대기가 표시된 리스트 받기

    laser_cnt = [] # laser 리스트에서 레이저가 표시된 부분은 'z'로 막대기가 표시된 부분은 양끝이 같은 숫자로 표시
    cnt = 1 # 막대기의 양 끝을 나타내기 위한 숫자
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
            laser_cnt.append('z')
        # 쇠막대의 끝 부분은 cnt를 1 빼준 후 cnt의 숫자를 입력한다
        elif laser[l] == ')' and laser[l - 1] == ')':
            cnt -= 1
            laser_cnt.append(cnt)
    # 각각 쇠막대의 처음과 끝의 인덱스를 stick_length에 저장한다.
    stick_length = []
    for v in range(maxV + 1):
        for c in range(len(laser_cnt)):
            if laser_cnt[c] == v:
                stick_length.append(c)

    idx = 0 # 다음 쇠막대로 넘어가기 위한 인덱스 조절 숫자
    z = 0 # 쇠막대 사이에 있는 레이저의 수
    piece = 0 # 레이저로 조각난 쇠막대의 수
    # 쇠막대의 시작과 끝을 하나의 반복으로 돌리기 위한 반복
    for k in range(len(stick_length)//2):
        # 쇠막대 사이에 레이저가 있으면 z에 레이저 수를 저장
        for y in range(stick_length[k + idx], stick_length[k + idx + 1]):
            if laser_cnt[y] == 'z':
                z += 1
        # 반복이 끝나면 레이저로 조각난 쇠막대의 수를 piece에 더하고, z를 초기화 한 후 idx를 1더해준다
        else:
            piece += z/2 + 1
            z = 0
            idx += 1

    print(f'#{t+1}', int(piece))




