use std::fs::read_to_string;

fn main() {
    let mut sum: u32 = 0;
    for line in read_to_string("../puzzle_input.txt").unwrap().lines() {
        let mut first: Option<u32> = None;
        let mut last: Option<u32> = None;
        for c in line.chars() {
            if let Some(n) = c.to_digit(10) {
                if first.is_none() {
                    first = Some(n);
                }
                last = Some(n);
            }
        }
        sum += first.unwrap() * 10 + last.unwrap();
    }
    println!("sum = {sum}");
}
