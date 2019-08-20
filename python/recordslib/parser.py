from dateutil import parser

from .user import User


class LineParser:
    supported_delimiters = ('|', ",", " ")

    def parse_line(self, line_of_text):
        delimiter = [i for i in self.supported_delimiters if i in line_of_text][0]
        fields = [f.strip() for f in line_of_text.split(delimiter)]
        return User(fields[1], fields[0], fields[2], fields[3], parser.parse(fields[4]).date())

    def parse_file(self, input_file):
        for line in input_file:
            yield self.parse_line(line)
