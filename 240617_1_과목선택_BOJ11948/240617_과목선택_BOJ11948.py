# 과목선택_BOJ11948

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
physics = int(input())                              # 물리점수를 input 받고
chemistry = int(input())                            # 화학점수를 input 받고
biology = int(input())                              # 생물점수를 input 받고
earth_science = int(input())                        # 지구과학점수를 input 받고
history = int(input())                              # 역사점수를 input 받고
geography = int(input())                            # 지리점수를 input 받는다
A = [physics, chemistry, biology, earth_science]    # 과학 4과목을 리스트에 저장하고
A.sort(reverse=True)                                # 내림차순으로 저장해서
A.pop()                                             # 가장 낮은 점수를 제거한다
B = [history, geography]                            # 역사와 지리를 리스트에 저장하고
print(sum(A) + max(B))                              # 과학 상위 3과목과 역사, 지리 중 높은 점수의 합을 출력한다