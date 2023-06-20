matrix = [[1,2,3],[4,5,6],[7,8,9]]
i=0
j=len(matrix)-1
while i < j:
  matrix[i],matrix[j]=matrix[j],matrix[i]
  i+=1
  j-=1
print(matrix) 
for i in range(len(matrix)):
  for j in range(i):
    matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
print(matrix)