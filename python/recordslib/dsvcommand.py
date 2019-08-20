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
