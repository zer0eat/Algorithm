# DNA_BOJ1969

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, M = map(int, sys.stdin.readline().split())       # N DNA의 개수 / M DNA의 길이

DNA = []                                            # DNA를 담을 리스트를 생성하고
for _ in range(N):                                  # N개의 DNA를 반복해서
    DNA.append(sys.stdin.readline().strip())        # DNA 리스트에 append

ans = ''                                            # DNA의 염기서열을 저장할 변수
cnt = 0                                             # Hamming Distance의 합을 저장할 변수
for m in range(M):                                  # DNA의 길이를 반복하고
    nucleotides = [0, 0, 0, 0]                      # A, C, G, T 가 나올때마다 각 인덱스에 개수를 추가
    for n in range(N):                              # DNA의 개수를 반복해서
        if DNA[n][m] == 'A':                        # A가 나왔다면
            nucleotides[0] += 1                     # nucleotides의 0번째 인덱스에 1을 더한다
        elif DNA[n][m] == 'C':                      # C가 나왔다면
            nucleotides[1] += 1                     # nucleotides의 1번째 인덱스에 1을 더한다
        elif DNA[n][m] == 'G':                      # G가 나왔다면
            nucleotides[2] += 1                     # nucleotides의 2번째 인덱스에 1을 더한다
        elif DNA[n][m] == 'T':                      # T가 나왔다면
            nucleotides[3] += 1                     # nucleotides의 3번째 인덱스에 1을 더한다
    else:                                           # 한줄을 모두 확인했으면
        Q = max(nucleotides)                        # 가장 많은 숫자의 개수를 Q에 저장하고
        if nucleotides.index(Q) == 0:               # 가장많은 개수의 인덱스가 0이라면
            ans += 'A'                              # ans에 A를 더하고
            cnt += (N - Q)                          # Hamming Distance를 N - Q개 더한다
        elif nucleotides.index(Q) == 1:             # 가장많은 개수의 인덱스가 1이라면
            ans += 'C'                              # ans에 C를 더하고
            cnt += (N - Q)                          # Hamming Distance를 N - Q개 더한다
        elif nucleotides.index(Q) == 2:             # 가장많은 개수의 인덱스가 2이라면
            ans += 'G'                              # ans에 G를 더하고
            cnt += (N - Q)                          # Hamming Distance를 N - Q개 더한다
        elif nucleotides.index(Q) == 3:             # 가장많은 개수의 인덱스가 3이라면
            ans += 'T'                              # ans에 T를 더하고
            cnt += (N - Q)                          # Hamming Distance를 N - Q개 더한다

print(ans)                                          # DNA를 출력
print(cnt)                                          # Hamming Distance의 합 출력

