class School_District:
    def __init__(self, name, students, revenue, schools):
        self.name = name
        self.students = students
        self.revenue = revenue
        self.schools = schools
Chappaqua = School_District('Chappaqua', 3900, 117210000, 6)
Briarcliff_Manor = School_District('Briarcliff Manor', 1600, 48541000, 3)
Scarsdale = School_District('Scarsdale', 4800, 141392000, 7)
print(Chappaqua.revenue)
