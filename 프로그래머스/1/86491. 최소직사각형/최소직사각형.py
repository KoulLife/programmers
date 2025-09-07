def solution(sizes):
    num_b = []
    num_s = []
    
    for [s1, s2] in sizes:
        num_b.append(max(s1, s2))
        num_s.append(min(s1, s2))
    
    return (max(num_b) * max(num_s))
        