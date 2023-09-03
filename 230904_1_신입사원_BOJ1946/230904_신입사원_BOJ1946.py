# 신입사원_BOJ1946

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                                            # 테스트 케이스를 input 받고
for t in range(T):                                          # 테스트 케이스를 반복해서
    N = int(input())                                        # 신입사원의 수를 input 받고
    new = []                                                # 신입사원을 저장할 리스트를 생성한다
    for i in range(N):                                      # 신입사원 의 수를 반복해서
        new.append(list(map(int, input().split())))         # 신입사원의 서류와 면접 점수를 input 받아 new에 append 한다
    new.sort()                                              # new를 오름차순 정렬하고
    selection = [new[0]]                                    # 선발인원을 저장할 리스트를 생성하여 서류 점수 일등을 넣는다
    for i in range(1, N):                                   # 서류 점수 2등 부터 끝까지 반복해서
        if len(selection) >= selection[0][1]:               # 합격자가 서류점수 1등의 면접 등수보다 커진다면
            break                                           # for문을 break한다
        if selection[-1][1] > new[i][1]:                    # 현재 합격자의 가장 높은 면접 등수보다 i번째 응시자의 면접 등수가 더 높다면
            selection.append(new[i])                        # 해당 응시자를 합격리스트에 append 한다
    print(len(selection))                                   # 합격 리스트의 인원을 출력한다