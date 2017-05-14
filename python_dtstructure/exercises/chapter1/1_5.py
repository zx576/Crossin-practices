import os

class StudentRecord():

    def __init__(self,filepath):
        # with open(filename,'')
        self.filepath = filepath
        self.check()
        self.all_info = self.extract_all()


    def check(self):
        existed = os.path.exists(self.filepath)
        assert existed,'file not exists'

    def extract_all(self):
        with open(self.filepath,'r',encoding='utf-8')as f:
            data = f.read()

        return data


    def display(self):
        print(self.all_info)

    def store(self,filename='output.txt'):

        with open(filename,'w',encoding='utf-8')as f:
            f.write(self.all_info)


sr = StudentRecord('report.txt')

# sr.display()
sr.store('output.txt')
