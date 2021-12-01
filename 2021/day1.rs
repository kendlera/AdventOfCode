use std::{
    env,
    fs::File,
    io::{BufRead, BufReader, Error, ErrorKind, Read},
};
use std::error::Error as genericError;

fn readInts<R: Read>(io: R) -> Result<Vec<i64>, Error> {
    let br = BufReader::new(io);
    br.lines()
        .map(|line| line.and_then(|v| v.parse().map_err(|e| Error::new(ErrorKind::InvalidData, e))))
        .collect()
}

fn part1() -> Result<(), Box<dyn genericError>> {
    let wordlist_file = File::open("puzzle_input.txt")?;
    let vec = readInts(wordlist_file)?;
    let mut lastDepth = vec[0];
    let mut numIncremented = 0;
    for depth in vec.iter() {
        if depth > &lastDepth {
            numIncremented += 1;
        }
        lastDepth = *depth;
    }
    println!("{}", numIncremented);
    return Ok(());
}

fn part2() -> Result<(), Box<dyn genericError>> {
    let wordlist_file = File::open("puzzle_input.txt")?;
    let vec = readInts(wordlist_file)?;
    let mut numIncremented = 0;
    let mut lastDepth = vec[0] + vec[1] + vec[2];
    let numDepths = vec.len();
    let mut sumDepth;
    for depthIdx in 1..(numDepths-2) {
        sumDepth = vec[depthIdx] + vec[depthIdx+1] + vec[depthIdx+2];
        if sumDepth > lastDepth {
            numIncremented += 1;
        }
        lastDepth = sumDepth;
    }
    println!("{}", numIncremented);
    return Ok(());
}

fn main() {
    part2();
}
