""""A client program written to verify correctness of the activity 
classes.
"""

_author_ = "ACE Faculty"
_version_ = ""
_credits_ = "Beerdavinder Singh"

from shape.shape import *
from shape.triangle import Triangle
from shape.rectangle import Rectangle


def main():
    """
    Test the functionality of the methods encapsulated 
    in this project.
    """

    # In the statements coded below, ensure that any statement that 
    # could result in an exception is handled.  When exceptions are 
    # 'caught', display the exception message to the console.

    # *** PART 1 ***
    print("PART 1*")

    # 1. Create an empty list of Shape objects.
    shapes = []


    # 2. Code a statement which creates an instance of the Triangle 
    # class.
    # Append the Triangle to the list of shapes.
    try:
        triangle0 = Triangle("white", 7, 8, 9)
        shapes.append(triangle0)
    except ValueError:
        print(f"Error in creating")

    # 3. Code a statement which creates an instance of the Rectangle 
    # class.
    # Append the Rectangle to the list of shapes.
    try:
        rectangle0 = Rectangle("grey", 7, 8)
        shapes.append(rectangle0)
    except ValueError:
        print(f"Error in creating")

     # 4. Code 3 additional statements which creates an instance of 
    # Triangle or Rectangle classes (your choice).
    # Append these instances to the list of shapes.
    try:
        triangle1 = Triangle("purple", 5, 6, 7)
        shapes.append(triangle1)

        triangle2 = Triangle("green", 7, 8,10)
        shapes.append(triangle2)

        rectangle1 = Rectangle("Yellow", 5,7)
        shapes.append(rectangle1)
    except ValueError:
        print(f"Error in creating.")

    # 5. Iterate through the list of shapes.  
    # On each iteration:
    # - print the shape
    # - print the area of the shape to 2 decimal places
    # - print the perimeter of the shape to 2 decimal places
    for shape in shapes:
        try:
            print(shape)
            print(f"Area: {shape.calculate_area():.2f}cm2")
            print(f"Perimeter: {shape.calculate_perimeter():.2f} cm")
        except Exception:
            print(f"Error")
    # *** END PART 1 ***


if __name__ == "__main__":
    main()