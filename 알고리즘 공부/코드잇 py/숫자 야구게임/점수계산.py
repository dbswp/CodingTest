def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0
    
    # 여기에 코드를 작성하세요
    for i in range(len(guesses)):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:
            ball_count += 1

    return strike_count, ball_count