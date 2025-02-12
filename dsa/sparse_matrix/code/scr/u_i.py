from sparse_matrix import SpareMatrix

def main():
    print("Sparse Matrix Operations")
    
    while True:
        print("\nPlease choose an option:")
        print("1. Load Matrix A")
        print("2. Load Matrix B")
        print("3. Add Matrices")
        print("4. Subtract Matrices")
        print("5. Multiply Matrices")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            file_path = input("Enter the file path for Matrix A: ")
            global matrix_a
            try:
                matrix_a = SpareMatrix(file_path=file_path)
                print("Matrix A loaded successfully.")
                print(matrix_a)
            except Exception as e:
                print(f"Error loading Matrix A: {e}")
                
        elif choice == "2":
            file_path = input("Enter the file path for Matrix B: ")
            global matrix_b
            try:
                matrix_b = SpareMatrix(file_path=file_path)
                print("Matrix B loaded successfully.")
                print(matrix_b)
            except Exception as e:
                print(f"Error loading Matrix B: {e}")

        elif choice == "3":
            if 'matrix_a' in globals() and 'matrix_b' in globals():
                try:
                    result = matrix_a.add(matrix_b)
                    print("Addition Result:")
                    print(result)
                except Exception as e:
                    print(f"Error adding matrices: {e}")
            else:
                print("Please load both matrices first.")

        elif choice == "4":
            if 'matrix_a' in globals() and 'matrix_b' in globals():
                try:
                    result = matrix_a.subtract(matrix_b)
                    print("Subtraction Result:")
                    print(result)
                except Exception as e:
                    print(f"Error subtracting matrices: {e}")
            else:
                print("Please load both matrices first.")

        elif choice == "5":
            if 'matrix_a' in globals() and 'matrix_b' in globals():
                try:
                    result = matrix_a.multiply(matrix_b)
                    print("Multiplication Result:")
                    print(result)
                except Exception as e:
                    print(f"Error multiplying matrices: {e}")
            else:
                print("Please load both matrices first.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()