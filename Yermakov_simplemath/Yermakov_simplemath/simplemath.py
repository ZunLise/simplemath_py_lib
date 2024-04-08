class NotATriangleError(Exception):
    # what shows up when you feed wrong triangle numbers
    def __init__(self, message="this is not a triangle"):
        self.message = message
        super().__init__(self.message)


def circle_area(radius: float) -> float:
    return 3.14159265 * radius * radius


def triangle_area(side1: float, side2: float, side3: float) -> float:
    # normal triangle checks
    if min(side1, side2, side3) <= 0:
        raise NotATriangleError("one of the sides is negative or zero in length")
    if max(side1, side2, side3) > side1 + side2 + side3 - max(side1, side2, side3):
        raise NotATriangleError("one of the sides is too big")
    # certified classic formula
    else:
        perim = (side1 + side2 + side3) / 2
        return (perim * (perim - side1) * (perim - side3) * (perim - side2)) ** 0.5


def triangle_isright(side1: float, side2: float, side3: float) -> bool:
    # once again not trying to understand which side is the biggest
    return 2 * max(side1, side2, side3) ** 2 == side1 ** 2 + side2 ** 2 + side3 ** 2
