use std::fs::File;

use regex::Regex;
use std::io::{self, prelude::*, BufReader};
use std::path::Path;

fn main() -> io::Result<()> {
    let re: Regex = Regex::new("[0-9]").unwrap();

    let path = Path::new("../../puzzles/1.txt");
    let display = path.display();

    // Open the path in read-only mode, returns `io::Result<File>`
    let mut file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, why),
        Ok(file) => file,
    };

    let mut total = 0;
    let reader = BufReader::new(file);
    for line in reader.lines() {
        let line = line?;
        let caps: Vec<_> = re.find_iter(&line).collect();
        let number = format!("{}{}", caps[0].as_str(), caps[caps.len() - 1].as_str());

        total += number.parse::<i32>().unwrap()
    }
    println!("{}", total);

    Ok(())
}
