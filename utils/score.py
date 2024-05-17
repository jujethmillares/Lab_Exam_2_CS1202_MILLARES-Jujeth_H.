import os

class Score:
    def __init__(self, directory='data', filename='scores.txt'):
        self.directory = directory
        self.filename = os.path.join(directory, filename)
        self.scores = self.load_scores()

    def load_scores(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        if not os.path.exists(self.filename):
            open(self.filename, 'w').close()

        scores = {}
        with open(self.filename, 'r') as file:
            for line in file:
                username, score = line.strip().split(',')
                if username in scores:
                    scores[username].append(int(score))
                else:
                    scores[username] = [int(score)]
        return scores

    def save_scores(self):
        with open(self.filename, 'w') as file:
            for username, user_scores in self.scores.items():
                for score in user_scores:
                    file.write(f'{username},{score}\n')

    def add_score(self, username, score):
        if username in self.scores:
            self.scores[username].append(score)
        else:
            self.scores[username] = [score]
        self.save_scores()

    def get_scores(self, username):
        return self.scores.get(username, [])

    def get_average_score(self, username):
        scores = self.get_scores(username)
        if scores:
            return sum(scores) / len(scores)
        return 0