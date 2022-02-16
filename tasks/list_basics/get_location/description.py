description_declare_variables = """Earlier we taught robots to understand commands and turn the direction of movement
into the right signal:
    'forward' in x + 0 and y + 1
    'back' in x + 0 and y - 1
    'right' in x + 1 and y + 0
    'left' in x - 1 and y + 0
It would be great if the robot knew where it is now, even without GPS.
Write a get_location function that takes a list of initial coordinates (as [x, y]) and a list of commands history,
and returns a list of final robot coordinates in the same format ([x, y]).
Example:
    coordinates = [2, 1]
    commands = ['left', 'back', 'back']
    
    Coordinates after the first command: [1, 1] # 1 step to the left
    Coordinates after the second team: [1, 0] # 1 step back
    Coordinates after the third team: [1, -1] # 1 step back

    The result will be [1, -1]"""
