extern crate itertools;

use std::fs::File;
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let file = File::open("day5.txt")?;
    let mut reading_stack = true;
    let mut stacks = Vec::<Vec<char>>::new();
    for line in io::BufReader::new(file).lines() {
        let line = line?;

        if line.len() == 0 {
            reading_stack = false;
            for i in 0..stacks.len() {
                let len = stacks[i].len();
                stacks[i].truncate(len - 1);
                stacks[i].reverse();
            }
            // for mut s in stacks {
            //     s.truncate(s.len() - 1);
            //     s.reverse();
            // }
        continue;
        }
        if reading_stack {
            let line: Vec<char> = line.chars().collect();
            let count = (line.len() + 1) / 4;
            if stacks.len() == 0 {
                for _ in 0..count {
                    stacks.push(Vec::new());
                }
            }
            for i in 0..count {
                let col = i*4 + 1;
                if line[col] != ' ' {
                    stacks[i].push(line[col]);
                }
            }
        } else {
            let parts = line.split(' ').collect::<Vec<&str>>();
            let count = parts[1].parse::<usize>().unwrap();
            let src = parts[3].parse::<usize>().unwrap() - 1;
            let dest = parts[5].parse::<usize>().unwrap() - 1;

            // Part 1:
            for _ in 0..count {
                let v = stacks[src].pop().unwrap();
                stacks[dest].push(v);
            }

            // Part 2:
            // let src_keep = stacks[src].len() - count;
            // let mut v = stacks[src].split_off(src_keep);
            // stacks[dest].append(&mut v);
        }
    }
    for s in &stacks {
        print!("{}", s[s.len() - 1]);
    }
    println!();
    Ok(())
}
