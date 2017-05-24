class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def Main():
    vec = Vector2D(5,7)
    print "x: " + str(vec.x) + " y: " + str(vec.y)

if __name__ == "__main__":
           
           Main()
