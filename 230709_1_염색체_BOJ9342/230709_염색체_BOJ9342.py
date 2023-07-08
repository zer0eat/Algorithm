# 염색체_BOJ9342

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                                            # 테스트 케이스
DNA = ['A', 'B', 'C', 'D', 'E', 'F']                        # 특정 패턴의 문자열을 저장한 리스트 생성
for t in range(T):                                          # 테스트 케이스를 반복해서
    chromosome = input().strip()                            # 염색체의 문자열을 input 받는다
    need = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0}       # 염색체의 문자열을 셀 딕셔너리를 생성한 후
    for c in range(len(chromosome)):                        # 염색체의 길이를 반복해서
        if chromosome[c] in DNA:                            # 염색체의 문자열이 DNA에 포함된 문자열일 경우
            if chromosome[c] == 'F':                        # 문자열이 F인 경우에는
                if need['A'] == 0:                          # A가 나오기 전에 F가 나왔다면
                    print('Good')                           # 규칙을 만족하지 않으므로 Good을 출력하고
                    break                                   # for문을 break
                else:                                       # A가 나온 후 F가 나왔다면
                    need[chromosome[c]] += 1                # F가 key인 value에 1을 추가한다
            elif chromosome[c] == 'C':                      # 문자열이 C인 경우에는
                if need['F'] == 0:                          # F가 나오기 전에 C가 나왔다면
                    print('Good')                           # 규칙을 만족하지 않으므로 Good을 출력하고
                    break                                   # for문을 break
                else:                                       # F가 나온 후 C가 나왔다면
                    need[chromosome[c]] += 1                # C가 key인 value에 1을 추가한다
            else:                                           # 문자열이 F와 C가 아닌 경우에는
                need[chromosome[c]] += 1                    # chromosome[c]가 key인 value에 1을 추가한다
        else:                                               # 염색체의 문자열이 DNA에 포함되지 않을 경우
            print('Good')                                   # 규칙을 만족하지 않으므로 Good을 출력하고
            break                                           # for문을 break
    else:                                                   # chromosome의 모든 문자열이 DNA에 포함된 문자열일 경우
        for n in need:                                      # need에 저장한 딕셔너리를 반복해서
            if n == 'A' or n == 'F' or n == 'C':            # key가 A, F, C인 경우에
                if need[n] >= 1:                            # 그 밸류가 1이상인 경우에는 
                    pass                                    # pass
                else:                                       # 0인 경우에는
                    print('Good')                           # 규칙을 만족하지 않으므로 Good을 출력하고
                    break                                   # for문을 break
            else:                                           # key가 B, D, E인 경우에
                if need[n] <= 1:                            # 그 밸류가 1이하인 경우에는
                    pass                                    # pass
                else:                                       # 2이상인 경우에는
                    print('Good')                           # 규칙을 만족하지 않으므로 Good을 출력하고
                    break                                   # for문을 break
        else:                                               # need의 모든 반복을 마쳤다면 조건을 만족하므로
            print('Infected!')                              # Infected!를 출력한다