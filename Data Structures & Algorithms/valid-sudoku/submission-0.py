class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validChars = set(["1","2","3","4","5","6","7","8","9"])
        def removeEmpties(arr):
            return [c for c in arr if c != "."]
        def check(arr):
            arr = removeEmpties(arr)
            if len(arr) > 9:
                return False
            
            mySet = set(arr)
            if len(mySet) != len(arr):
                return False
            
            for c in arr:
                if c not in validChars:
                    return False
            return True
        
        def transpose(arr):
            return [list(row) for row in zip(*arr)]
        
        def get_quadrant(board, quad_idx):
            # Find the starting row and column of the 3x3 block
            start_row = (quad_idx // 3) * 3
            start_col = (quad_idx % 3) * 3
            
            quadrant = []
            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    quadrant.append(board[r][c])
                    
            return quadrant
        
        def getBoxes(arr):
            return list(map(
                lambda x: get_quadrant(arr,x),[0,1,2,3,4,5,6,7,8])
            )


        # check rows
        for row in board:
            if not check(row):
                return False
        # check columns
        for col in transpose(board):
            if not check(col):
                return False
        # check sub-boxes
        for box in getBoxes(board):
            if not check(box):
                return False
        
        return True