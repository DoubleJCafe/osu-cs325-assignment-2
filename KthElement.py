# Name: Joshua Jansen
# OSU Email: Jansejos@oregonstate.edu
# Course: CS325
# Assignment: 2
# Description: Function that finds the kth element after combing 2 assorted arrays.

def kthElement(arr1, arr2, k):
    """
    Finds the element of a sorted list.

    :param arr1: Sorted list
    :param arr2: Sorted list
    :param k: Index postion of the element wanted when the list are combined in sorted order.
    :return: Element stored at param k.
    """
    sortedArray = merg(arr1, arr2)
    return sortedArray[k - 1]


def merg(arr1, arr2):
    """
    Takes 2 sorted lists and merges them together.
    :param arr1: Sorted list
    :param arr2: Sorted list
    :return: List of the 2 given list combined in sorted order.
    """
    sortedArray = []
    arr1Index = 0
    arr2Index = 0

    while arr1Index < len(arr1) and arr2Index < len(arr2):
        if arr1[arr1Index] < arr2[arr2Index]:
            sortedArray.append(arr1[arr1Index])
            arr1Index += 1
        else:
            sortedArray.append(arr2[arr2Index])
            arr2Index += 1

    while arr1Index < len(arr1):
        sortedArray.append(arr1[arr1Index])
        arr1Index += 1

    while arr2Index < len(arr2):
        sortedArray.append(arr2[arr2Index])
        arr2Index += 1
    return sortedArray




