class Student:
    def __init__(self, inputID, inputFName, inputLName, inputEmail, inputMajor):
        self.student_ID = inputID
        self.first_Name = inputFName
        self.last_Name = inputLName
        self.email_ID = inputEmail
        self.major = inputMajor

    def __str__(self):
        return (str(self.student_ID) + " " + self.first_Name + " "
                + self.last_Name + " " + self.email_ID + " "
                + self.major)
