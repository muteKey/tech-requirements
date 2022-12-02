
class StatsMerger:
    def __init__(self, filenames: list, out_file):
        self.filenames = filenames
        self.result = {}
        self.delimeter = ": "
        self.out_file = out_file

    def process(self):
        for filename in self.filenames:
            self.process_file(filename)

    def process_file(self, filename):
        try:
            with open(filename, newline='') as file:
                lines = file.readlines()
                lines.pop(0)

                for line in lines:
                    values = line.split(self.delimeter)                
                    tech = values[0]
                    rating = int(values[1])

                    if tech in self.result:
                        self.result[tech] += rating
                    else:
                        self.result[tech] = rating
        except:
            return

    def write_result(self):
        sort_by_value_lambda = lambda value_pair: value_pair[1]
        tech = sorted(self.result.items(), key=sort_by_value_lambda, reverse=True)
        with open(self.out_file, 'w') as f:
            for key, value in tech:
                f.write('%s: %s\n' % (key, value))


            