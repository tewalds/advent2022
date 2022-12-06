use std::fs::File;
use std::io::{self, BufRead};
use std::collections::HashSet;

fn main() -> io::Result<()> {
    let file = File::open("day6.txt")?;
    for line in io::BufReader::new(file).lines() {
        let line = line?;
        for len in [4, 14] {
            for i in 0..line.len()-len {
                let a: HashSet<_> = line[i..i+len].as_bytes().iter().cloned().collect();
                if a.len() == len {
                    print!("{} ", i+len);
                    break;
                }
            }
        }
        println!();
    }
    Ok(())
}
