import math

def do_trig(hypotenuse, a_side, b_side):
        
        #sides a and b are absolute value of distance to player a is x. b is y.
        triangle_side_a = abs(a_side)
        triangle_side_b = abs(b_side)
        # triangle_side_c = math.sqrt(triangle_side_a**2 + triangle_side_b**2)

        triangle_angle_A = math.atan(triangle_side_a / triangle_side_b)
        triangle_angle_B = math.atan(triangle_side_b / triangle_side_a)

        # print(triangle_side_c)

        # print(triangle_angle_A)
        # print(triangle_angle_B)

        movement = hypotenuse

        move_triangle_side_c = movement
        #how far to move x
        move_triangle_side_a = round(move_triangle_side_c * (math.sin(triangle_angle_A)))
        #how far to move y
        move_triangle_side_b = round(move_triangle_side_c * (math.sin(triangle_angle_B)))

        return [move_triangle_side_a, move_triangle_side_b]

# #sides a and b are absolute value of distance to player a is x. b is y.
# triangle_side_a = 3
# triangle_side_b = 4
# triangle_side_c = math.sqrt(triangle_side_a**2 + triangle_side_b**2)

# triangle_angle_A = math.atan(triangle_side_a / triangle_side_b)
# triangle_angle_B = math.atan(triangle_side_b / triangle_side_a)

# # print(triangle_side_c)

# print(triangle_angle_A)
# print(triangle_angle_B)

# movement = 5

# move_triangle_side_c = movement
# move_triangle_side_a = round(move_triangle_side_c * (math.sin(triangle_angle_A)))
# move_triangle_side_b = round(move_triangle_side_c * (math.sin(triangle_angle_B)))

# print(move_triangle_side_a)
# print(move_triangle_side_b)
# print(move_triangle_side_c)