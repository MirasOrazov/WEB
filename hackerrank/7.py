x = int(input())

A=[]
for i in range(0,x):
    A.append(int(input()))

m = max(A)
mini = min(A)

for i in range(0, x):
    if A[i] != m:
        if mini < A[i]:
            mini = A[i]
print(mini)