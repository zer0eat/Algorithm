# 단어뒤집기2_BOJ17413

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
S = input()                     # S에 input 받은 문자열을 저장하고

flag = True                     # <>표시를 확인하기 위한 flag를 생성한다
answer = ''                     # 정답을 저장할 변수를 생성하고
ans = ''                        # 띄어쓰기를 고려해 임시로 저장할 변수를 생성한다
for s in S:                     # 문자열을 반복해서
    if flag == True:            # <>태그 안의 글씨가 아니라면
        if s == ' ':            # 띄어쓰기가 나왔을 때
            ans += s            # ans 뒤에 띄어쓰기를 붙여주고
            answer += ans       # answer 뒤에 붙여준다
            ans = ''            # ans를 빈 문자열로 초기화 한다
        elif s == '<':          # <가 나왔을 때
            flag = False        # flag를 False로 바꿔 <>안이라는 표시를 해주고
            if len(ans):        # ans가 빈 문자열이 아니라면
                answer += ans   # answer 뒤에 붙여준다
                ans = ''        # ans를 빈 문자열로 초기화 한다
            ans += s            # ans에 <를 저장해 준다
        else:                   # 문자열일 때
            ans = s + ans       # 문자를 뒤집어야하므로 ans 앞에 s를 붙여준다
    else:                       # <> 안의 글씨일 때
        if s == '>':            # >가 나왔을 때
            flag = True         # flag를 True로 바꿔 <>끝이라는 표시를 해주고
            ans += s            # ans 뒤에 >를 붙여주고
            answer += ans       # answer 뒤에 붙여준다
            ans = ''            # ans를 빈 문자열로 초기화 한다
        else:                   # 문자열일 때
            ans += s            # 문자를 그대로 붙여야하므로 ans 뒤에 s를 붙여준다
else:                           # 문자열을 반복을 마친 후에
    if len(ans):                # ans가 빈 문자열이 아니라면
        answer += ans           # answer 뒤에 붙여준다

print(answer)                   # 정답을 출력한다
