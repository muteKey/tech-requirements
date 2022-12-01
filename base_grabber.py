from datetime import datetime

class BaseGrabber:
    def __init__(self, in_file_name, out_file_name, delimeter):
        self.in_file = in_file_name
        self.out_file = out_file_name
        self.delimeter = delimeter

    def process(self):
        pass

    def cleanup_text(self, text):
        return text.strip().replace("● ", "").replace(" "," ").replace(" "," ").replace(" "," ").replace("• ", " ").replace(" ", "").replace("• ", "").replace("​", "")
    
    def write_results(self, descriptions):
        results = open(self.out_file, "w")
        date_time_str = "Generated at " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + "\n"

        results.writelines([date_time_str])
        results.writelines(descriptions)
        results.close()

