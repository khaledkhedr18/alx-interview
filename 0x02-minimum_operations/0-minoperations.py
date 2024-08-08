#!/usr/bin/python3
"""
Module for 0-minoperations
Contains function minOperations calculates the minimum number of operations
required to obtain exactly n 'H' characters, where each operation is either
a copy-all operation or a paste operation.
"""


def min_operations(target_length):
    """
    Calculates the minimum number of operations needed to obtain exactly
    target_length 'H' characters, where each operation is either a copy-all
    operation or a paste operation.

    Args:
        target_length (int): The target length of the resulting string.

    Returns:
        int: The minimum number of operations needed.
    """

    # If target length is less than 2, no operations are needed.
    if target_length < 2:
        return 0

    operations = 0
    current_length = 2

    # Loop through prime factors of target length, incrementing operations
    # for each factor found.
    while current_length <= target_length:
        # If target length is divisible by current length, a copy-all operation
        # followed by a paste operation is needed for each factor.
        if target_length % current_length == 0:
            operations += current_length
            target_length //= current_length
        # Increment current length to find next prime factor.
        current_length += 1

    return operations
