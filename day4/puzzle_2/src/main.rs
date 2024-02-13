use std::fs::read_to_string;

fn main() {
    let s = read_to_string("../puzzle_input.txt").unwrap();
    let mut counts: Vec<usize> = Vec::new();
    for card in s.lines() {
        let parts: Vec<&str> = card.split(|c| ":|".contains(c)).collect();
        let winning_numbers: Vec<usize> = parts[1]
            .split(|c| char::is_whitespace(c))
            .filter(|s| !s.is_empty())
            .map(|s| s.parse().unwrap())
            .collect();
        let my_numbers: Vec<usize> = parts[2]
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
        process_card(&mut sum, &counts[index..]);
    }
    println!("sum = {sum}");
}

/// Processes the outcome of a single card.
///
/// The card is processed and then all subsequent cards are processed recursively.
fn process_card(sum: &mut u32, counts: &[usize]) {
    *sum += 1;
    for i in 1..=counts[0] {
        process_card(sum, &counts[i..]);
    }
}
