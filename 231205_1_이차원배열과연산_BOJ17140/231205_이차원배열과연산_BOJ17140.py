# 이차원 배열과 연산_BOJ17140

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
R, C, K = map(int, input().split())                         # R 행의 위치 / C 열의 위치 / K R,C 위치의 원소 값을 input받고
lst = [list(map(int, input().split())) for _ in range(3)]   # 배열을 input 받는다

def R_cal():
    new = []                                                # 연산 후 배열을 저장할 리스트를 생성하고
    maxN = 0                                                # 연산 후 행의 최대 값을 저장할 변수를 생성한다
    for i in range(len(lst)):                               # lst 배열의 행을 반복하고
        tmp = dict()                                        # 한 행에 있는 원소의 개수를 세기위한 딕셔너리를 생성하고
        for j in range(len(lst[i])):                        # lst 배열의 열을 반복해서
            if lst[i][j] != 0:                              # 원소값이 0이 아니라면
                if tmp.get(lst[i][j]) == None:              # 딕셔너리에 key가 원소값일 때 저장된 값이 없다면
                    tmp[lst[i][j]] = 1                      # 해당 키의 value를 1로 저장하고
                else:                                       # 딕셔너리에 key가 원소값일 때 저장된 값이 있다면
                    tmp[lst[i][j]] += 1                     # 해당 키의 value에 1을 추가한다
        else:                                               # 한 행의 원소의 개수를 모두 셋다면
            tmp2 = []                                       # 정렬 후 정보를 저장할 리스트를 생성하고
            for t in tmp:                                   # 정렬한 딕셔너리를 반복해서
                tmp2.append([tmp[t], t])                    # tmp2에 [개수, 원소] 정보를 append한 후
            else:                                           # 딕셔너리를 모두 반복한 후에
                tmp2.sort()                                 # tmp2를 개수에 따라 오름차순으로 정렬하고
                tmp3 = []                                   # 정렬 후 행의 정보를 저장할 리스트를 생성한 후
                for t in tmp2:                              # tmp2를 반복해서
                    tmp3.append(t[1])                       # 개수에 따라 오름차순 정렬된 원소 값을 append하고
                    tmp3.append(t[0])                       # 개수에 따라 오름차순 정렬된 원소의 개수를 append한다
                else:                                       # 모든 정보를 tmp3에 append한 후
                    maxN = max(maxN, len(tmp3))             # 정렬 후 한 행의 최대길이를 maxN에 저장하고
                    new.append(tmp3)                        # new에 한 행을 append한다
    else:                                                   # 모든 행에 대해 정렬을 마쳤다면
        for n in range(len(new)):                           # 각 행을 반복해서
            new[n] += [0]*(maxN-len(new[n]))                # 가장 긴 행보다 짧은 만큼 원소 0을 추가하고
            new[n] = new[n][:100]                           # 한 행의 최대길이가 100이 되도록 슬라이싱한 후
    return new                                              # 정렬된 배열을 return한다

def C_cal():
    new = []                                                # 연산 후 배열을 저장할 리스트를 생성하고
    maxN = 0                                                # 연산 후 열의 최대 값을 저장할 변수를 생성한다
    for j in range(len(lst[0])):                            # lst 배열의 열을 반복하고
        tmp = dict()                                        # 한 열에 있는 원소의 개수를 세기위한 딕셔너리를 생성하고
        for i in range(len(lst)):                           # lst 배열의 행을 반복해서
            if lst[i][j] != 0:                              # 원소값이 0이 아니라면
                if tmp.get(lst[i][j]) == None:              # 딕셔너리에 key가 원소값일 때 저장된 값이 없다면
                    tmp[lst[i][j]] = 1                      # 해당 키의 value를 1로 저장하고
                else:                                       # 딕셔너리에 key가 원소값일 때 저장된 값이 있다면
                    tmp[lst[i][j]] += 1                     # 해당 키의 value에 1을 추가한다
        else:                                               # 한 행의 원소의 개수를 모두 셋다면
            tmp2 = []                                       # 정렬 후 정보를 저장할 리스트를 생성하고
            for t in tmp:                                   # 정렬한 딕셔너리를 반복해서
                tmp2.append([tmp[t], t])                    # tmp2에 [개수, 원소] 정보를 append한 후
            else:                                           # 딕셔너리를 모두 반복한 후에
                tmp2.sort()                                 # tmp2를 개수에 따라 오름차순으로 정렬하고
                tmp3 = []                                   # 정렬 후 열의 정보를 저장할 리스트를 생성한 후
                for t in tmp2:                              # tmp2를 반복해서
                    tmp3.append(t[1])                       # 개수에 따라 오름차순 정렬된 원소 값을 append하고
                    tmp3.append(t[0])                       # 개수에 따라 오름차순 정렬된 원소의 개수를 append한다
                else:                                       # 모든 정보를 tmp3에 append한 후
                    maxN = max(maxN, len(tmp3))             # 정렬 후 한 열의 최대길이를 maxN에 저장하고
                    new.append(tmp3)                        # new에 한 열을 append한다
    else:                                                   # 모든 열에 대해 정렬을 마쳤다면
        if maxN > 100:                                      # 한 열의 최대 길이가 100을 넘는다면
            maxN = 100                                      # 최대값을 100으로 저장하고
        new2 = [[] for _ in range(maxN)]                    # 정렬 후 배열을 저장할 리스트 안에 maxN개의 리스트를 생성한다
        length = len(new)                                   # 정렬된 열의 개수를 length에 저장하고
        if length > 100:                                    # 정렬된 열이 100개가 넘는다면
            length = 100                                    # 정렬된 열의 최대값을 100으로 저장한 후
        for n in range(length):                             # 열의 개수만큼 반복해서
            length2 = len(new[n])                           # 정렬된 행의 개수를 length2에 저장하고
            if length2 > 100:                               # 정렬된 행이 100개가 넘는다면
                length2 = 100                               # 정렬된 행의 최대값을 100으로 저장한 후
            for m in range(length2):                        # 행의 개수만큼 반복해서
                new2[m].append(new[n][m])                   # m번째 행에 정렬된 원소를 append하고
            else:                                           # 행의 최대값까지 반복을 마쳤다면
                for k in range(maxN - len(new[n])):         # maxN에서 해당 열의 최대값을 뺀 수만큼
                    new2[m+k+1].append(0)                   # 다음 행에 0을 append한다
    return new2                                             # 정렬된 배열을 return한다

cnt = 0                                                     # 연산횟수를 저장할 변수를 생성하고
while cnt < 101:                                            # 연산횟수가 100번이 될때까지 반복해서
    if R <= len(lst) and C <= len(lst[0]) and lst[R-1][C-1] == K:   # R과 C가 배열 범위 안에 있고, R, C의 원소가 K라면
        print(cnt)                                          # 연산횟수를 출력하고
        break                                               # while문을 종료한다
    else:                                                   # R,C 자리에 K가 오지 않았다면
        cnt += 1                                            # 연산횟수를 1 추가하고
        # R 연산 (행>=열)
        if len(lst) >= len(lst[0]):                         # 행이 열보다 같거나 크다면
            lst = R_cal()                                   # R연산을 수행하고
        # C 연산 (행<열)
        else:                                               # 열이 행보다 크다면
            lst = C_cal()                                   # C 연산을 수행한다
else:                                                       # 100번을 넘어도 R,C 자리에 K값이 오지 않는다면
    print(-1)                                               # -1을 출력한다