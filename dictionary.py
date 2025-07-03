marks={
    "yash":100,
    "dhruve":70,
    "virat":54
     
}
print(marks,type(marks))
print(marks["yash"])
marks["virat"]

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"yash":100,"harry":100})
print(marks)
print(marks.get("yash"))#if we print the "yash2" then it will gives output none
print(marks["yash"])#if we print(marks["yash"])then it will gives the error
new_dict = dict.fromkeys(["x", "y"], 0)
print(new_dict)  # Output: {'x': 0, 'y': 0}
marks = marks.copy()
print(marks)
marks.clear()
print(marks)  # Output: {}
