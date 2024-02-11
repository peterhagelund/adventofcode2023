use regex::Regex;
use std::fs::read_to_string;

fn main() {
    let s = read_to_string("../puzzle_input.txt").unwrap();
    assert!(s.is_ascii());
    let ignorables = b".0123456789";
    let lines: Vec<&str> = s.lines().collect();
    let schematic: Vec<&[u8]> = lines.iter().map(|l| l.as_bytes()).collect();
    let re = Regex::new("[0-9]{1,3}").unwrap();
    let mut sum: u32 = 0;
    for (line_no, line) in lines.iter().enumerate() {
        for m in re.find_iter(line) {
            let mut start = m.start();
            let mut end = m.end();
            let mut is_part = (start > 0 && !ignorables.contains(&schematic[line_no][start - 1]))
                || (end < line.len() && !ignorables.contains(&schematic[line_no][end]));
            if !is_part {
                start = if start > 0 { start - 1 } else { start };
                end = if end == line.len() { end - 1 } else { end };
                if line_no > 0 {
                    for i in start..=end {
                        if !ignorables.contains(&schematic[line_no - 1][i]) {
                            is_part = true;
                            break;
                        }
                    }
                }
                if !is_part && line_no < lines.len() - 1 {
                    for i in start..=end {
                        if !ignorables.contains(&schematic[line_no + 1][i]) {
                            is_part = true;
                            break;
                        }
                    }
                }
            }
            if is_part {
                sum += m.as_str().parse::<u32>().unwrap();
            }
        }
    }
    println!("sum = {sum}");
}
