extern crate itertools;

use std::fs::File;
use std::io::{self, BufRead};
use std::collections::HashSet;
// use itertools::Itertools;

fn main() -> io::Result<()> {
    let file = File::open("day3.txt")?;
    let mut total: i32 = 0;
    let scores = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".as_bytes();
    let mut set = HashSet::new();
    for (i, line) in io::BufReader::new(file).lines().enumerate() {
        let line = line?;
        let a: HashSet<_> = line.as_bytes().iter().cloned().collect();
        if i % 3 == 0 {
            set = a;
        } else {
            set = set.intersection(&a).cloned().collect();
        }
        if i % 3 == 2 {
            for c in &set {
                let score = scores.iter().position(|&i| i == *c).unwrap() as i32;
                total += score;
                // println!("{} {} {}", c, score, total);
            }
        }
    }

    println!("{}", total);
    Ok(())
}
