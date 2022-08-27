# 직사각형_2527

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = 4                                               # 테스트 케이스
for t in range(T):                                  # 테스트 케이스만큼 반복할 때
    square = list(map(int, input().split()))        # 두 사각형의 꼭지점의 정보를 리스트에 저장

    X1 = square[2] - square[4]                      # 첫번째 사각형의 오른쪽 X = 두번째 사각형의 왼쪽 X
    X2 = square[6] - square[0]                      # 두번째 사각형의 오른쪽 X = 첫번째 사각형의 왼쪽 X
    Y1 = square[3] - square[5]                      # 첫번째 사각형의 오른쪽 Y = 두번째 사각형의 왼쪽 Y
    Y2 = square[7] - square[1]                      # 두번째 사각형의 오른쪽 Y = 첫번째 사각형의 왼쪽 Y

    squareXY = [X1, X2, Y1, Y2]                     # 위의 정보를 하나의 리스트로 받음

    cnt = 0                                         # 0의 개수를 셀 변수
    for l in squareXY:                              # 사각형의 영역을 비교한 것을 반복할 때
        if l < 0:                                   # 하나라도 음수가 있다면 겹치지 않으므로
            print('d')                              # d를 출력하고 break
            break
        elif l >= 0:                                # 0 이상의 수라면
            if l == 0:                              # 0일 때는 cnt에 1을 더하고 양수일 땐 패스
                cnt += 1
    else:                                           # 반복문이 종료 됐을 때
        if cnt == 1:                                # cnt가 1개이고 나머지가 모두 양수이면 사각형의 두변이 닿아 있으므로
            print('b')                              # b를 출력
        elif cnt == 2:                              # cnt가 2개이고 나머지가 모두 양수이면 한점에서 만나므로
            print('c')                              # c를 출력
        elif cnt == 0:                              # cnt가 0개이고 나머지가 모두 양수이면 두개의 사각형이 겹치므로
            print('a')                              # a를 출력