

class LifeGrid():

    def __init__(self,row,col):
        assert row > 0 and col > 0, 'row and col must gt zero'
        self.num_rows = row
        self.num_cols = col
        self.grid = [['d' for c in range(col)] for r in range(row)]


    def num_rows(self):
        return self.num_rows

    def num_cols(self):
        return self.num_cols

    def configure(self,*sep):
        for coo in sep:
            assert len(coo) == 2, 'a cell must be 2 elements'
            assert isinstance(coo[0],int) and isinstance(coo[1],int), 'the row and col must be integers'

            self.grid[coo[0],coo[1]] = 'a'

    def clear_grid(self):
        for row_idx in range(self.num_rows):
            for col_idx in range(self.num_cols):
                self.grid[row_idx][col_idx] = 'd'

    def clear_cell(self,row,col):
        assert 0 <= row <= self.num_rows and 0 <= col <= self.num_cols
        # assert
        self.grid[row][col] = 'd'

    def setcell(self,row,col):
        assert 0 <= row <= self.num_rows and 0 <= col <= self.num_cols
        self.grid[row][col] = 'a'

    def is_live_cell(self,row,col):
        assert 0 <= row <= self.num_rows and 0 <= col <= self.num_cols
        return self.grid[row][col] == 'a'

    def num_of_live(self,row,col):
        count_live = 0
        start_row,end_row = row-1, row+1
        if start_row < 0:
            start_row = 0
        elif end_row > self.num_rows:
            end_row = self.num_rows

        start_col, end_col = col-1, col+1
        if start_col < 0:
            start_col = 0
        elif end_col > self.num_cols:
            end_col = self.num_cols

        for row_idx in range(start_row,end_row+1):
            for col_idx in range(start_col,end_row+1):
                if self.grid[row_idx][col_idx] == 'a':
                    count_live += 1

        return count_live

    def __str__(self):
