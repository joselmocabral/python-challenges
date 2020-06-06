class Sudoku(object):
    array = []
    
    def __init__(self, data):
        self.array = data
        
    def valid_rows(self):
        valid = True
        size = len(self.array) * (len(self.array) + 1) / 2
        for i in range(0, len(self.array)):
            valid = valid and sum(self.array[i]) == size and len(list(set(self.array[i]))) == len(self.array)
        return valid
        
    def valid_cols(self):
        valid = True
        size = len(self.array) * (len(self.array) + 1) / 2
        for i in range(0, len(self.array)):
            sum_col = []
            for j in range(0, len(self.array)):
                sum_col.append(self.array[j][i])
            valid = valid and sum(sum_col) == size and len(list(set(sum_col))) == len(self.array)
        return valid
    
    def valid_box(self):
        valid = True
        size = len(self.array) * (len(self.array) + 1) / 2
        m = len(self.array)
        ran = int(len(self.array) ** 0.5)
        valid = True
        for i in range(0, ran):
            for j in range(0, ran):
                sum_box = []
                for k in range(0, ran):
                    for l in range(0, ran):
                        sum_box.append(self.array[i*ran + k][j*ran + l])
                valid = valid and size == sum(sum_box) and len(list(set(sum_box))) == len(self.array)
        return valid
        
    def is_valid(self):
        if int((len(self.array)) ** 0.5) ** 2 != len(self.array):
            return False
        if len(self.array) != len(self.array[0]):
            return False
        if len(self.array) == 0:
            return False
        for el in self.array:
            for el_2 in el:
                if not isinstance(el_2, int) or type(el_2) == bool:
                    return False
        
        return (self.valid_rows() and self.valid_cols() and self.valid_box())