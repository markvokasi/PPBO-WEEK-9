class F1Driver:
    TEAMS = ['Red Bull', 'Mercedes', 'McLaren', 'Ferrari']

    def __init__(self, name, team, points):
        self.name = name
        self.team = team
        self.points = points

    @property
    def rank(self):
        if self.points >= 300:
            return "Champion Contender"
        elif self.points >= 200:
            return "Top Driver"
        else:
            return "Midfield"

    @classmethod
    def show_teams(cls):
        return cls.TEAMS

    @staticmethod
    def f1_rules():
        return "F1 drivers mendapatkan 25 poin jika di posisi 1, 18 poin untuk posisi 2, dan seterusnya."

driver1 = F1Driver("Max Verstappen", "Red Bull", 310)

print(driver1.name)
print(driver1.team)
print(driver1.rank)
print(F1Driver.show_teams())
print(F1Driver.f1_rules())
