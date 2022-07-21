from functools import cmp_to_key
def compare(a,b):
    if int(str(a)+str(b)) < int(str(b)+str(a)): return 1                 # str끼리 붙인게 더 큰쪽으로 바꾸는거
    elif int(str(a)+str(b)) >= int(str(b)+str(a)): return -1

def solution(numbers):
    if max(numbers) == min(numbers) == 0: return "0"

    for i in range(len(numbers)): numbers[i] = ''.join(str(numbers[i]))  # 하나씩 '문자열'로 저장

    numbers = sorted(numbers, key=cmp_to_key(compare))                   # cmp_to_key를 import해서 쓰면 sorted할 때 커스텀한 함수를 사용할 수 있다.
    
    return ''.join(numbers)
  
  
  
  
  
  
  
  
  
  
  
  아래는 시행착오들
  
      #return str(int(hold[0]))
    #return str(int(hold[0]))[0]


    #return int(str(int(hold[0]))+str(int(hold[1])))
    #hold.sort(reverse=True, key = lambda x : ( str(int(x))[0], str(int(x))[1]))


def solution(numbers):
    hold = []
    if max(numbers) == min(numbers) == 0: return "0"
    numbers.sort()
    
    for i in range(len(numbers)): hold.append(''.join(reversed(str(numbers[i]))))  # 뒤집어서 저장

    for i in range(len(hold)):
        for j in range(i+1, len(hold)):
            if int(str(int(hold[i]))+str(int(hold[j]))) < int(str(int(hold[j]))+str(int(hold[i]))): 
                hold[i], hold[j] = hold[j], hold[i]
    
    for i in range(len(hold)): hold[i] = ''.join(reversed(str(hold[i])))   # 다시 원래 형태로 뒤집음
    return ''.join(hold)



def solution(numbers):
    hold = []
    if max(numbers) == min(numbers) == 0: return "0"
    numbers.sort()
    
    for i in range(len(numbers)): hold.append(''.join(str(numbers[i])))  # 뒤집어서 저장
    #return hold
    for i in range(len(hold)):
        for j in range(i+1, len(hold)):
            if int(str(hold[i])+str(hold[j])) < int(str(hold[j])+str(hold[i])): 
                hold[i], hold[j] = hold[j], hold[i]
    
    #for i in range(len(hold)): hold[i] = ''.join(reversed(str(hold[i])))   # 다시 원래 형태로 뒤집음
    return ''.join(hold)


from functools import cmp_to_key

def compare(a,b):
    if int(str(a)+str(b)) < int(str(b)+str(a)): return 1
    elif int(str(a)+str(b)) > int(str(b)+str(a)): return -1
    else: return 0

def solution(numbers):
    hold = []
    if max(numbers) == min(numbers) == 0: return "0"

    for i in range(len(numbers)): hold.append(''.join(str(numbers[i])))  # 하나씩 '문자열'로 저장

    hold = sorted(hold, key=cmp_to_key(compare))
    
    # for i in range(len(hold)):
    #     for j in range(i+1, len(hold)):
    #         if int(str(hold[i])+str(hold[j])) < int(str(hold[j])+str(hold[i])): 
    #             hold[i], hold[j] = hold[j], hold[i]

    return ''.join(hold)
