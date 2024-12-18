# src/ranging.py
import numpy as np

def split_ranges(position_array):
    """
    Splits the position array into pre-stimulus, stimulus, and post-stimulus ranges.

    Args:
        position_array (numpy.ndarray): Shape (recordings, frames, 3) containing X, Y, Z.

    Returns:
        tuple: (pre_stimulus, stimulus, post_stimulus) arrays.
    """
    pre_stimulus = position_array[:, 0:50, :]
    stimulus = position_array[:, 50:80, :]
    post_stimulus = position_array[:, 80:150, :]
    return pre_stimulus, stimulus, post_stimulus

    # src/metrics.py
def calculate_centroid(data):
    """
    Calculates the centroid (mean position) of the data.

    Args:
        data (numpy.ndarray): Shape (recordings, frames, 3) containing X, Y, Z.

    Returns:
        numpy.ndarray: Centroid as (X, Y, Z).
    """
    return np.mean(data.reshape(-1, 3), axis=0)

def calculate_path_length(data):
    """
    Calculates the total path length of the movement.

    Args:
        data (numpy.ndarray): Shape (recordings, frames, 3) containing X, Y, Z.

    Returns:
        float: Total path length.
    """
    diffs = np.diff(data, axis=1)
    distances = np.linalg.norm(diffs, axis=2)
    return np.sum(distances)

def normalize_path_length(path_length, num_frames):
    """
    Normalizes path length by the number of frames.

    Args:
        path_length (float): Total path length.
        num_frames (int): Number of frames in the range.

    Returns:
        float: Path length normalized by frames.
    """
    return path_length / num_frames