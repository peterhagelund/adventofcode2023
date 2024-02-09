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

    fn update_minimums(&self, red: &mut u32, green: &mut u32, blue: &mut u32) {
        if self.red.is_some_and(|r| r > *red) {
            *red = self.red.unwrap()
        }
        if self.green.is_some_and(|g| g > *green) {
            *green = self.green.unwrap()
        }
        if self.blue.is_some_and(|b| b > *blue) {
            *blue = self.blue.unwrap()
        }
    }
}

#[derive(Debug)]
struct Game {
    _id: u32,
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
        Game { _id: id, reveals }
    }

    fn update_minimums(&self, red: &mut u32, green: &mut u32, blue: &mut u32) {
        for reveal in &self.reveals {
            reveal.update_minimums(red, green, blue);
        }
    }
}

fn main() {
    let mut sum: u32 = 0;
    for line in read_to_string("../puzzle_input.txt").unwrap().lines() {
        let mut red: u32 = 1;
        let mut green: u32 = 1;
        let mut blue: u32 = 1;
        let game = Game::from_str(line);
        game.update_minimums(&mut red, &mut green, &mut blue);
        sum += red * green * blue;
    }
    println!("sum = {sum}");
}
