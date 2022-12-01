
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    if let Ok(lines) = read_lines("day1.txt") {
        let mut elves: Vec<i32> = vec![];
        let mut elf: i32 = 0;
        for line in lines {
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
    }
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
