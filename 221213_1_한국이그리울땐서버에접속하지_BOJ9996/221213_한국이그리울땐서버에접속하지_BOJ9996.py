# 한국이그리울땐서버에접속하지_BOJ9996

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(sys.stdin.readline())               # 테스트 케이스
ans = sys.stdin.readline().rstrip()         # 버그가 생긴 파일이름을 input 받고
for a in range(len(ans)):                   # 파일이름을 반복해서
    if ans[a] == '*':                       # * 표시가 나왔다면
        front = ans[0: a]                   # * 앞을 front로 저장하고
        back = ans[a+1: len(ans)]           # * 뒤를 back으로 저장한다

for t in range(T):                          # 테스트 케이스를 반복해서
    Q = sys.stdin.readline().rstrip()       # 파일이름을 input 받고
    if len(Q) >= len(front) + len(back):    # 파일이름이 front와 back의 합보다 같거나 클 경우에
        for f in range(len(front)):         # front를 반복해서
            if Q[f] == front[f]:            # front의 자리수와 파일이름 Q의 자리수가 일치하면
                pass                        # 패스
            else:                           # 일치하지 않으면
                print('NE')                 # NE를 출력하고
                break                       # for문을 break한다
        else:                               # 모두 일치했다면
            for b in range(len(back)):      # back를 반복해서
                if Q[len(Q)-len(back)+b] == back[b]:    # back의 자리수와 파일이름 Q의 뒤에서부터 자리수가 일치
                    pass                    # 패스
                else:                       # 일치하지 않으면
                    print('NE')             # NE를 출력하고
                    break                   # for문을 break한다
            else:                           # 모두 일치했다면
                print('DA')                 # DA를 출력한다
    else:                                   # 파일이름이 front와 back의 합보다 작으면
        print('NE')                         # NE를 출력한다