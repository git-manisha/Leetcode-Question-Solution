class Solution {
public:
    bool Traversal(vector<vector<char>>& board,int r1,int r2,int c1,int c2){
         set<char> st;
        for(int i=r1;i<=r2;i++){
            for(int j=c1;j<=c2;j++){
                if(board[i][j] == '.'){
                    continue;
                }
                if(st.find(board[i][j]) != st.end()){
                    return false;
                }
                st.insert(board[i][j]);
            }
        }
        return true;
    }
    bool isValidSudoku(vector<vector<char>>& board) {
        for(int i=0;i<board.size();i++){
            set<char> st;
            for(int j=0;j<board.size();j++){
                if(board[i][j] == '.'){
                    continue;
                }
                if(st.find(board[i][j]) != st.end()){
                    return false;
                }
                st.insert(board[i][j]);
            }
        }

        for(int i=0;i<board.size();i++){
            set<char> str;
            for(int j=0;j<board.size();j++){
                if(board[j][i] == '.'){
                    continue;
                }
                if(str.find(board[j][i]) != str.end()){
                    return false;
                }
                str.insert(board[j][i]);
            }
        }

        for(int sr=0;sr<9;sr+=3){
            int er = sr+2;
            for(int sc=0;sc<9;sc+=3){
                int ec = sc+2;
                if(Traversal(board,sr,er,sc,ec)==false){
                    return false;
                }
            }
        }

        return true;
        
    }
};