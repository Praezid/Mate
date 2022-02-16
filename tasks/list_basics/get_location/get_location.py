def get_location(coordinates: list, commands: list) -> list:
    # write your code here
    for command in commands:
        if command == 'forward':
            coordinates = [coordinates[0],coordinates[1]+1]
        if command == 'back':
            coordinates = [coordinates[0],coordinates[1]-1]
        if command == 'right':
            coordinates = [coordinates[0]+1,coordinates[1]]
        if command == 'left':
            coordinates = [coordinates[0]-1,coordinates[1]]
    return coordinates
