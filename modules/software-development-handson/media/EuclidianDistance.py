import math
import numpy as np

def euclidean_distance(point1 : list[float], point2 : list[float]) -> float:
    '''Compute the Euclidian distance between 2 points.

    Args:
        point1: a 2-elements float list
        point2: a 2-elements float list

    Return:
        float: the distance between the two points
    '''
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def pairwise_distances_basic(points : list[float]) -> list[float]:
    '''Compute distances between all points in a list.'''
    distances = []
    for i in range(len(points)):
        row = []
        for j in range(len(points)):
            if i != j:
                dist = euclidean_distance(points[i], points[j])
            else:
                dist = 0.0
            row.append(dist)
        distances.append(row)
    return distances

def pairwise_distances_numpy(points : list[float]) -> list[float]:
    '''Compute distances between all points in a list using Numpy.'''
    points_np = np.array(points)
    diff = points_np[:, np.newaxis, :] - points_np[np.newaxis, :, :]
    distances = np.sqrt(np.sum(diff**2, axis=-1))
    return distances.tolist()

def get_distances(points : list[float], method : str) -> list[float]:
    '''Interface to various backend implementation.'''
    if (method == "base"):
        return pairwise_distances_basic(points)
    elif (method == "numpy"):
        return pairwise_distances_numpy(points)
    else:
        print(f"Unknown implementation: {method}")
        exit()
