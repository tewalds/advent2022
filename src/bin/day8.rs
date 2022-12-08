
use std::fs::File;
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let file = File::open("day8.txt")?;
    let mut grove = Vec::<Vec<i8>>::new();
    for line in io::BufReader::new(file).lines() {
        let line = line?;
        if line.len() != 0 {
            grove.push(line.chars().map(|c| c.to_digit(10).unwrap() as i8).collect());
        }
    }
    let y_size = grove.len();
    let x_size = grove[0].len();

    let mut total_visible = 0;
    let mut best_score = 0;
    for y in 0..y_size {
        for x in 0..x_size {
            let height = grove[y][x];
            let mut visible = 4;
            let mut dists = [x, x_size-x-1, y, y_size-y-1];
            for (d, i) in (0..x).rev().enumerate() {
                if grove[y][i] >= height {
                    visible -= 1;
                    dists[0] = d + 1;
                    break;
                }
            }
            for (d, i) in (x+1..x_size).enumerate() {
                if grove[y][i] >= height {
                    visible -= 1;
                    dists[1] = d + 1;
                    break;
                }
            }
            for (d, i) in (0..y).rev().enumerate() {
                if grove[i][x] >= height {
                    visible -= 1;
                    dists[2] = d + 1;
                    break;
                }
            }
            for (d, i) in (y+1..y_size).enumerate() {
                if grove[i][x] >= height {
                    visible -= 1;
                    dists[3] = d + 1;
                    break;
                }
            }
            if visible != 0 {
                total_visible += 1;
            }
            let score = dists.iter().product();
            if score > best_score {
                best_score = score;
            }
        }
    }

    println!("visible: {total_visible}");
    println!("score: {best_score}");
    Ok(())
}
