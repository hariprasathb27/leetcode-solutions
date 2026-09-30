class Solution{
    int m,n;
    char[][] grid;
    Boolean[][][] memo;
    public Boolean hasValidPath(char[][] grid){
        this.grid = grid;
        m = grid.length;
        n= grid[0].length;
        memo = new Boolean[m][n][m+n+1];
        int balance = grid[0][0]=='('?1:-1;
        return dfs(0,0,balance);
    }
    private boolean dfs(int i,int j, int balance){
        if(balance <0){
            return false;
        }
        if(i==m-1&&j==n-1){
            return balance==0;
        }
        if(memo[i][j][balance] != null){
            return memo[i][j][balance];
        }
        if(i+1<m){
            int newBalance = balance+(grid[i+1][j]=='('?1:-1);
            if(dfs(i+1,j,newBalance)){
                return memo[i][j][balance] =true;
            }
        }
        if(j+1<n){
            int newBalance = balance+(grid[i][j+1]=='('?1:-1);
            if(dfs(i,j+1,newBalance)){
                return memo[i][j][balance] =true;
            }
        }
        return memo[i][j][balance]= false;
    }
}
        