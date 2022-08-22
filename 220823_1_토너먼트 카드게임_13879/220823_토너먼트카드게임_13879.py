# 토너먼트 카드게임_13879

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def ha(start, end):
    half = ((start + end) // 2)
    start1 = start
    end1 = half
    start2 = half
    end2 = N
    res = [start1, end1, start2, end2]
    return res

# input 받기
T = int(input())                                        # 테스트 케이스를 T에 저장
for t in range(T):                                      # 테스트 케이스를 반복할 때
    N = int(input())                                    # 카드게임의 참여자 수를 N에 저장
    card = list(map(int, input().split()))              # 참여자가 받은 카드의 숫자를 card 리스트에 저장

    half = []
    res = [1, N]

    for r in res:
        if len(res) % 2 == 0 and r % 2 == 0:
            if res[r+1]:
                pass
            elif (res[r] + res[r+1]) // 2 == 2:
                half.append((res[r] + res[r+1]) // 2)
                print(half)
                break
            else:
                print(ha(res[r] + res[r+1]))
                break

#
# def rsp(,card):
#     win1 = 0                                            # 1 그룹 승자의 인덱스를 저장할 변수
#     win2 = half                                         # 2 그룹 승자의 인덱스를 저장할 변수
#     for i in range(1, half):                            # 1그룹의 참가자를 비교할 때
#         if card[win1] == card[i]:                       # 같은 카드를 들고 있다면
#             pass                                        # 앞 순번이 승자이므로 패스
#         elif card[win1] == card[i] + 1 :                # 앞 순번의 숫자가 뒷 순번보다 하나 크면
#             pass                                        # 앞 순번이 승자이므로 패스
#         elif card[win1] == 1 and card[i] == 3:          # 앞 순번이 가위 뒷 순번이 보자기를 냈을 때
#             pass                                        # 앞 순번이 승자이므로 패스
#         elif card[win1] + 1 == card[i]:                 # 뒷 순번의 숫자가 앞 순번보다 하나 크면
#             win1 = i                                    # 뒷 순번이 승자이므로 win1을 뒷순번의 인덱스로 바꿈
#         elif card[win1] == 3 and card[i] == 1:          # 앞 순번이 보자기 뒷 순번이 가위를 냈을 때
#             win1 = i                                    # 뒷 순번이 승자이므로 win1을 뒷순번의 인덱스로 바꿈
#
#     for j in range(half + 1, N):                        # 2그룹의 참가자를 비교할 때
#         if card[win2] == card[j]:                       # 같은 카드를 들고 있다면
#             pass                                        # 앞 순번이 승자이므로 패스
#         elif card[win2] == card[j] + 1 :                # 앞 순번의 숫자가 뒷 순번보다 하나 크면
#             pass                                        # 앞 순번이 승자이므로 패스
#         elif card[win2] == 1 and card[j] == 3:          # 앞 순번이 가위 뒷 순번이 보자기를 냈을 때
#             pass                                        # 앞 순번이 승자이므로 패스
#         elif card[win2] + 1 == card[j]:                 # 뒷 순번의 숫자가 앞 순번보다 하나 크면
#             win2 = j                                    # 뒷 순번이 승자이므로 win2을 뒷순번의 인덱스로 바꿈
#         elif card[win2] == 3 and card[j] == 1:          # 앞 순번이 보자기 뒷 순번이 가위를 냈을 때
#             win2 = j                                    # 뒷 순번이 승자이므로 win2을 뒷순번의 인덱스로 바꿈
#
#     if card[win1] == card[win2]:                        # # 같은 카드를 들고 있다면
#         print(f'#{t+1}', win1 + 1)                      # 앞 순번이 승자이므로 승자의 번호를 출력
#     elif card[win1] == card[win2] + 1:                  # 앞 순번의 숫자가 뒷 순번보다 하나 크면
#         print(f'#{t+1}', win1 + 1)                      # 앞 순번이 승자이므로 승자의 번호를 출력
#     elif card[win1] == 1 and card[win2] == 3:           # 앞 순번이 가위 뒷 순번이 보자기를 냈을 때
#         print(f'#{t+1}', win1 + 1)                      # 앞 순번이 승자이므로 승자의 번호를 출력
#     elif card[win1] + 1 == card[win2]:                  # 뒷 순번의 숫자가 앞 순번보다 하나 크면
#         print(f'#{t+1}', win2 + 1)                      # 뒷 순번이 승자이므로 승자의 번호를 출력
#     elif card[win1] == 3 and card[win2] == 1:           # 앞 순번이 보자기 뒷 순번이 가위를 냈을 때
#         print(f'#{t+1}', win2 + 1)                      # 뒷 순번이 승자이므로 승자의 번호를 출력


