import unittest
import io
from tests import datagen as dg
from recordslib import DsvCommand


class CmdTests(unittest.TestCase):
    faker = dg.make_faker(569394833)

    def test_no_input_yields_no_output(self):
        # Using object as stdout will throw an exception if any write is attempted.
        cmd = DsvCommand([], object())
        cmd.run()

    def test_input_generates_many_lines(self):
        pass


if __name__ == '__main__':
    unittest.main()
