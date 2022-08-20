import sys
sys.stdin = open('회문2_input_2.txt')

T = 10                                                              # 테스트 케이스
for t in range(T):                                                  # 테스트 케이스 만큼 반복
    case = int(input())                                             # 케이스 번호
    arr = [list(input()) for _ in range(100)]                       # 행렬을 받음

    length = 100                                                    # 검사할 회문의 길이
    long_r = 0                                                      # 찾은 회문의 길이
    find = False                                                    # 회문을 찾았는지 여부
    while find == False:                                            # 회문을 찾을 때까지 반복
        for i in range(100):                                        # 행의 수만큼 반복할 때
            if find == True:                                        # 만약 회문을 찾았다면 break
                break
            for j in range(100-length+1):                           # 회문의 시작점을 반복할 때
                for k in range(length):                             # 회문의 길이만큼 반복할 때
                    if arr[i][j+k] == arr[i][j+length-k-1]:         # 만약 앞과 뒤의 문자가 같다면 패스
                        pass
                    elif arr[i][j+k] != arr[i][j+length-k-1]:       # 다르다면 break
                        break
                else:                                               # 모두 패스해서 회문을 찾았다면
                    find = True                                     # 회문을 발견했다고 표시하고
                    long_r = length                                 # 길이를 저장하고 break
                    break
        else:                                                       # 회문을 찾지 못했다면 length를 줄여 하나 작은 회문을 찾음
            length -= 1

    length = 100                                                    # 위와 같은 방법으로 세로에서 회문을 찾음
    long_c = 0
    find = False
    while find == False:
        for i in range(100):
            if find == True:
                break
            for j in range(100-length+1):
                for k in range(length):
                    if arr[j+k][i] == arr[j+length-k-1][i]:
                        pass
                    elif arr[j+k][i] != arr[j+length-k-1][i]:
                        break
                else:
                    find = True
                    long_c = length
                    break
        else:
            length -= 1

    if long_c < long_r:                                             # 가로 회문의 최대길이와 세로 회문의 최대길이를 비교해서 큰 값을 출력
        print(f'#{t+1}', long_r)
    else:
        print(f'#{case}', long_c)