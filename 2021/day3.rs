use std::fs::read_to_string;
use std::error::Error as genericError;

fn part1(diagnostic_report: &[i32]) -> Result<(Vec<i32>), Box<dyn genericError>> {
    let width = 12;
    let mut sums = vec![0; width];
    let mut total = 0;
    for item in diagnostic_report.iter() {
        for pos in 0..width {
            if (i32::pow(2, pos as u32) & item) > 0 {
                sums[pos] += 1;
            }
        }
        total += 1;
    }
    for pos in 0..width {
        if (sums[pos] > ((total / 2) - 1)) {
            println!("1");
        } else {
            println!("0");
        }
    }
    return Ok(sums);
}

fn find_closest_match(diagnostic_report: &[i32], pos: i32) {
    if diagnostic_report.len() < 2 {
        println!("{}", diagnostic_report[0]);
        return;
    }
    let mut candidates: Vec<i32> = Vec::new();
    let mcb = find_mcb_at_pos(&diagnostic_report, pos);
    for item in diagnostic_report.iter() {
        if ((i32::pow(2, pos as u32) & item) > 0) && (mcb == 1) {
            candidates.push(*item);
        } else if ((i32::pow(2, pos as u32) & item) == 0) && (mcb == 0) {
            candidates.push(*item);
        }
    }
    println!("candidates length {}", candidates.len());
    find_closest_match(&candidates, pos-1);
}

fn find_mcb_at_pos(items: &[i32], pos: i32) -> i32 {
    // find the most common bit at some position
    let mut summed = 0;
    let mut total = 0;
    let mask = i32::pow(2, pos as u32);
    for item in items.iter() {
        if (mask & item) > 0 {
            summed += 1;
        }
        total += 1;
    }
    if summed >= (total / 2) {
        return 0;
    }
    return 1;
}

fn part2(diagnostic_report: &[i32]) -> Result<(), Box<dyn genericError>> {
    let most_common = i32::from_str_radix("101110111100", 2).unwrap();
    find_closest_match(&diagnostic_report, 11);
    return Ok(());
}

fn main() {
    let binary_strs = read_to_string("puzzle_input.txt").expect("File Not Found");
    let binary_nums = binary_strs.lines().map(|n| i32::from_str_radix(n, 2).unwrap()).collect::<Vec<_>>();
    // part1(&binary_nums);
    part2(&binary_nums); // 3295388 too low
    println!("Hello, world!");
}
