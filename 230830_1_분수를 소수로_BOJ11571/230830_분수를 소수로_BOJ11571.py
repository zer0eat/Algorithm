# 분수를 소수로_BOJ11571

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                                    # 테스트 케이스를 input 받고
for t in range(T):                                  # 테스트 케이스를 반복한다
    p, q = map(int, input().split())                # p 분자 / q 분모를 input 받고
    ans = p // q                                    # p를 q로 나눈 몫을 ans에 저장하고
    p = (p % q) * 10                                # p를 q로 나눈 나머지를 10을 곱해 p에 저장한다
    share = []                                      # 몫을 저장할 리스트를 생성하고
    remain = []                                     # 나머지를 저장할 리스트를 생성한다
    while 1:                                        # break가 나올 때까지 반복해서
        if p in remain:                             # p가 나머지 리스트에 중복되는 원소가 있다면
            idx = remain.index(p)                   # remain의 리스트에서 p의 인덱스를 가져와서 idx에 저장하고
            non_cyc = share[:idx]                   # 몫 리스트에서 idx전까지 순환하지 않는 부분으로 잘라 저장하고
            cyc = share[idx:]                       # 몫 리스트에서 idx이후로 순환하는 부분으로 잘라 저장한다
            break                                   # while문을 break 한다
        remain.append(p)                            # p가 나머지 리스트에 중복되는 것이 없다면 나머지 리스트에 p를 append
        ans2, p = divmod(p, q)                      # p를 q로 나눈 몫과 나머지를 저장해서
        share.append(ans2)                          # 몫을 share 리스트에 append 하고
        p *= 10                                     # 나머지를 10을 곱해 저장한다
    s = f"{ans}."                                   # 정답을 저장할 변수에 몫을 저장하고
    for i in non_cyc:                               # 반복되지 않는 부분을 반복해서
        s += str(i)                                 # 정답 뒤에 붙여준다
    for i in range(len(cyc)):                       # 순환되는 부분을 반복해서
        if i == 0:                                  # 순환 되는 첫 부분에는
            s += '('                                # (를 앞에 붙여주고
        s+=str(cyc[i])                              # 순환되는 부분을 붙여준다
        if i == len(cyc)-1:                         # 순환 되는 마지막 부분에는
            s += ')'                                # )를 뒤에 붙여준다
    print(s)                                        # 완성된 순환소수를 출력한다