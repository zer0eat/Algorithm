# 선형 Queue
N = 3
q = [0] * N
front = - 1
rear = - 1

#enqueue(10)
rear += 1
q[rear] = 10

#enqueue(20)
rear += 1
q[rear] = 20

#enqueue(30)
rear += 1
q[rear] = 30

#dequeue()
front += 1
print(q[front])

#dequeue()
front += 1
print(q[front])

#dequeue()
front += 1
print(q[front])


# 순환 Queue
N = 3
q = [0] * N
front = 0
rear = 0

#enqueue(10)
rear = (rear + 1) % N
q[rear] = 10

#enqueue(20)
rear = (rear + 1) % N
q[rear] = 20

#enqueue(30)
rear = (rear + 1) % N
q[rear] = 30

#enqueue(40)
rear = (rear + 1) % N
q[rear] = 40

print(q)

#dequeue()
front = (front + 1) % N
print(q[front])

#dequeue()
front = (front + 1) % N
print(q[front])

#dequeue()
front = (front + 1) % N
print(q[front])

