# 한수_BOJ1065

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def han(N):                                 # 한수를 찾는 함수를 돌려
    cnt = 0                                 # 한수를 저장할 변수를 생성하고
    for i in range(1, N+1):                 # 1부터 N까지 반복해서
        if i < 100:                         # 99까지는 모두 한수이므로
            cnt += 1                        # cnt에 1을 추가하고
        else:                               # 100 이상인 숫자는
            i = str(i)                      # str형태로 숫자를 변환하여
            for q in range(len(i)-2):       # 연속된 세자리 중 맨앞자리만 반복해서
                if int(i[q])-int(i[q+1]) == int(i[q+1]) - int(i[q+2]):  # 1,2번째 숫자의 차와 2,3번째 숫자의 차가 같으면
                    pass                    # 패스
                else:                       # 다르면 break 한다
                    break
            else:                           # 모두 패스했다면 한수이므로
                cnt += 1                    # cnt에 1을 추가하고
    return cnt                              # 모든 수를 탐색했다면 cnt를 리턴한다

# input 받기
N = int(sys.stdin.readline().rstrip())      # 한수를 찾을 자연수의 범위를 input 받고
print(han(N))                               # N까지 한수의 개수를 출력한다