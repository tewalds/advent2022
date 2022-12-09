use std::collections::HashSet;
use std::fs::File;
use std::io::{self, BufRead};
use std::ops;

#[derive(Eq, Hash, PartialEq, Clone, Copy)]
struct Point {
    x: i32,
    y: i32,
}

impl ops::Add<Point> for Point {
    type Output = Point;
    fn add(self, rhs: Point) -> Point {
        Point{x: self.x + rhs.x, y: self.y + rhs.y}
    }
}

impl ops::Sub<Point> for Point {
    type Output = Point;
    fn sub(self, rhs: Point) -> Point {
        Point{x: self.x - rhs.x, y: self.y - rhs.y}
    }
}

fn update_head(head: Point, direction: &str) -> Point {
    match direction {
        "R" => head + Point {x: 1, y: 0},
        "L" => head + Point {x: -1, y: 0},
        "U" => head + Point {x: 0, y: 1},
        "D" => head + Point {x: 0, y: -1},
        _ => panic!("Invalid direction."),
    }
}
fn update_tail(head: Point, tail: Point) -> Point {
    match head - tail {
        Point{x: 2, y: 2} => tail + Point {x: 1, y: 1},
        Point{x: -2, y: 2} => tail + Point {x: -1, y: 1},
        Point{x: 2, y: -2} => tail + Point {x: 1, y: -1},
        Point{x: -2, y: -2} => tail + Point {x: -1, y: -1},
        Point{x: 2, y: n} => tail + Point {x: 1, y: n},
        Point{x: -2, y: n} => tail + Point {x: -1, y: n},
        Point{x: n, y: 2} => tail + Point {x: n, y: 1},
        Point{x: n, y: -2} => tail + Point {x: n, y: -1},
        _ => tail,
    }
}

fn main() -> io::Result<()> {
    let file = File::open("day9.txt")?;
    let mut set = HashSet::<Point>::new();
    const KNOTS: usize = 1;  // 1 for part 1, 9 for part 2.
    let mut state = [Point{x: 0, y: 0}; KNOTS + 1];
    for line in io::BufReader::new(file).lines() {
        let line = line?;
        let Some((direction, count)) = line.split_once(' ')
            else { panic!("wrong number of elements")};
        let count = count.parse::<i32>().unwrap();
        for _ in 0..count {
            state[0] = update_head(state[0], direction);
            for i in 1..state.len() {
                state[i] = update_tail(state[i-1], state[i]);
            }
            set.insert(state[state.len()-1]);
        }
    }
    println!("tail: {}", set.len());
    Ok(())
}
