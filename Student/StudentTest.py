from Student import Student
from Course import Course

std1= Student("Deema","123a")
std2= Student("Ahmed","123b")
course1= Course("Programming")
course1.enral(std1)
course1.enral(std2)
course1.getInfo()