import os

class SparseMatrix:
    '''Class to handle sparse matrices'''
    def __init__(self, file_name=None, num_rows=None, num_cols=None):
        self.position_dict = {}
        if file_name:
            self.load_from_file(file_name)
        elif num_rows is not None and num_cols is not None:
            self.num_rows = num_rows
            self.num_cols = num_cols
        else:
            raise ValueError("Please provide a file name or matrix dimensions.")

    def load_from_file(self, file_name):
        '''Reads matrix data from a file'''
        base_path = os.path.abspath("../../sample_inputs/")  # Fixed base path
        file_path = os.path.join(base_path, file_name)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                self.num_rows = int(f.readline().split('=')[1].strip())
                self.num_cols = int(f.readline().split('=')[1].strip())
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            row, col, value = map(int, line.strip("()").split(","))
                            self.position_dict[(row, col)] = value
                        except ValueError as exc:
                            raise ValueError("Invalid matrix file format.") from exc
            except Exception as e:
                raise ValueError(f"Error reading the matrix file: {e}") from e

    def get_element(self, row, col):
        '''Retrieve value at given position'''
        return self.position_dict.get((row, col), 0)

    def set_element(self, row, col, value):
        '''Set a value in the matrix'''
        if value == 0:
            self.position_dict.pop((row, col), None)
        else:
            self.position_dict[(row, col)] = value

    def add(self, other_matrix):
        '''Add two matrices'''
        if self.num_rows != other_matrix.num_rows or self.num_cols != other_matrix.num_cols:
            raise ValueError("Matrices must have the same dimensions for addition.")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)

        for (row, col), value in self.position_dict.items():
            result.set_element(row, col, value)

        for (row, col), value in other_matrix.position_dict.items():
            result.set_element(row, col, result.get_element(row, col) + value)

        return result

    def subtract(self, other_matrix):
        '''Subtract two matrices'''
        if self.num_rows != other_matrix.num_rows or self.num_cols != other_matrix.num_cols:
            raise ValueError("Matrices must have the same dimensions for subtraction.")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)

        for (row, col), value in self.position_dict.items():
            result.set_element(row, col, value)

        for (row, col), value in other_matrix.position_dict.items():
            result.set_element(row, col, result.get_element(row, col) - value)

        return result

    def multiply(self, other_matrix):
        '''Multiply two matrices'''
        if self.num_cols != other_matrix.num_rows:
            raise ValueError("Number of columns in first matrix must match number of rows in second matrix.")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=other_matrix.num_cols)

        for (row1, col1), value1 in self.position_dict.items():
            for (row2, col2), value2 in other_matrix.position_dict.items():
                if col1 == row2:  # Valid multiplication condition
                    result.set_element(row1, col2, result.get_element(row1, col2) + value1 * value2)

        return result

def main():
    '''User interface for matrix operations'''
    print("Sparse Matrix Operations")
    
    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "4":
            print("Exiting program.")
            break

        file1 = input("Enter the name of the first matrix file in sample_inputs folder (e.g., matrix_a.txt): ").strip()
        file2 = input("Enter the name of the second matrix file in sample_inputs folder (e.g., matrix_b.txt): ").strip()

        try:
            matrix1 = SparseMatrix(file1)
            matrix2 = SparseMatrix(file2)

            if choice == "1":
                result = matrix1.add(matrix2)
                print("Addition completed successfully.")
            elif choice == "2":
                result = matrix1.subtract(matrix2)
                print("Subtraction completed successfully.")
            elif choice == "3":
                result = matrix1.multiply(matrix2)
                print("Multiplication completed successfully.")
            else:
                print("Invalid choice. Please try again.")
                continue

            # Save the result
            output_file = input("Enter the output file name (e.g., result.txt): ").strip()
            base_path = os.path.abspath("../../sample_inputs/")
            output_path = os.path.join(base_path, output_file)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"rows={result.num_rows}\n")
                f.write(f"cols={result.num_cols}\n")
                for (row, col), value in result.position_dict.items():
                    f.write(f"({row}, {col}, {value})\n")

            print(f"Result saved to {output_path}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
