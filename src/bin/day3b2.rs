extern crate itertools;

use std::fs::File;
use std::io::{self, BufRead};
use std::collections::HashSet;
use itertools::Itertools;

fn main() -> io::Result<()> {
    let file = File::open("day3.txt")?;
    let scores = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".as_bytes();
    let total = io::BufReader::new(file)
        .lines()
        .enumerate()
        .group_by(|(i, _)| i / 3).into_iter()
        .map(|(_, group)|
            group
            .map(|(_, lines)| lines)
            .map(|line| line.unwrap().as_bytes().iter().cloned().collect::<HashSet<u8>>())
            .reduce(|a, b| a.intersection(&b).cloned().collect())
            .unwrap()
            .iter()
            .map(|c| scores.iter().position(|&i| i == *c).unwrap())
            .fold(0, |a, b| a + b))
        .fold(0, |a, b| a + b);

    println!("{}", total);
    Ok(())
}
