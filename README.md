# Password Entropy Calculator

A Python CLI project that evaluates password strength using two entropy-based approaches: character-set entropy and Shannon entropy. It is designed as a small learning project focused on practical Python, mathematical reasoning, and clean command-line program structure.

## Why I built this

I built this project to better understand how password strength can be analyzed beyond simple length checks or basic validation rules. I wanted to explore how Python can be used to combine math, frequency analysis, and real-world security concepts in a way that is both practical and easy to explain. [web:73][web:76]

## Features

- Detects lowercase, uppercase, digits, and special characters
- Estimates total character pool size
- Calculates character-set entropy
- Calculates Shannon entropy based on character frequency
- Rates password strength using the calculated results
- Provides simple suggestions to improve weak passwords

## How it works

This project evaluates passwords using two different ideas:

1. **Character-set entropy**  
   Estimates how difficult a password is to brute-force based on its length and the size of the possible character pool.

   ```text
   entropy_bits = password_length * log2(character_pool_size)
   ```

2. **Shannon entropy**  
   Measures how much unpredictability is actually present in the password by looking at character repetition and frequency distribution.

   ```text
   H = -sum(p * log2(p))
   total_shannon_bits = H * password_length
   ```

Character-set entropy gives a theoretical estimate of complexity, while Shannon entropy gives a more realistic view of repetition and predictability inside the password itself. [web:73][web:76]

## Project structure

```text
paste your tree here
```

## Run locally

```bash
python password_entropy_calculator.py
```

## Example input

```text
P@ssword123!!
```

## Example output

```text
Password length: 13
Unique characters: 10
Character pool size: 94
Character-set entropy: 85.21 bits
Shannon entropy per character: 3.24 bits
Total Shannon entropy: 42.12 bits
Strength rating: Strong
```

## Screenshots

![Input Example](./screenshots/input-example.png)
![Output Report](./screenshots/output-report.png)

## What I learned

- How entropy can be applied to password analysis
- The difference between theoretical complexity and actual unpredictability
- How repeated characters reduce effective randomness
- How to structure and present a small Python CLI project clearly

## Future improvements

- Add batch password testing from a file
- Export analysis results to JSON
- Add unit tests for entropy calculations and strength ratings

## License

This project is licensed under the MIT License.
