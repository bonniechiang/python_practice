class Score:
    def __init__(self):
        self.score = int(input("score: "))
        if self.score >= 90:
            print('Grade is: A')
        elif self.score >= 80:
            print('Grade is: B')
        elif self.score >= 70:
            print('Grade is: C')
        elif self.score >= 60:
            print('Grade is: D')
        else:
            print('Grade is: F')
