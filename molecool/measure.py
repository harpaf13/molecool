"""
calculate.py
A Python package for analyzing and visualizing xyz files. For MolSSI Workshop Python Packag development workshop.

Calculates distance and angles from bonds
"""
import numpy as np

def calculate_distance(rA, rB):
    # This function calculates the distance between two points given as numpy arrays.
    if isinstance(rA,np.ndarray) is False or isinstance(rB,np.ndarray) is False:
        raise TypeError("rA and rB must be numpy arrays")
    dist_vec = (rA - rB)
    distance = np.linalg.norm(dist_vec)
    if distance == 0.0:
        raise Exception("Two atoms are located in the same point in space")
    return distance

def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
