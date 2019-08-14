import unittest
import io
from tests import datagen as dg
from recordslib import DsvCommand, LineParser


class CmdTests(unittest.TestCase):
    faker = dg.make_faker(569394833)

    def test_no_input_yields_no_output(self):
        # Using object as stdout will throw an exception if any write is attempted.
        cmd = DsvCommand([], object(), LineParser())
        cmd.run()

    def test_input_generates_many_lines(self):
        outfile = io.StringIO("")
        input_length = self.faker.random.randint(1, 51)
        inputs = [self.faker.user() for _ in range(input_length)]
        cmd = DsvCommand([str(u) + '\n' for u in inputs], outfile, LineParser())
        cmd.run()
        out_lines = outfile.getvalue().splitlines()
        line_count_assert_message = "Generated the wrong number of output lines: {} found, input: {}"
        formatted_message = line_count_assert_message.format(len(out_lines), input_length)
        self.assertEqual(input_length*3+5, len(out_lines), formatted_message)
        self.assertRegexpMatches(out_lines[2], r'\d{1,2}/\d{1,2}/\d{4}')


if __name__ == '__main__':
    unittest.main()
