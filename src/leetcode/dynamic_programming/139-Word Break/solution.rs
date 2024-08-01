#![allow(unused)]

fn main() {
    assert_eq!(
        false,
        Solution::word_break(
            "catsandog".to_string(),
            vec![
                "cats".to_string(),
                "dog".to_string(),
                "sand".to_string(),
                "and".to_string(),
                "cat".to_string()
            ]
        )
    )
}

struct Solution {}

use std::collections::HashMap;

type Map = HashMap<usize, bool>;

impl Solution {
    /* Bottom Up
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        let s = s.as_bytes();
        let n = s.len();

        let mut memo = vec![false; n + 1];
        memo[0] = true;

        for i in 1..=n {
            for word in word_dict.iter() {
                let m = word.len();
                if i >= m && memo[i - m] && &s[i - m..i] == word.as_bytes() {
                    memo[i] = true;
                    break;
                }
            }
        }

        *memo.last().unwrap()
    }
    // */
    // /* Top-Bottom with Memoization
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        fn rec(
            s: &[u8],
            word_dict: &Vec<String>,
            i: usize,
            memo: &mut HashMap<usize, bool>,
        ) -> bool {
            if i == s.len() {
                return true;
            }
            if let Some(&result) = memo.get(&i) {
                return result;
            }

            let mut val = false;
            for word in word_dict {
                let word_bytes = word.as_bytes();
                if s.len() >= i + word_bytes.len() && &s[i..i + word_bytes.len()] == word_bytes {
                    if rec(s, word_dict, i + word_bytes.len(), memo) {
                        memo.insert(i, true);
                        val = true;
                        break;
                    }
                }
            }

            memo.insert(i, val);
            val
        }

        let mut memo = HashMap::new();
        rec(s.as_bytes(), &word_dict, 0, &mut memo)
    }
    // */
}
