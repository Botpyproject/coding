class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        row = len(image)
        col = len(image[0])
        grid = image
        hashMap = {}
        color_To_check = grid[sr][sc]
        queue = [(sr,sc)]
        while len(queue) is not 0:
            current_node = queue.pop(0)
            try:
                x = hashMap[current_node]
            except KeyError:
                
                i = current_node[0]
                j = current_node[1]
                
                if grid[i][j] == color_To_check:
                    grid[i][j] = newColor
                    
                # check for all the neighbours of node and if they are live, put them in queue
                if i-1 in range(0,row) and j in range(0,col):
                    if grid[i-1][j] is color_To_check:
                        queue.append((i-1,j))
                        grid[i-1][j] = newColor
                        
                if i in range(0,row) and j-1 in range(0,col):
                    if grid[i][j-1] is color_To_check:
                        queue.append((i,j-1))
                        grid[i][j-1] = newColor
                        
                if i+1 in range(0,row) and j in range(0,col):
                    if grid[i+1][j] is color_To_check:
                        queue.append((i+1,j))
                        grid[i+1][j] = newColor
                        
                if i in range(0,row) and j+1 in range(0,col):
                    if grid[i][j+1] is color_To_check:
                        queue.append((i,j+1))
                        grid[i][j+1] = newColor
                        
                hashMap[(i,j)] = 1
        return grid
