scores = [85, 92, 78, 96, 88]
 #         0   1   2   3   4
# showing index and value
print(scores[1])
print(scores[1:3])
# .append() method is used to add an element to the end of the list
scores.append(90)
print(scores[5])
# .remove() method is to remove something from the list
scores.remove(92)
print(scores[1])
# now how to change index value
marks = [38, 49, 60, 39, 42, 38, 48]
marks[3-1] = 40
print(marks[2])

# list slicing 
list_1 = marks[0:2]
list_2 = marks[3:5]
list_3 = marks[4:]
print(list_1, list_2, list_3)

# .insert() is for inserting value 
marks.insert(0, 35)
print(marks[0])
# .pop is to remove something using index no.abs
print(marks[1])
marks.pop(1)
print(marks[1])

