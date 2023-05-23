import math

def stenopeic_hole_calculator():
    while True:
        try:
            focal_length = float(input("Enter the focal length (or 'q' to quit): "))
        except ValueError:
            break

        hole_size = round(math.sqrt(focal_length) / 31.6227766017, 3)

        print("The optimal size of the stenopeic hole is:", hole_size)

if __name__ == '__main__':
    stenopeic_hole_calculator()
    input("Press enter to exit...")
