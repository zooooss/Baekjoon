def solution(people, limit):
    answer = 0
    people.sort()
    min = 0
    max = len(people) - 1
    
    while min <= max:
        if people[min] + people[max] <= limit:
            min += 1
        max -= 1
        answer += 1
    return answer