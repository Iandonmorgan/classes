import datetime

class Employee:
    def __init__(self, name):
        self.name = name
    
    def hired(self, job_title):
        self.job_title = job_title
        self.employment_start = datetime.datetime.now().strftime('%m-%d-%Y')