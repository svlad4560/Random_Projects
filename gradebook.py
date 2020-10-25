ast_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]
#this is one way of adding it to the individual list
subjects.append("Computer Science")
grades.append(100)

gradebook = list(zip(grades, subjects))
# or you can add it this way
gradebook.append(('visual arts', 93))
# gradebook.zip(subjects,grades)
full_gradebook = subjects + grades
print(full_gradebook)
