함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.



def quick(array):
    if len(array) <= 1: return array
    pivot, tail = array[0], array[1:]
    
    left = [x for x in tail if x > pivot]
    right = [x for x in tail if x <= pivot]
    
    return quick(left) + [pivot] + quick(right)

def solution(n):
    sample = []
    while(n>0):
        sample.append(n%10)
        n //= 10
        
    sample = quick(sample)
    return int(''.join(map(str, sample)))  # int형 리스트 join할 때는 map(str, array) 꼴로 해줘야함
  
  
  
  나는 n을 각 숫자로 sample에 저장해주고, 이거를 퀵소트로 정렬해주고, 다시 str으로 바꿔서 하나로 붙였는데....
  

def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))
  
  그냥 숫자를 list(str(n))하면 각각 떨어져서 저장됨
  그리고 sort를 str에 적용해도 어차피 내림차순 정렬 가능하고
  그걸 그냥 int로 붙이기만 하면 되는거였음
