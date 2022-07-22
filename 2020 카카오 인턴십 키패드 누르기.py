def solution(numbers, hand):
    dic = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], '*':[3,0], 0:[3,1], '#':[3,2]}
    answer, l_hand, r_hand = "", dic['*'], dic['#']
    for i in numbers:
        if i==1 or i==4 or i==7:
            answer += 'L'
            l_hand = dic[i]
        elif i==3 or i==6 or i==9:
            answer += 'R'
            r_hand = dic[i]
        else:
            if abs(l_hand[0] - dic[i][0]) + abs(l_hand[1] - dic[i][1]) < abs(r_hand[0] - dic[i][0]) + abs(r_hand[1] - dic[i][1]):
                answer += 'L'
                l_hand = dic[i]
            elif abs(l_hand[0] - dic[i][0]) + abs(l_hand[1] - dic[i][1]) > abs(r_hand[0] - dic[i][0]) + abs(r_hand[1] - dic[i][1]):
                answer += 'R'
                r_hand = dic[i]
            else:
                if hand[0] == 'l':
                    answer += 'L'
                    l_hand = dic[i]
                if hand[0] == 'r':
                    answer += 'R'
                    r_hand = dic[i]
    return answer
