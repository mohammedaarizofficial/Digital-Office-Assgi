class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, instructions, upper_right_x, upper_right_y):
        for instruction in instructions:
            if instruction == "L":
                self.turn_left()
            elif instruction == "R":
                self.turn_right()
            elif instruction == "M":
                if self.direction == "N" and self.y < upper_right_y:
                    self.y += 1
                elif self.direction == "E" and self.x < upper_right_x:
                    self.x += 1
                elif self.direction == "S" and self.y > 0:
                    self.y -= 1
                elif self.direction == "W" and self.x > 0:
                    self.x -= 1

    def turn_left(self):
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "N"

    def turn_right(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "N"


def test_rovers():
    # Test case with plateau size 5x5 and one rover
    upper_right_x = 5
    upper_right_y = 5
    rover1 = Rover(1, 2, "N")
    rover1.move("LMLMLMLMM", upper_right_x, upper_right_y)
    assert (rover1.x, rover1.y, rover1.direction) == (1, 3, "N")

    # Test case with plateau size 5x5 and two rovers
    upper_right_x = 5
    upper_right_y = 5
    rover2 = Rover(3, 3, "E")
    rover2.move("MMRMMRMRRM", upper_right_x, upper_right_y)
    assert (rover2.x, rover2.y, rover2.direction) == (5, 1, "E")


if __name__ == "__main__":
    test_rovers()
