import numpy as np
from pkg_pyknnclassifier.find_neighbors import find_neighbors
from pkg_pyknnclassifier.calculate_distance import calculate_distance

def test_find_neighbors():
    """Test for the function correctness with the toy input"""
    labeled_arrays = np.array([
        [1, 2],
        [2, 3], 
        [3, 4]
    ])
    unlabeled_array = np.array([2, 2])
    k = 2

    distances = [calculate_distance(labeled_array, unlabeled_array) for labeled_array in labeled_arrays]
    
    expected_indices = np.argsort(distances)[:k]
    
    indices = find_neighbors(labeled_arrays, unlabeled_array, k)
    
    assert np.array_equal(indices, expected_indices), f"Expected indices {expected_indices} but got {indices}"


def test_find_neighbors_invalid_k():
    """Test find_neighbors with invalid k."""
    labeled_arrays = np.array([[1, 2], [2, 3], [3, 4]])
    unlabeled_array = np.array([2, 2])
    k = 0  # Invalid k

    try:
        find_neighbors(labeled_arrays, unlabeled_array, k)
    except ValueError as e:
        assert str(e) == "k must be positive and less than or equal to the number of labeled examples."
    else:
        assert False, "Expected ValueError not raised"


def test_find_neighbors_different_dimensions():
    """Test find_neighbors with inputs of different dimensions."""
    labeled_arrays = np.array([[1, 2], [2, 3], [3, 4]])
    unlabeled_array = np.array([2, 2, 2])  # Extra dimension
    k = 2

    try:
        find_neighbors(labeled_arrays, unlabeled_array, k)
    except ValueError as e:
        assert str(e) == "labeled_arrays and unlabeled_array must have the same number of features."
    else:
        assert False, "Expected ValueError not raised"

