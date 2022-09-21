# 컨테이너운반_14175

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                    # 테스트케이스
for t in range(T):                                  # 테스트케이스를 반복할 때
    N, M = map(int, input().split())                # 컨테이너 수 N / 트럭 수 M
    container = (list(map(int, input().split())))   # 컨테이너의 무게를 리스트에 저장
    truck = (list(map(int, input().split())))       # 트럭의 적재 용량을 리스트에 저장

    container.sort(reverse=True)                    # 컨테이너의 무게를 내림차순으로 정렬
    truck.sort(reverse=True)                        # 트럭의 적재용량을 내림차순으로 정렬

    ans = 0                                         # 이동한 총 무게를 저장할 변수
    while truck:                                    # truck을 모두 배차 시킬 때
        car = truck.pop(0)                          # 트럭을 배차해서 적재용량을 확인한 후
        for a in range(len(container)):             # container를 살펴보면서
            if car >= container[a]:                 # 적재용량보다 작은 짐이 나오면
                load = container.pop(a)             # 트럭에 실어 보낸다
                ans += load                         # 배달한 총 무게에 컨테이너의 무게를 더하고 반복문을 종료한다
                break
    else:                                           # while문이 끝나면 ans를 출력한다
        print(f'#{t+1}', ans)