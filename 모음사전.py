from itertools import permutations, product   # product는 중복을 허용한 순열이라 여기서는 이걸 써주는게 맞다.
def solution(word):
    dic = ['A','E','I', 'O', 'U']
    save = []

    for i in range(1, 6):
        tmp = list(product(dic, repeat = i))  # product는 repeat = 인자 이렇게 넘겨줘야지만이 오류 안남!!!!
        for j in tmp:
            save.append(''.join(j))           # ''.join은 리스트 안의 요소들을 하나의 "문자열" 형태로 변환해준다.
    save.sort()
    
    return save.index(word)+1
