import heapq

# record_list : [0, 0, 0]
def solution(jobs):    
    record_list = [0] * len(jobs)   # 평균 값을 저장 할 리스트
            
    for i, job in enumerate(jobs): # jobs에 인덱스 넣기 jobs: 0(시간), 1(길이), 2(번호)
        job.append(i)
    heapq.heapify(jobs)
        
    work_queue = []
    process_queue = []    
    time = 0
    
    while True:                        
        if not work_queue and not process_queue and not jobs:   # 종료 조건
            break
                
        while jobs: # 디스크에 넣기
            val = heapq.heappop(jobs)
            if val[0] == time:
                # work_queue: 0(길이), 1(시간), 2(번호)
                heapq.heappush(work_queue, [val[1], val[0], val[2]])    
                record_list[val[2]] = val[0]
            else:
                heapq.heappush(jobs, val)
                break
                        
        if not process_queue:   # 디스크 투입
            if work_queue:
                process = heapq.heappop(work_queue)
                process_queue.append([process[0], process[2]])
        
        time += 1
        # process_queue: 0(시간), 1(번호)
        if process_queue:
            num, idx = process_queue.pop(0)
            num -= 1
            if num == 0:
                record_list[idx] = time - record_list[idx]
            else:
                process_queue.append([num, idx])
                
    
    return sum(record_list) // len(record_list)
        
    