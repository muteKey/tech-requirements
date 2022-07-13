import csv

class StatsCounter:
    def __init__(self, in_file, delimeter, out_file):
        self.technologies = {}
        with open('stats/tech.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                key = row[0].lower()
                self.technologies[key] = 0
        self.texts = open(in_file, "r").read().split(delimeter)
        self.out_file = out_file

    
    def check(self):
        for text in self.texts:
            for key in self.technologies.keys():                
                if key in text.lower():
                    value = self.technologies[key]
                    self.technologies[key] = value + 1
        
    def write_results(self):
        with open(self.out_file, 'w') as f: 
            for key, value in self.technologies.items():
                if value > 0:
                    f.write('%s:%s\n' % (key, value))





    