#    북  동  남 서 
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0,-1]

def dfs(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    
    if data[x][y] == 1:
        return False
    elif data[x][y] == 0:
        data[x][y] = 1
        for i in range(4):
            dfs(x+dx[i],y+dy[i])
        return True



count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            count += 1
            
print(count)
