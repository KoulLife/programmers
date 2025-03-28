def solution(participant, completion):
    # hashSum, hashSet 생성
    hash_sum = 0
    hash_dict = {}
    
    for p in participant:
        hash_dict[hash(p)] = p
        hash_sum += hash(p)
    
    for c in completion:
        hash_sum -= hash(c)
    
    return hash_dict[hash_sum]