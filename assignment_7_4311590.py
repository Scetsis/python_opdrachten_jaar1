import collections.abc
import numpy as np

def create_coordinate_dict(ints) -> {}:
    if not isinstance(ints, collections.abc.Sequence) or not len(ints) %2 == 0:
        raise ValueError("Ints must be a sequence of an even amount of integers.")
    index = 0
    coordinates = {}
    while index < len(ints):
        coordinate = (ints[index],ints[index + 1])
        if coordinate not in coordinates:
            coordinates[coordinate] = 1
        else:
            coordinates[coordinate] = coordinates[coordinate] + 1
        index += 2
    return coordinates


def create_2D_grid(coordinates):
    countdown =
    my_array = np.array([[[coordinates]]])
    return my_array


hoi = create_coordinate_dict([4, 2, 3, 4, 4, 2, 4, 2, 3, 1])
print(hoi)
doei = create_2D_grid(hoi)
print(doei)
