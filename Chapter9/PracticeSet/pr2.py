def game():
    return 6466


score = game()

with open("./PracticeSet/highscore.txt") as f:
    highscoreStr = f.read()
if highscoreStr == '':
    with open("highscore.txt", 'w') as f:
        f.write(str(score))

elif (highscoreStr) < score:
    with open("highscore.txt", "w") as f:
        f.write(str(score))
