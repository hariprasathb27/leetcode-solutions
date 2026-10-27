class Solution {
    public int closedIsland(int[][] grid) {
    int row = grid.length, col = grid[0].length;
        for(int i=0;i<row;i++){
            dfs(grid,i,0);
            dfs(grid,i,col-1);
        }
        for(int i=0;i<col;i++){
            dfs(grid,0,i);
            dfs(grid,row-1,i);
        }
        int count =0;
        for(int i=1;i<row;i++){
            for(int j=1;j<col-1;j++){
                if(grid[i][j]==0){
                    count++;
                    dfs(grid,i,j);
                }
            }
        }
        return count;
    }
    private void dfs(int[][] grid, int i, int j){
        if(i<0 || j<0 || i>=grid.length || j>=grid[0].length || grid[i][j]==1){
            return;
        }
        grid[i][j]=1;
        dfs(grid,i+1,j);
        dfs(grid,i-1,j);
        dfs(grid,i,j+1);
        dfs(grid,i,j-1);
    }    
    
}