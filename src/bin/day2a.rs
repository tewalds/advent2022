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
            let o = (b - a + 4) % 3;
            let score = b + 1 + o * 3;
            // println!("{} {} {} {}", a, b, o, score);
            total += score;
        }
    }
    println!("{}", total);
    Ok(())
}
