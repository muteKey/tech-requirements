class BaseGrabber:
    def __init__(self, in_file_name, out_file_name, delimeter):
        self.in_file = in_file_name
        self.out_file = out_file_name
        self.delimeter = delimeter

    def process(self):
        pass
    
    def write_results(self, descriptions):
        results = open(self.out_file, "w")
        text = "".join(descriptions)

        results.write(text)
        results.close()

