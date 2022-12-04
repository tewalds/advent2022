extern crate itertools;

use std::fs::File;
use std::io::{self, BufRead};
use itertools::Itertools;

fn main() -> io::Result<()> {
    let file = File::open("day4.txt")?;
    let mut full: i32 = 0;
    let mut partial: i32 = 0;
    for line in io::BufReader::new(file).lines() {
        let Some((a_min, a_max, b_min, b_max)) = line?
            .split(&['-', ','][..])
            .map(|v| v.parse::<i32>().unwrap())
            .collect_tuple()
            else { panic!("wrong number of elements")};
        if (a_min <= b_min && a_max >= b_max) ||
           (a_min >= b_min && a_max <= b_max) {
            full += 1;
        }
        if (a_min <= b_min && a_max >= b_min) ||
           (b_min <= a_min && b_max >= a_min) {
            partial += 1;
        }
    }
    println!("{}", full);
    println!("{}", partial);
    Ok(())
}
