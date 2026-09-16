rect_one_length = int(input("Enter the length of the first rectangle: "))
rect_one_width = int(input("Enter the width of the first rectangle: "))
rect_one_area = rect_one_length * rect_one_width
rect_two_width = int(input("Enter the length of the second rectangle: "))
rect_two_length = int(input("Enter the width of the second rectangle: "))
rect_two_area = rect_two_length * rect_two_width

if (rect_one_area > rect_two_area):
    print("The first rectangle has a greater area.")
elif (rect_one_area < rect_two_area):
    print("The second rectangle has a greater area.")
else:
    print("Both rectangles have the same area.")