import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        sub_boxes = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == '.':
                    continue
                
                sub_box = (i//3,j//3)
                
                if (val in row[i] or val in col[j] or val in sub_boxes[sub_box]):
                    return False 
                row[i].add(val)
                col[j].add(val)
                sub_boxes[sub_box].add(val)
        return True