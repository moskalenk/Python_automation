def points(games):
    count = 0

    for game in games:
        score = game.split(':')

        if score[0] > score[1]:
            count +=3
        elif score[0] == score[1]:
            count += 1

points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3'])