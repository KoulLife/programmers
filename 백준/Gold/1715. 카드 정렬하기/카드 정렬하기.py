from queue import PriorityQueue
N = int(input())
C = [0] * N

for i in range(N):
  C[i] = int(input())

pq = PriorityQueue()

for i in range(N):
  pq.put(C[i])
res = 0
while pq.qsize() > 1:
  a = pq.get()
  b = pq.get()
  res += a+b
  pq.put(a+b)

print(res)