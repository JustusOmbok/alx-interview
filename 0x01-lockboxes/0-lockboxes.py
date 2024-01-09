#!/usr/bin/python3
'''The module for lootboxes.
'''


def canUnlockAll(boxes):
    """
    Determines if all the boxes in the given list can be unlocked.

    Args:
        boxes (list): A list of lists.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """

    # Check if the list of boxes is empty or the first box is empty
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    visited = [False] * n  # Keep track of visited boxes
    visited[0] = True  # Mark the first box as visited
    stack = [0]  # Use a stack to keep track of boxes to visit

    while stack:
        current_box = stack.pop()

        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    # Check if all boxes have been visited
    return all(visited)
