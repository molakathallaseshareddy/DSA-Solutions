a = [3, 2, 4, 1]
n = len(a)
# selection sorting
for i in range(n):
  index_value = i
  for j in range(i+1,n):
    if a[index_value] < a[j]:
      a[index_value], a[j] = a[j], a[index_value]

#Bubble sorting
for i in range(n):
  for j in range(n-1):
    if a[j] < a[j+1]:
      a[j], a[j+1] = a[j+1], a[j]

#Insertion Sorting
for i in range(n-1):
  for j in range(i+1,-1,-1):
    if a[j] < a[j-1]:
      a[j], a[j-1] = a[j-1], a[j]
      
print(a)