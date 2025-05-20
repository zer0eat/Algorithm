# 특별한 학교 이름 암호화_BOJ27891

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
school = input().strip()                    # 암호화된 학교 이름을 input받고
name = ['North London Collegiate School',
    'Branksome Hall Asia',
    'Korea International School',
    'St. Johnsbury Academy'
]                                           # 학교 이름을 리스트로 생성해서
ans = ['NLCS', 'BHA', 'KIS', 'SJA']         # 학교의 약어를 리스트로 생성하고
ans2 = []                                   # 암호화된 학교 코드를 저장할 리스트를 생성한다
for n in name:                              # 학교이름을 반복해서
    tmp = ''                                # 변수를 생성하고
    for c in n:                             # 학교이름의 스펠링을 반복해서
        if len(tmp) == 10:                  # 10자가 넘어가면
            break                           # for문을 break한다
        if not c.isalpha():                 # 학교 스펠링이 알파벳이 아니라면
            continue                        # 넘어가고
        if c.isupper():                     # 학교 스펠링이 대문자라면
            tmp += c.lower()                # 소문자로 변경해서 저장하고
            continue                        # 넘어가고
        tmp += c                            # 소문자라면 바로 저장한다
    ans2.append(tmp)                        # 암호화된 이름을 ans2 리스트에 저장한다
for i in range(26):                         # 알파벳의 수를 반복해서
    tmp = ''                                # 저장할 변수를 생성하고
    for s in school:                        # input 받은 이름을 반복해서
        next = ord(s) + i                   # 스펠링의 다음 글자로 바꾸고
        if ord('z') < next:                 # z를 넘어간다면
            next = (next % ord('z')) + ord('a') - 1 # a로 돌아와서 다시 올라간다
        tmp += chr(next)                    # 변경된 문자를 저장하고
    for a in range(4):                      # 암호화된 학교이름을 반복해서
        if ans2[a] == tmp:                  # 암호화된 학교이름을 찾았다면
            print(ans[a])                   # 약어를 출력하고
            quit()                          # 종료한다