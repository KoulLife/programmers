import heapq

def solution(operations):
    arr = []
    rev_arr = []
    hash_map = {}

    for op in operations:
        com, num = op.split()
        num = int(num)

        # 넣기
        if com == 'I':
            heapq.heappush(arr, num)
            heapq.heappush(rev_arr, -num)
            hash_map[num] = hash_map.get(num, 0) + 1                  
        else:            
            if num == -1:
                while arr:
                    tmp = heapq.heappop(arr)
                    if tmp in hash_map.keys() and hash_map[tmp] > 0:
                        hash_map[tmp] -= 1
                        break
            else:
                while rev_arr:
                    tmp = heapq.heappop(rev_arr) * -1
                    if tmp in hash_map.keys() and hash_map[tmp] > 0:
                        hash_map[tmp] -= 1
                        break

    max_num = -1e9
    min_num = 1e9

    for k, v in hash_map.items():
        if v > 0:
            max_num = max(max_num, k)
            min_num = min(min_num, k)

    if max_num == -1e9:
        max_num = 0
    if min_num == 1e9:
        min_num = 0

    return [max_num, min_num]