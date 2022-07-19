def solution(n, arr1, arr2):
    answer = []       
    
    for i,j in zip (arr1, arr2):
        save = []
        for a,b in zip('{:019b}'.format(i)[-n:], '{:019b}'.format(j)[-n:]):          # 19자리의 이진수로 변환하되 n자리수에 맞게 잘라서 넣어줌
            save.append('#') if (int(a) or int(b)) == 1 else save.append(' ')        # 한 원소씩 보면서 비트 연산 해줌
        answer.append(''.join(save))

    return answer
