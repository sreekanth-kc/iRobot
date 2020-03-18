from robot import Robot
robot_position = [0, 0]
robot_current_direction = 'S'
valid_command_list = ["N", "E", "W", "S", "M"]
row = 5
column = 5


test_cases = [
    {"input_command": "MMMM", "output_position": [4, 0], "output_direction": 'S'},
    {"input_command": "MEMMM", "output_position": [1, 3], "output_direction": 'E'},
    {"input_command": "EMMMMSMMMM", "output_position": [4, 4], "output_direction": 'S'},
    {"input_command": "MMEMMMMMMM", "output_position": [2, 4], "output_direction": 'E'},
    {"input_command": "WMMSMMEMMSMMWM", "output_position": [4, 1], "output_direction": 'W'},
    {"input_command": "WMM", "output_position": [0, 0], "output_direction": 'W'},
    {"input_command": "EMSMEMMMMM", "output_position": [1, 4], "output_direction": 'E'},
    {"input_command": "WMM", "output_position": [0, 0], "output_direction": 'W'},
    {"input_command": "M", "output_position": [1, 0], "output_direction": 'S'},
    {"input_command": "MMMMMWMMMEM", "output_position": [4, 1], "output_direction": 'E'}
]


class TestRobot:
    def test_get_new_position(self):
        for test_case in test_cases:
            robot_obj = Robot(test_case["input_command"],
                              valid_command_list,
                              robot_current_direction,
                              robot_position,
                              row,
                              column)
            out_put_position, out_put_direction = robot_obj.get_new_position()
            assert out_put_direction == test_case["output_direction"]
            assert out_put_position == test_case["output_position"]
