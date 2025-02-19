# 안밖 밖안 계단 역계단_BOJ28290

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
S = input().strip()                         # 키보드를 input 받고
if S == "fdsajkl;" or S == "jkl;fdsa":      # 문자열이 안에서 밖으로 쳤다면
    print('in-out')                         # 인아웃을 출력하고
elif S == "asdf;lkj" or S == ";lkjasdf":    # 문자열이 밖에서 안으로 쳤다면면
    print('out-in')                         # 아웃인을 출력하고
elif S == "asdfjkl;":                       # 문자열을 오른쪽으로 쳤다면
    print('stairs')                         # 계단을 출력하고
elif S == ";lkjfdsa":                       # 문자열을 왼쪽으로 쳤다면
    print('reverse')                        # 반대를 출력하고
else:                                       # 모두 해당하지 않는다면
    print('molu')                           # 몰루를 출력한다