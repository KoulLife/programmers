def solution(people, limit):
    people = sorted(people)
    l = 0
    r = len(people) - 1
    two_boat = 0
    
    while l < r:
        if people[l] + people[r] <= limit:
            l += 1
            two_boat += 1
        r -= 1
    
    return len(people) - two_boat