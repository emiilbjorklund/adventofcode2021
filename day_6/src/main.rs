use std::io::{self, BufRead};



// Good impl
fn part_two(mut numbers:  Vec<u128>){
    let mut lanterns: [u128; 9] = [0; 9];

   for i in 0..8 {
        lanterns[i] = numbers.iter().filter(|&n| *n == i.try_into().unwrap()).count().try_into().unwrap();
    }

    for _n in 0..256{
        let  temp = lanterns[0];
        for i in 0..8 {
            lanterns[i] = lanterns[i + 1];
        }
        lanterns[lanterns.len() - 3] = lanterns[lanterns.len() - 3] + temp;
        lanterns[lanterns.len() - 1] = temp;

    }

    let sum: u128 = lanterns.iter().sum();
    println!("{}", sum);


}

// Bad impl
fn part_one(mut numbers:  Vec<u128>){
    for _n in 0..80 {
        let mut temp: Vec<u128> = Vec::new();

        for i in 0..numbers.len() as u128 {
            if  numbers[i as usize] == 0 {
                temp.push(8);
                numbers[i as usize] = 6;
            } else {
                numbers[i as usize] = numbers[i as usize] - 1;
            }
        }

        if temp.len() > 0{
            numbers.append(&mut temp);
        }
        temp.clear()
    }

    println!("{:?}", numbers.len());

}

fn main() {

    let mut line = String::new();
    let stdin = io::stdin();
    stdin.lock().read_line(&mut line).unwrap();

    line.pop();

    let numbers: Vec<u128> = line.split(",").map(|x| x.parse::<u128>().unwrap()).collect();

    //part_one(numbers);
    part_two(numbers);

}