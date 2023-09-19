from datetime import datetime


class Human:
    def __init__(self, name: str):
        self.name = name
        self.money = 0

    def __str__(self):
        return f'Human {self.name}'

    # def __repr__(self):
    #     return f'Human {self.name}'
    __repr__ = __str__


class SportTeam:
    def __init__(self, name: str, month_salary_one_person: int = 1000):
        self.name = name
        self.date = datetime.now()
        self.players: list[Human] = []
        self.money = 0
        self.month_salary_one_person = month_salary_one_person

    def __str__(self):
        return f'Team {self.name}'

    __repr__ = __str__

    def pay_salary(self) -> None:
        if len(self.players) * self.month_salary_one_person <= self.money:
            print('paying......')
            for player in self.players:
                player.money += self.month_salary_one_person
                self.money -= self.month_salary_one_person
        else:
            print('Not enough money')

    def fire(self, player: Human):
        self.players.remove(player)
        return self


team = SportTeam('Desna')
# team2 = SportTeam('Desna')

# print(team == team)

max = Human('Max')
team.players.append(max)

team.pay_salary()
# team2.pay_salary()
team.money += 5000
team.pay_salary()

john = Human('John')
team.players.append(john)
team.pay_salary()

# print(max)
# print(john)
# print(max)
# print(team)
# print(team.money)
# print(team.players)

print(team.money)
print(max.money)
print(john.money)

print(team.fire(max).fire(john))
# team.fire(john)
print(team.players)
