# 리스트를 이용한 Queue
q = []

# enqueue(item)
q.append(10)
q.append(20)
q.append(30)

print(q)

#dequeue()
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

print(q)


# 덱을 이용한 Queue
from collections import deque
q = deque()

# enqueue(item)
q.append(10)
q.append(20)
q.append(30)

print(q)

#dequeue()
print(q.popleft())
print(q.popleft())
print(q.popleft())

print(q)

