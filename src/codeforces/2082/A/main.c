/*
 * -------------------------------------------------------
 * LINK: https://codeforces.com/problemset/problem/2082/A
 * TIME-START: March-21-2025 10:15 AM
 * TIME-END:   March-21-2025 10:15 AM
 * AUTHOR: smpl
 * -------------------------------------------------------
 */

/*
 TODO:
 - performing XOR oparations
 - Main algorithm: minimizing swaps to make matrix good
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

#define MAX_BUFF_SIZE 1024
u_int8_t matrix[MAX_BUFF_SIZE][MAX_BUFF_SIZE] = { 0 };

// FORWARD DECLARATIONS
void my_algorithm(int rows, int cols);
void print_matrix_xor_results(int rows, int cols);

int main() {
  int total_tests = -1;
  FILE* file = fopen("input.txt", "r");
  if (file == NULL) {
    perror("Error opening file");
    return 1;
  }

  char buff[MAX_BUFF_SIZE];

  // Read number of tests
  if (fgets(buff, sizeof(buff), file)) {
    sscanf(buff, "%d", &total_tests);
    printf("Total tests: %d\n", total_tests);
  }

  // Process each test case
  for (int test = 0; test < total_tests; test++) {
    int rows, cols;

    // Read matrix dimensions
    if (fgets(buff, sizeof(buff), file)) {
      sscanf(buff, "%d %d", &rows, &cols);
      printf("\nTest #%d\n", test + 1);
      printf("ROWS: %d COLS: %d\n", rows, cols);
    }

    // Allocate matrix

    // Read matrix data
    for (int i = 0; i < rows; i++) {
      if (fgets(buff, sizeof(buff), file)) {
        // Remove newline if present
        size_t len = strlen(buff);
        if (len > 0 && buff[len - 1] == '\n') {
          buff[len - 1] = '\0';
        }

        // Read the digits from the row and convert them to integers
        for (int j = 0; j < cols; j++) {
          if (j < strlen(buff) && buff[j] >= '0' && buff[j] <= '9') {
            int num = buff[j] - '0';
            matrix[i][j] = num;
          }
        }
      }
    }

    // Apply your algorithm
    print_matrix_xor_results(rows, cols);
    // my_algorithm(rows, cols);
  }

  fclose(file);
  return 0;
}

void my_algorithm(int rows, int cols) {
  // Example algorithm: Print the matrix
  printf("Matrix:\n");
  for (int i = 0; i < rows; i++) {
    // Check if row is good
    for (int j = 0; j < cols; j++) {
      printf("%d ", matrix[i][j]);
    }
    printf("\n");
  }
}

#include <stdint.h>
#include <stdio.h>

int find_min(int matrix[MAX_BUFF_SIZE][MAX_BUFF_SIZE], int rows, int cols) {

  // base condition
  if get_xor () {
  }

  find_min(matrix, 10, 20);

  return -1;
}

void calculate_matrix_xor(int rows, int cols, uint8_t row_xor[MAX_BUFF_SIZE],
                          uint8_t col_xor[MAX_BUFF_SIZE]) {
  // Calculate XOR for each row
  for (int i = 0; i < rows; i++) {
    row_xor[i] = 0; // Initialize to 0 (identity element for XOR)
    for (int j = 0; j < cols; j++) {
      row_xor[i] ^= matrix[i][j]; // XOR each element in the row
    }
  }

  // Calculate XOR for each column
  for (int j = 0; j < cols; j++) {
    col_xor[j] = 0; // Initialize to 0 (identity element for XOR)
    for (int i = 0; i < rows; i++) {
      col_xor[j] ^= matrix[i][j]; // XOR each element in the column
    }
  }
}

// Example usage
void print_matrix_xor_results(int rows, int cols) {
  uint8_t row_xor[MAX_BUFF_SIZE] = { 0 };
  uint8_t col_xor[MAX_BUFF_SIZE] = { 0 };

  calculate_matrix_xor(rows, cols, row_xor, col_xor);

  // Print row XORs
  printf("Row XORs:\n");
  for (int i = 0; i < rows; i++) {
    printf("Row %d: %d\n", i, row_xor[i]);
  }

  // Print column XORs
  printf("\nColumn XORs:\n");
  for (int j = 0; j < cols; j++) {
    printf("Column %d: %d\n", j, col_xor[j]);
  }
}
