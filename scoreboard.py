from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    """This class is used to manage the scoreboard of the game."""
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt",encoding='utf-8') as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.update_scoreboard()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """This function updates the scoreboard of the game."""
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        """This function resets the scoreboard of the game."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w', encoding='utf-8') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """This function adds the score to the scoreboard of the game."""
        self.score += 1
        self.update_scoreboard()
