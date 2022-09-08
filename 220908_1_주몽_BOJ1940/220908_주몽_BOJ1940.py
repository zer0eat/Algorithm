# 주몽_BOJ1940

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(input())                                    # 재료의 개수
M = int(input())                                    # 갑옷을 만드는데 필요한 수
material = list(map(int, input().split()))          # 재료의 숫자를 리스트로 input

armor = 0                                           # 만들어진 갑옷을 셀 변수를 만듦
while material:                                     # material 모두 사용할 때까지
    m = material.pop(0)                             # material의 맨 앞 재료를 빼서 m에 저장
    for i in range(len(material)):                  # 남음 재료를 반복하면서
        if m + material[i] == M:                    # m과 합쳐서 M이 되는 자료를 찾는다면
            armor += 1                              # 갑옷을 하나 만들고
            material.pop(i)                         # 그 재료를 삭제한 후 반복문 종료
            break

print(armor)