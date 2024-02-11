use regex::{Match, Regex};
use std::fs::read_to_string;

/// An encapsualtion of an Elf gondola engine schematic.
///
/// The schematic is expected to be read as `&str` and be ASCII.
#[derive(Debug)]
struct Schematic<'a> {
    bytes: Vec<&'a [u8]>,
    matches: Vec<Vec<Match<'a>>>,
}

/// `Schematic` methods.
impl Schematic<'_> {
    /// Creates a `Schematic` from a `&str`.
    ///
    /// The string is split into lines and the corresponding ASCII bytes are captured
    /// as a "shadow" vector.
    ///
    /// A `Regex` for matching numbers is created and all matches are captured.
    fn from_str(s: &str) -> Schematic {
        let lines: Vec<&str> = s.lines().collect();
        let bytes: Vec<&[u8]> = lines.iter().map(|l| l.as_bytes()).collect();
        let re = Regex::new("[0-9]{1,3}").unwrap();
        let mut matches: Vec<Vec<Match>> = Vec::new();
        for line in &lines {
            matches.push(re.find_iter(line).collect());
        }
        Schematic { bytes, matches }
    }

    /// Finds all adjacent matches for the specified `y` and `x` coordinates within the `Schematic`.
    ///
    /// Numbers are adjacent to the `y`/`x` coordinate if they butt up against the gear
    /// like:
    /// ```
    /// 123*456
    /// ```
    /// or if they are "near" the gear like:
    /// ```
    /// 123
    ///    *
    ///   456
    /// ```
    fn adjacents_for(&self, y: usize, x: usize) -> Vec<&Match> {
        let mut adjacents: Vec<&Match> = Vec::new();
        if let Some(m) = self.adjacent_before(y, x) {
            adjacents.push(m);
        }
        if let Some(m) = self.adjacent_after(y, x) {
            adjacents.push(m);
        }
        if let Some(matches) = self.adjacents_above(y, x) {
            adjacents.extend(matches);
        }
        if let Some(matches) = self.adjacents_below(y, x) {
            adjacents.extend(matches);
        }
        adjacents
    }

    /// Looks for an adjacent number before the `*` at the specified `y`/`x` coordinates.
    ///
    /// Example
    /// -------
    /// ```
    /// 123*...
    /// ```
    fn adjacent_before(&self, y: usize, x: usize) -> Option<&Match> {
        self.matches[y].iter().find(|&m| x == m.end())
    }

    /// Looks for an adjacent number after the `*` at the specified `y`/`x` coordinates.
    ///
    /// Example
    /// -------
    /// ```
    /// ...*456
    /// ```
    fn adjacent_after(&self, y: usize, x: usize) -> Option<&Match> {
        self.matches[y].iter().find(|&m| x + 1 == m.start())
    }

    /// Finds `0`, `1`, or `2` adjacent number(s) above the `*` at the specified `y`/`x` coordinates.
    ///
    /// If the the `*` is within the first line of the schematic, `None` is returned.
    ///
    /// Example
    /// -------
    /// ```
    /// .123...
    ///     *
    /// ```
    fn adjacents_above(&self, y: usize, x: usize) -> Option<Vec<&Match>> {
        if y == 0 {
            None
        } else {
            Some(self.adjacents_near(y - 1, x))
        }
    }

    /// Finds `0`, `1`, or `2` adjacent number(s) below the `*` at the specified `y`/`x` coordinates.
    ///
    /// If the the `*` is within the last line of the schematic, `None` is returned.
    ///
    /// Example
    /// -------
    /// ```
    ///     *
    /// ..12.3..
    /// ```
    fn adjacents_below(&self, y: usize, x: usize) -> Option<Vec<&Match>> {
        if y + 1 == self.bytes.len() {
            None
        } else {
            Some(self.adjacents_near(y + 1, x))
        }
    }

    /// Finds `0`, `1`, or `2` adjacent number(s) "near" the `*` at the specified `y`/`x` coordinates.
    fn adjacents_near(&self, y: usize, x: usize) -> Vec<&Match> {
        self.matches[y]
            .iter()
            .filter(|&m| x + 1 >= m.start() && x <= m.end())
            .collect()
    }
}

fn main() {
    let s = read_to_string("../puzzle_input.txt").unwrap();
    assert!(s.is_ascii());
    let schematic = Schematic::from_str(&s);
    let mut sum: u32 = 0;
    for (y, line_bytes) in schematic.bytes.iter().enumerate() {
        for (x, b) in line_bytes.iter().enumerate() {
            if *b != b'*' {
                continue;
            }
            let adjacents = schematic.adjacents_for(y, x);
            if adjacents.len() != 2 {
                continue;
            }
            sum += adjacents[0].as_str().parse::<u32>().unwrap()
                * adjacents[1].as_str().parse::<u32>().unwrap();
        }
    }
    println!("sum = {sum}");
}
