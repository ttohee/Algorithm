def solution(str_list, ex):
    def check(s):
        return ex not in s
    
    filtered = list(filter(check, str_list))
    return "".join(filtered)