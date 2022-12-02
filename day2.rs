use std::fs::File;
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let file = File::open("day2.txt")?;
    let mut total: i32 = 0;
    for line in io::BufReader::new(file).lines() {
        let line = line?;
        if line.len() == 3 {
            let a = i32::from(line.as_bytes()[0]) - 65;
            let b = i32::from(line.as_bytes()[2]) - 88;
            let mut score = b + 1;
            if a == b {
                score += 3;
            } else if a == (b + 2) % 3 {
                score += 6;
            }
            // println!("{} {} {}", a, b, score);
            total += score;
        }
    }
    println!("{}", total);
    Ok(())
}
