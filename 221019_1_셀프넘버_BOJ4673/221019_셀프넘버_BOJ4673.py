# 셀프넘버_BOJ4673

ans = set([i for i in range(1,10001)])  # 1부터 10000까지 있는 set을 만들고

for i in range(1,10001):                # 1부터 10000까지 반복해서
    self = i                            # self에 i를 저장하고
    a = str(i)                          # a에 i를 str 형태로 변환해서 저장
    for b in a:                         # a를 반복해서 
        self += int(b)                  # 숫자 하나하나를 self에 더한 후
    else:                               # self에 모두 더한 후
        ans -= set([self])              # 그 값을 ans에 있으면 빼준다

ans = list(ans)                         # ans를 list로 바꾸고
ans.sort()                              # 오름차순 정렬한다

for a in ans:                           # ans를 반복해서
    print(a)                            # 하나씩 출력한다