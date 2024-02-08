use std::fs::read_to_string;

fn main() {
    let mut sum: u32 = 0;
    for line in read_to_string("../puzzle_input.txt").unwrap().lines() {
        let mut first: Option<u32> = None;
        let mut last: Option<u32> = None;
        for c in line.chars() {
            match c.to_digit(10) {
                Some(n) => {
                    if first.is_none() {
                        first = Some(n);
                    }
                    last = Some(n);

                },
                None => continue,
            }
        }
        sum += first.unwrap() * 10 + last.unwrap();
    }
    println!("sum = {sum}");
}
