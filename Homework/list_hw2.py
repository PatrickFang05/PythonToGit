# Create a list named "l" with the following values ([1, 4, 9, 10, 23]).
# 1. Using list slicing get the sublists [4, 9] and [10, 23].
# 2. Append the value 90 to the end of the list "l".
# Check the difference between list concatenation and the "append" method.
# 3. Calculate the average value of all values on the list. You can use the "sum" and "len" functions.
# 4. Remove the sublist [4, 9].

L = ([1, 4, 9, 10, 23])
print(L[1:3])
print(L[3:5])
L.append(90)
print(sum(L) / len(L))
del L[1:3]
print(L)
