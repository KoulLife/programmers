from queue import PriorityQueue

N = int(input())
P = [0] * N

for i in range(N):
  P[i] = int(input())

pq = PriorityQueue()

for i in range(1, N):
  pq.put(-P[i])

if N == 1:
  print(0)
else:
  count = 0

  while True:
    max_val = -pq.get()
    if P[0] > max_val:
      break

    max_val -= 1
    P[0] += 1
    count += 1
    pq.put(-max_val)

  print(count)
