# 회문2_1216_slicing 없이 풀기

# input.txt 열기
import sys
sys.stdin = open('회문2_input.txt')

# input 받기
T = 10 # 테스트 수
for t in range(T):
    N = int(input()) # 테스트 케이스
    arr = [list(input()) for _ in range(100)] # 회문이 포함된 100x100 판
    arr_reverse = [[arr[j][i] for j in range(100)] for i in range(100)]

    # 회문 찾기
    A = 100 # arr row, col의 크기
    B = 1 # 회문의 크기에 따른 한 줄에서 비교할 회문의 갯수
    C = 100 # 찾을 회문의 크기
    D = True # 회문 확인 여부
    while C > 0: # 회문의 크기가 0 이상일 때까지 반복
        for i in range(A): # 첫번째 줄부터 100번쨰 줄까지
            for b in range(B): # 한줄에서 찾을 회문의 갯수
                # 가로에서 회문을 찾았다면 D를 False로 바꾼 후 반복 중단
                find_p = []
                find_p_r = []
                for c in range(C):
                    find_p.append(arr[i][b + c])
                    find_p_r.append(arr_reverse[i][b + c])
                fp_reverse = []
                fpr_reverse = []
                for d in range(C-1, -1, -1):
                    fp_reverse.append(arr[i][b + d])
                    fpr_reverse.append(arr_reverse[i][b + d])
                else:
                    if find_p == fp_reverse:
                        D = False
                        break
                    # 세로에서 회문을 찾았다면 D를 False로 바꾼 후 반복 중단
                    elif find_p_r == fpr_reverse:
                        D = False
                        break
            if D == False:
                break
        if D == False:
            break
        # 회문을 찾지 못했다면 찾을 회문의 크기(C)를 하나 줄이고 한줄에서 찾을 회문 수(B)를 하나 늘린다.
        else:
            B += 1
            C -= 1


    print(f'#{t + 1} {C}')