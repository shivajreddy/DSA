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

// Function to allocate a matrix and initialize to 0
u_int8_t** allocate_matrix(int rows, int cols) {
  int** matrix = malloc(rows * sizeof(int*));
  if (!matrix) exit(1); // Memory allocation failed

  for (int i = 0; i < rows; i++) {
    matrix[i] = malloc(cols * sizeof(int));
    if (!matrix[i]) exit(1); // Memory allocation failed
  }
  return matrix;
}

// Function to free the matrix
void free_matrix(int** matrix, int rows) {
  for (int i = 0; i < rows; i++) {
    free(matrix[i]);
  }
  free(matrix);
}

// Function to simulate the algorithm (you can modify this part)
u_int8_t my_algorithm(int** matrix, int rows, int cols);

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
    char** matrix = allocate_matrix(rows, cols);

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
    my_algorithm(matrix, rows, cols);

    // Free allocated memory
    free_matrix(matrix, rows);
  }

  fclose(file);
  return 0;
}

void my_algorithm(int** matrix, int rows, int cols) {
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
