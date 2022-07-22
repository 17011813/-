def solution(new_id):
    new_id = list(new_id.lower())   # 1단계
    i = 0
    while(i < len(new_id)):
        if new_id[i] != '-' and new_id[i] != '.' and new_id[i] != '_':       # 2단계
            if not (new_id[i] >= '0' and new_id[i] <= '9') and not(new_id[i] >= 'a' and new_id[i] <= 'z'):
                del new_id[i]
                i -= 1
        if i+1 < len(new_id) and new_id[i] == '.' and new_id[i+1] == '.':    # 3단계
            del new_id[i]
            i -= 1
        i += 1
        
    if len(new_id) > 0 and new_id[0] == '.': del new_id[0]       # 4단계
    if len(new_id) > 0 and new_id[-1] == '.': del new_id[-1]
    
    if not new_id:          # 5단계
        new_id.append("a")
    
    if len(new_id) >= 16: del new_id[15:]     # 6단계
    
    if new_id[-1] == '.': del new_id[-1]      # 6단계
    
    while(len(new_id) < 3):                   # 7단계
        new_id.append(new_id[-1])
    
    return ''.join(new_id)
