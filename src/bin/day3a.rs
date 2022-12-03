use std::fs::File;
use std::io::{self, BufRead};
use std::collections::HashSet;

fn main() -> io::Result<()> {
    let file = File::open("day3.txt")?;
    let mut total: i32 = 0;
    let scores = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".as_bytes();
    for line in io::BufReader::new(file).lines() {
        let line = line?;
        let a: HashSet<_> = line[..line.len()/2].as_bytes().iter().cloned().collect();
        let b: HashSet<_> = line[line.len()/2..].as_bytes().iter().cloned().collect();
        for c in a.intersection(&b) {
            let score = scores.iter().position(|&i| i == *c).unwrap() as i32;
            total += score;
            // println!("{} {} {}", c, score, total);
        }
    }
    println!("{}", total);
    Ok(())
}
