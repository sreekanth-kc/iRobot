from operator import add


class Robot:
    """
    This is a class for handle robot movement.

    Attributes:
        input_command(string): User command.
        valid_command_list (list): Valid commands.
        robot_current_direction(string): current direction of the robot.
        robot_position(list): current position of the robot
        row(int): Number of rows in the grid.
        column(int): Number of columns in the grid.
    """
    def __init__(self, input_command,
                 valid_command_list,
                 robot_current_direction,
                 robot_position,
                 row,
                 column):
        self.input_command = input_command
        self.valid_command_list = valid_command_list
        self.robot_current_direction = robot_current_direction
        self.robot_position = robot_position
        self.row = row
        self.column = column

    def get_new_position(self):
        """
        Move the robot and return new position
        Parameters:

        Returns:
            robot_position(list): Current position of the Robot
            robot_current_direction(int): Current direction of the robot

        """
        direction = {
            "N": {"move": [-1, 0], "boundary_value": [0, '*']},
            "S": {"move": [1, 0], "boundary_value": [self.row - 1, '*']},
            "E": {"move": [0, 1], "boundary_value": ['*', self.column - 1]},
            "W": {"move": [0, -1], "boundary_value": ['*', 0]}
        }
        for command in self.input_command:
            boundary_value = direction[self.robot_current_direction]["boundary_value"].copy()  # Get the boundary value
            if command == "M":
                boundary_value[boundary_value.index("*")] = self.robot_position[boundary_value.index("*")]
                if boundary_value != self.robot_position:
                    self.robot_position = list(map(add,
                                                   self.robot_position,
                                                   direction[self.robot_current_direction]["move"]))
            else:
                self.robot_current_direction = command
        return self.robot_position, self.robot_current_direction


def move_robot():
    robot_current_position = [0, 0]     # Initial position of the robot.
    robot_current_direction = 'S'   # Initial direction of the robot
    valid_command_list = ["N", "E", "W", "S", "M"]  # List of valid command
    row = int(input("Enter the number of rows: "))
    column = int(input("Enter the number of columns: "))
    input_command = str.upper(input("Enter the command (0 to Exit): "))

    while input_command != '0':
        if set(input_command) - set(valid_command_list):    # Check for invalid commands
            print("Invalid command")
        else:
            robot_class_object = Robot(input_command,
                                       valid_command_list,
                                       robot_current_direction,
                                       robot_current_position,
                                       row,
                                       column)
            robot_current_position, robot_current_direction = robot_class_object.get_new_position()
            print("Current position : ", tuple(robot_current_position + list(robot_current_direction)))
            input_command = str.upper(input("Enter the command (0 to Exit): "))


if __name__ == '__main__':
    move_robot()
