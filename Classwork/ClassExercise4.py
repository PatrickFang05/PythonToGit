# Write a Python function that takes a list of words and
# returns the length of the longest one
# myTest = ['this', 'is', 'a', 'list', 'of', 'words']

def longestList(a):
    longestList = 0
    for i in a:
        if len(i) > longestList:
            longestList = len(i)
    return longestList

print(longestList(['this', 'is', 'a', 'list', 'of', 'words']))
