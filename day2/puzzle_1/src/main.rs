use std::fs::read_to_string;

#[derive(Debug)]
struct Reveal {
    red: Option<u32>,
    green: Option<u32>,
    blue: Option<u32>,
}

impl Reveal {
    fn from_str(pattern: &str) -> Reveal {
        let mut red: Option<u32> = None;
        let mut green: Option<u32> = None;
        let mut blue: Option<u32> = None;
        for color_count in pattern.trim().split(',') {
            let mut split = color_count.trim().split(' ');
            let count = split.next().unwrap().trim();
            let count: u32 = count.parse().unwrap();
            let color = split.next().unwrap().trim();
            match color {
                "red" => red = Some(count),
                "green" => green = Some(count),
                "blue" => blue = Some(count),
                _ => panic!("color {color} is not valid"),
            }
        }
        Reveal { red, green, blue }
    }

    fn is_possible(&self, red: u32, green: u32, blue: u32) -> bool {
        !(self.red.is_some_and(|r| r > red)
            || self.green.is_some_and(|g| g > green)
            || self.blue.is_some_and(|b| b > blue))
    }
}

#[derive(Debug)]
struct Game {
    id: u32,
    reveals: Vec<Reveal>,
}

impl Game {
    fn from_str(pattern: &str) -> Game {
        let mut split = pattern.split(':');
        let game_name = split.next().unwrap();
        let id: u32 = game_name[5..].parse().unwrap();
        let mut reveals = vec![];
        for pattern in split.next().unwrap().split(';') {
            reveals.push(Reveal::from_str(pattern));
        }
        Game { id, reveals }
    }

    fn is_possible(&self, red: u32, green: u32, blue: u32) -> bool {
        for reveal in &self.reveals {
            if !reveal.is_possible(red, green, blue) {
                return false;
            }
        }
        true
    }
}
fn main() {
    let mut sum: u32 = 0;
    for line in read_to_string("../puzzle_input.txt").unwrap().lines() {
        let game = Game::from_str(line);
        if game.is_possible(12, 13, 14) {
            sum += game.id;
        }
    }
    println!("sum = {sum}");
}
