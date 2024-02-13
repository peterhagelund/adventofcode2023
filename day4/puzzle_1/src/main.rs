use std::fs::read_to_string;

fn main() {
    let s = read_to_string("../puzzle_input.txt").unwrap();
    let mut sum = 0;
    for card in s.lines() {
        let parts: Vec<&str> = card.split(|c| ":|".contains(c)).collect();
        let winning_numbers: Vec<u32> = parts[1]
            .split(|c| char::is_whitespace(c))
            .filter(|s| !s.is_empty())
            .map(|s| s.parse().unwrap())
            .collect();
        let my_numbers: Vec<u32> = parts[2]
            .split(|c| char::is_whitespace(c))
            .filter(|s| !s.is_empty())
            .map(|s| s.parse().unwrap())
            .collect();
        let mut points = 0;
        for number in my_numbers {
            if winning_numbers.contains(&number) {
                points = if points == 0 { 1 } else { points * 2 };
            }
        }
        sum += points;
    }
    println!("sum = {sum}");
}
