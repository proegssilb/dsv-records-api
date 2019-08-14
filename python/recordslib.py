import datetime as dt
from dateutil import parser


class DsvCommand:
    def __init__(self, lines_in, output_stream, line_parser):
        self.lines_in = lines_in
        self.output_stream = output_stream
        self.parser = line_parser

    def run(self):
        # This is not how this should work in production code.
        lines_buffer = [self.parser.parse_line(i) for i in self.lines_in]

        if len(lines_buffer) == 0:
            # Don't generate output.
            return

        self.run_sort(lines_buffer, "Sorted by gender and last name:", lambda u: (u.gender, u.last_name))
        print('', file=self.output_stream)
        self.run_sort(lines_buffer, "Sorted by birthday:", lambda u: u.birth_date)
        print('', file=self.output_stream)
        self.run_sort(lines_buffer, "Sorted by last name:", lambda u: u.last_name, True)

    def run_sort(self, lines_buffer, header, sort_func, reverse=False):
        print(header, file=self.output_stream)
        for line in sorted(lines_buffer, key=sort_func, reverse=reverse):
            print(line, file=self.output_stream)


class LineParser:
    supported_delimiters = ('|', ",", " ")

    def parse_line(self, line_of_text):
        delimiter = [i for i in self.supported_delimiters if i in line_of_text][0]
        fields = [f.strip() for f in line_of_text.split(delimiter)]
        return User(fields[1], fields[0], fields[2], fields[3], parser.parse(fields[4]).date())

    def parse_file(self, input_file):
        for line in input_file:
            yield self.parse_line(line)


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
