import numpy as np


def shortest_vector_index(array):
    """
    Takes an array of vectors and finds the shortest one.

    :param array: array of vectors
    :return idx: the index of the shortest vector in the array
    """
    idx = np.array([np.linalg.norm(vector) for vector in array]).argmin()
    return int(idx)


def gauss_reduce(vec1, vec2, tol=1e-6):
    """
    Get the shortest vectors in the lattice generated by
    the vectors vec1 and vec2 by using the Gauss reduction method
    """
    reduced = False
    while not reduced:
        length1 = np.linalg.norm(vec1)
        length2 = np.linalg.norm(vec2)
        # First vector should be the shortest between the two
        if (length1 - length2) > tol:
            vec = vec1.copy()
            length = length1
            vec1 = vec2.copy()
            length1 = 1 * length2
            vec2 = vec.copy()
            length2 = 1 * length
        vec = vec2 - np.round(np.dot(vec1, vec2) / length1 ** 2) * vec1
        length = np.linalg.norm(vec)
        if length1 - length > tol:
            vec2 = vec1.copy()
            vec1 = vec.copy()
        else:
            vec2 = vec.copy()
            reduced = True
    return vec1, vec2
