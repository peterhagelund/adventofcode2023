use std::fs::read_to_string;

fn main() {
    let digits = [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine",
    ];
    let mut sum: u32 = 0;
    for line in read_to_string("../puzzle_input.txt").unwrap().lines() {
        let mut first_index: usize = line.len();
        let mut first: u32 = 0;
        let mut last_index: usize = 0;
        let mut last: u32 = 0;
        for (i, digit) in digits.iter().enumerate() {
            if let Some(index) = line.find(digit) {
                if index < first_index {
                    first_index = index;
                    first = (i % (digits.len() / 2)) as u32 + 1;
                }
            }
            if let Some(index) = line.rfind(digit) {
                if index >= last_index {
                    last_index = index;
                    last = (i % (digits.len() / 2)) as u32 + 1;
                }
            }
        }
        sum += first * 10 + last;
    }
    println!("sum = {sum}");
}
