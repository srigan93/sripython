class Circle(r):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle()
r=float(input("Enter a number to calculate area :"))
print(aCircle(r))
