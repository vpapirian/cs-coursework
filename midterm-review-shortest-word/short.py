"""
Authors: Vatche, Zack Wei, Dash
"""


def getShortStr(aStrList):
    shortest = aStrList[0]

    for i in aStrList:
        if len(i) < len(shortest):
            shortest = i
    return shortest


