import csv
from datetime import datetime

class StatsCounter:
    def __init__(self, in_file, tech_file, delimeter, out_file):
        self.technologies = {}
        with open(tech_file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                key = row[0].lower()
                self.technologies[key] = 0
        self.texts = open(in_file, "r").read().strip('\n').split(delimeter)
        self.out_file = out_file

    
    def check(self):
        for text in self.texts:
            for key in self.technologies.keys():                
                if key in text.lower():
                    value = self.technologies[key]
                    self.technologies[key] = value + 1
        
    def write_results(self):
        sort_by_value_lambda = lambda value_pair: value_pair[1]
        tech = sorted(self.technologies.items(), key=sort_by_value_lambda, reverse=True)
        with open(self.out_file, 'w') as f:
            date_time_str = "Generated at " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + "\n"
            f.write(date_time_str)
            f.write(f'number of vacancies: {len(self.texts)}\n')
            for key, value in tech:
                if value > 0:
                    f.write('%s: %s\n' % (key, value))





    