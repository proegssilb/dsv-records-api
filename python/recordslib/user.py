import datetime as dt


class User:
    first_name = ''
    last_name = ''
    gender = ''
    favorite_color = ''
    birth_date = dt.datetime.now()

    def __init__(self, first_name='', last_name='', gender='', favorite_color='', birth_date=dt.date.today()):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.favorite_color = favorite_color
        self.birth_date = birth_date

    def __repr__(self):
        format_string = '<User {0.first_name} {0.last_name}, {0.gender}, {0.favorite_color}, {0.birth_date}>'
        return format_string.format(self)

    def __str__(self):
        return ' | '.join((self.last_name,
                           self.first_name,
                           self.gender,
                           self.favorite_color,
                           '{dt.month}/{dt.day}/{dt:%Y}'.format(dt=self.birth_date),
                           ))

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return vars(self) == vars(other)
