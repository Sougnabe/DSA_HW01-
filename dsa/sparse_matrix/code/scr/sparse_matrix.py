'''clss'''
class SpareMatrix:
    '''class'''
    def __init__(self, file_path = None, num_rows = None, num_cols = None):
        self.position_dict = {}
        if file_path:
            self.load_from_file(file_path)
        elif num_rows is not None and num_cols is not None:
            self.num_rows = num_rows
            self.num_cols = num_cols
        else:
            raise ValueError("Please provide a matrixFilePath or numRows and numCols")

    def load_from_file(self, file_path):
        '''read the 2 first lines lines to get the number of rows and columns'''
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                self.num_rows = int(f.readline().split('=')[1].strip())
                self.num_cols = int(f.readline().split('=')[1].strip())
                for line in f.readlines():
                    line = line.strip()
                    if line:
                        try:
                            row, col, value = map(int, line.strip("()").split(","))
                            self.position_dict[(row, col)] = value
                        except ValueError as exc:
                            raise ValueError("Please provide a valid matrix file") from exc
            except Exception as e:
                raise ValueError("Error reading the matrix file: {e}") from e

    def get_element(self, row, col):
        '''get the value base on his position'''
        if (row, col) not in self.position_dict:
            return 0
        return self.position_dict.get((row, col), 0)

    def set_element(self, row, col, value):
        '''set a value in a matrix with his positions'''

        if value == 0:
            self.position_dict.pop((row, col), None)
        else:
            self.position_dict[(row, col)] = value

    def add(self, other_matrix):
        '''add 2 matrices and return a new matrix'''

        if self.num_rows != other_matrix.num_rows or self.num_cols != other_matrix.num_cols:
            raise ValueError("Matrices must have the same dimensions")

        result = SpareMatrix(num_rows=self.num_rows, num_cols=self.num_cols)

        for (row, col) in other_matrix.position_dict.items():
            result.set_element(row, col, result.get_element(row, col))

        for (row, col) in self.position_dict.items():
            result.set_element(row, col, result.get_element(row, col))

        return result

    #new
    def subtract(self, other_matrix):
        '''Soustrait deux matrices creuses et retourne une nouvelle matrice creuse.'''
        if self.num_rows != other_matrix.num_rows or self.num_cols != other_matrix.num_cols:
            raise ValueError("Matrices must have the same dimensions")

        result = SpareMatrix(num_rows=self.num_rows, num_cols=self.num_cols)

        # Soustraire les éléments de la matrice actuelle
        for (row, col), value in self.position_dict.items():
            result.set_element(row, col, result.get_element(row, col) + value)

        # Soustraire les éléments de l'autre matrice
        for (row, col), value in other_matrix.position_dict.items():
            result.set_element(row, col, result.get_element(row, col) - value)

        return result

    def multiply(self, other_matrix):
        '''Multiplie deux matrices creuses et retourne une nouvelle matrice creuse.'''
        if self.num_cols != other_matrix.num_rows:
            raise ValueError("1st colunm must be  == to 2nd row")
        result = SpareMatrix(num_rows=self.num_rows, num_cols=other_matrix.num_cols)

        # Effectuer la multiplication matricielle
        for (row1, col1), value1 in self.position_dict.items():
            for (row2, col2), value2 in other_matrix.position_dict.items():
                if col1 == row2:  # Multiplication valide
                    result.set_element(row1, col2, result.get_element(row1, col2) + value1 * value2)

        return result
    