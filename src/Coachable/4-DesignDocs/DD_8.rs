/*
463. Island Perimeter
https://leetcode.com/problems/island-perimeter/description/
*/

use std::collections::HashSet;

fn main() {
    // Example usage:
    let grid = vec![
        vec![0, 1, 0, 0],
        vec![1, 1, 1, 0],
        vec![0, 1, 0, 0],
        vec![1, 1, 0, 0],
    ];
    let result = island_perimeter(grid);
    println!("Island perimeter: {}", result);
}

fn island_perimeter(grid: Vec<Vec<i32>>) -> i32 {
    let mut visited: HashSet<(i32, i32)> = HashSet::new();

    fn dfs(grid: &Vec<Vec<i32>>, visited: &mut HashSet<(i32, i32)>, r: usize, c: usize) -> i32 {
        if r >= grid.len() || c >= grid[0].len() || grid[r][c] == 0 {
            return 1;
        }
        if visited.contains(&(r as i32, c as i32)) {
            return 0;
        }

        visited.insert((r as i32, c as i32));

        dfs(grid, visited, r.wrapping_sub(1), c)
            + dfs(grid, visited, r + 1, c)
            + dfs(grid, visited, r, c.wrapping_sub(1))
            + dfs(grid, visited, r, c + 1)
    }

    for r in 0..grid.len() {
        for c in 0..grid[0].len() {
            if grid[r][c] == 1 {
                return dfs(&grid, &mut visited, r, c);
            }
        }
    }
    0
}
