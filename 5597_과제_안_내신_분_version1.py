students = set(range(1,31))

for _ in range(28):
    students.remove(int(input()))
st = list(students)
st.sort()
for a in st:
    print(a)