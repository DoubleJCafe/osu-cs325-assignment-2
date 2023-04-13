# Name: Joshua Jansen
# OSU Email: Jansejos@oregonstate.edu
# Course: CS325
# Assignment: 2
# Description: Function that finds the kth element after combing 2 assorted arrays.

def kthElement(arr1, arr2, k):
    """

    :param arr1:
    :param arr2:
    :param k:
    :return:
    """
    sortedArray = merg(arr1, arr2)
    return sortedArray[k - 1]


def merg(arr1, arr2):
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




