
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

sum = 0.0
for i in range(0, len(student_marks[query_name])):
    sum += student_marks[query_name][i]
sum /= len(student_marks[query_name])

print("%.2f" % sum)