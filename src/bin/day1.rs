use std::fs::File;
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let file = File::open("day1.txt")?;
    let mut elves: Vec<i32> = vec![];
    let mut elf: i32 = 0;
    for line in io::BufReader::new(file).lines()  {
        if let Ok(line) = line {
            if line == "" {
                elves.push(elf);
                elf = 0;
            } else {
                elf += line.parse::<i32>().unwrap()
            }
        }
    }
    elves.sort();
    elves.reverse();
    println!("{}", elves[0]);
    println!("{}", elves[0..3].iter().sum::<i32>());
    Ok(())
}
