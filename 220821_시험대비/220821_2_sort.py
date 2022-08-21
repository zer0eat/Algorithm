A = [5,4,9,7,8,6,2,1,3,0]

# bubble sort
for i in range(len(A)):
    for j in range(len(A)-i):
        if A[i] > A[i + j]:
            A[i], A[i + j] = A[i + j], A[i]

print(A)

B = [0,4,1,3,1,2,4,1]

# counting sort
maxB = 0
for b in B:
    if b > maxB:
        maxB = b

cnt = [0] * (maxB+1)
cnt_sum = [0] * (maxB+1)
for b in B:
    cnt[b] += 1
for c in range(len(cnt)):
    cnt_sum[c] = cnt[c] + cnt_sum[c-1]


cnt_new = [0] * len(B)
for d in range(len(B)-1, -1, -1):
    cnt_new[cnt_sum[B[d]]-1] = B[d]
    cnt_sum[B[d]] -= 1

print(cnt_new)

