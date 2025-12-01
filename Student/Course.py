class Course:

    student=[] #static variable

    def __init__(self,title):
        self.title=title

    def enral(self,std):
        self.student.append(std)
    
    @staticmethod  # ما فيها self
    def getInfo():
        for std in Course.student:
            print(std.getInfo())
