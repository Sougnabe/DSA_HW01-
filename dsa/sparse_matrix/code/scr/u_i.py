import os
from sparse_matrix import SpareMatrix

def load_matrix():
    """Loads the matrix from a file specified by the user."""
    # Ask the user for the matrix file name
    file_name = input("Enter the matrix file name (e.g., matrix_a.txt): ").strip()

    # Set the relative path to the sample_inputs folder
    file_path = os.path.join('..', 'sample_inputs', file_name)

    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_name}' does not exist in the 'sample_inputs' folder.")
        return None

    # Load the matrix using the SparseMatrix class
    try:
        matrix = SpareMatrix(file_path=file_path)
        print(f"Matrix loaded from {file_path} successfully!")
        return matrix
    except ValueError as e:
        print(f"Error loading matrix: {e}")
        return None

def perform_operation(matrix_a, matrix_b):
    """Perform operations (addition, subtraction, multiplication) on the matrices."""
    print("\nSelect an operation:")
    print("1. Add matrices")
    print("2. Subtract matrices")
    print("3. Multiply matrices")
    print("4. Exit")

    choice = input("Enter the number of the operation you want to perform: ")

    if choice == '1':
        result = matrix_a.add(matrix_b)
        print("Addition result:")
        print(result.position_dict)
    elif choice == '2':
        result = matrix_a.subtract(matrix_b)
        print("Subtraction result:")
        print(result.position_dict)
    elif choice == '3':
        result = matrix_a.multiply(matrix_b)
        print("Multiplication result:")
        print(result.position_dict)
    elif choice == '4':
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please try again.")
        perform_operation(matrix_a, matrix_b)

def main():
    """Main function to interact with the user and perform matrix operations."""
    print("Welcome to the Sparse Matrix Operations Program!")

    # Load matrix A
    matrix_a = load_matrix()
    if matrix_a is None:
        return

    # Load matrix B
    matrix_b = load_matrix()
    if matrix_b is None:
        return

    # Perform operations
    perform_operation(matrix_a, matrix_b)

if __name__ == "__main__":
    main()
