fn main() {
    let mut flag = String::new();
    println!("This is a Rust Program!\nAnd don't forget the flag starts with moectf{{");
    println!("And please input the flag:");
    std::io::stdin().read_line(&mut flag).unwrap();
    let trim_flag = flag.trim_end();
    if trim_flag.len() != 30 {
        println!("Length wrong!");
        std::process::exit(1);
    }
    let enc: Vec<u8> = vec![0xe5,0xe7,0xed,0xeb,0xfc,0xee,0xf3,0xda,0xfd,0xfb,0xfc,0xd7,0xfa,0xed,0xfe,0xd7,0xff,0xe1,0xe4,0xe4,0xd7,0xea,0xed,0xd7,0xe9,0xff,0xee,0xfd,0xb9,0xf5,];
    let mut tmp_flag: Vec<u8> = Vec::new();
    for c in trim_flag.chars() {
        tmp_flag.push(c as u8);
    };
    let mut flag: bool = true;
    for i in 0..30 {
        if *enc.get(i).unwrap() != (tmp_flag.get(i).unwrap()^0x88)  {
            flag = false;
        }
    }
    if flag {
        println!("GOOD");
    } else {
        println!("Try one more time!");
    };
    println!();
}
