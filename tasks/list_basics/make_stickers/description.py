description_declare_variables = """Write a program for the make_stickers printer that takes the details_count number and
the robot_part string. The function should return a list of rows in the following format: {robot_part} detail # {n}.
If details_count = 0, return an empty list.
Examples:
    make_stickers(3, 'Body') == ['Body detail #1', 'Body detail #2', 'Body detail #3']
    make_stickers(4, 'Head') == ['Head detail #1', 'Head detail #2', 'Head detail #3', 'Head detail #4']
    make_stickers(0, 'Foot') == []"""
