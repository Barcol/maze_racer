import bpy

cars_rot, cars_coord = False, False


def place_obstacle(obj_x: float, obj_y: float):
    bpy.ops.mesh.primitive_cube_add(size=0.1, location=(obj_x, obj_y, 0.05))


def place_tree(obj_x: float, obj_y: float):
    bpy.ops.mesh.primitive_cube_add(size=0.1, location=(obj_x, obj_y, 0.05))


def place_plane(obj_x: float, obj_y: float):
    bpy.ops.mesh.primitive_plane_add(size=0.1, location=(obj_x, obj_y, 0.00))


with open("../maze_data/maze.txt") as file:
    for row in file:
        coords, colour = row.split()
        obj_x, obj_y = coords.split(",")
        if colour == "BLACK":
            place_obstacle(obj_x, obj_y)
        if colour == "WHITE":
            place_plane(obj_x, obj_y)
        if colour == "RED" and not cars_coord:
            cars_coord = (obj_x, obj_y)
        if colour == "GREEN":
            place_tree(obj_x, obj_y)
        if colour == "BLUE" and not cars_rot:
            cars_rot = (obj_x, obj_y)
