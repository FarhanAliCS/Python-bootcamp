from dataclasses import dataclass

@dataclass
class Students:
    name : str
    age : int
    marks : int

    def is_passed(self) -> bool:
        return self.marks >= 50

student=Students("Farhan Ali",20,49)
result=student.is_passed()
print(result)