use std::fs::read_to_string;

fn main() {
    let s = read_to_string("../puzzle_input.txt").unwrap();
    let mut counts: Vec<u32> = Vec::new();
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
        let mut count = 0;
        for number in my_numbers {
            if winning_numbers.contains(&number) {
                count += 1;
            }
        }
        counts.push(count);
    }
    let mut sum = 0;
    for index in 0..counts.len() {
        sum = process_card(sum, index, &counts);
    }
    println!("sum = {sum}");
}

/// Processes the outcome of a single card.
///
/// The card is processed and then all subsequent cards are processed recursively.
fn process_card(sum: u32, index: usize, counts: &Vec<u32>) -> u32 {
    let mut sum = sum + 1;
    let count = counts[index];
    for i in 1..count + 1 {
        let new_index = index + i as usize;
        if new_index < counts.len() {
            sum = process_card(sum, new_index, counts);
        }
    }
    sum
}
