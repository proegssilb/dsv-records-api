import io
import unittest
from recordslib import LineParser
from tests.datagen import make_faker


class ParsingTests(unittest.TestCase):
    faker = make_faker(154173733)

    def test_can_parse_lines(self):
        for _ in range(50):
            user = self.faker.user()
            stringed_user = str(user)
            parser = LineParser()
            self.assertEqual(user, parser.parse_line(stringed_user))

    def test_can_switch_between_delimiters(self):
        # Because the command line version uses fileinput to abstract files vs. stdin, can't tell which delimiter is in
        # which file.
        lines = []
        users = [self.faker.user() for _ in range(50)]
        for user in users:
            delimiter = self.faker.random.choice([' | ', ', ', ' '])
            user_fields = vars(user)
            stringed_user = delimiter.join((user_fields['last_name'],
                                            user_fields['first_name'],
                                            user_fields['gender'],
                                            user_fields['favorite_color'],
                                            str(user_fields['birth_date'])
                                            ))
            lines.append(stringed_user + '\n')

        input_file = io.StringIO(''.join(lines))
        parser = LineParser()
        self.assertListEqual(users, list(parser.parse_file(input_file)))


def all_properties(obj):
    return vars(obj)


if __name__ == '__main__':
    unittest.main()
