class RankingModel:
    def __init__(self):
        self.ranking = {}

    def increment(self, item):
        if item in self.ranking:
            self.ranking[item] += 1
        else:
            self.ranking[item] = 1

    def get_most_popular(self):
        if not self.ranking:
            return None
        return max(self.ranking, key=self.ranking.get)
