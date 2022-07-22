def solution(board, moves):
    stack, answer = [], 0
    board = list(zip( *board ))           # list의 행렬 반대로 전치
    arr = [[0] * len(board) for i in range(len(board))]   # 이렇게 선언해줘야 값 할당할 때 문제 안생김
    for i in range(len(board)):
        for j in range(len(board)):
            arr[i][j] = board[i][j]         # array에 list board의 값 넣어줌 -- 추후 값 변경을 위해 array를 사용

    for i in moves:    # 맨 처음 0번째는 이미 앞에서 stack에 바로 쌓아줬으니까 생략
        for j in range(len(arr[i-1])):
            if arr[i-1][j] != 0:
                if stack and stack[-1] == arr[i-1][j]:   # stack이 비어있지 않고 맨 마지막 원소가 지금 들어오는 원소랑 같다면
                    stack.pop()   # stack의 맨 마지막 캐릭터랑 같으면 stack에서 없애주고
                    answer += 1
                else:
                    stack.append(arr[i-1][j])            # stack의 맨 마지막 캐릭터랑 다르면 stack에 추가
                arr[i-1][j] = 0                            # 해당 array의 값 0으로 바꿔준다
                break

    return answer*2
  
  
  
  stack이 비었는지 확인해줘야 런타임 에러를 방지할 수 있다.
