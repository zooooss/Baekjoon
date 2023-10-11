def solution(s):
    answer = ''
    answer = s[len(s)//2] if len(s) % 2 == 1 else s[len(s)//2-1]+s[len(s)//2]
    return answer