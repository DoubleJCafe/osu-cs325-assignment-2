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
    arr1Index = 0
    arr2Index = 0
    start = 0
    arr1Length = len(arr1)
    while True:
        if arr1Index < arr1Length and arr1[arr1Index] <= arr2[arr2Index]:
            start += 1
            arr1Index += 1
            if start == k:
                return arr1[arr1Index]
        else:
            start += 1
            arr2Index += 1
            if start == k:
                return arr1[arr1Index]


