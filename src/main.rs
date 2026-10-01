use std::io::{self, Read};

fn main() -> io::Result<()> {
    let args = std::env::args().skip(1).collect::<Vec<_>>();
    let mut input = args.join(" ");
    if args.is_empty() {
        io::stdin().read_to_string(&mut input)?;
    }

    println!("{}", odd_echo(&input));
    Ok(())
}

fn odd_echo(input: &str) -> String {
    input
        .split_whitespace()
        .rev()
        .map(|word| word.chars().rev().collect::<String>())
        .collect::<Vec<_>>()
        .join(" ")
}

#[cfg(test)]
mod tests {
    use super::odd_echo;

    #[test]
    fn reverses_word_order_and_each_word() {
        assert_eq!(odd_echo("Rust is odd"), "ddo si tsuR");
    }

    #[test]
    fn normalizes_whitespace() {
        assert_eq!(odd_echo("  hello\tstrange\nworld  "), "dlrow egnarts olleh");
    }

    #[test]
    fn handles_empty_input() {
        assert_eq!(odd_echo(" \n\t"), "");
    }
}
