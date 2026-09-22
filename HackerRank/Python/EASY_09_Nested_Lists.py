if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    # list of scores 
    scores = [score for name, score in records]

    # get unique scores & order them
    unique_scores = list(sorted(set(scores)))

    second_lowest_score = unique_scores[1]

    second_lowest_students = [name for name, score in records if score == second_lowest_score]

    second_lowest_students.sort()
    
    print('\n'.join(second_lowest_students))
    
