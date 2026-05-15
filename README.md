# Password Entropy Calculator

A simple Python project that evaluates password strength using character-set entropy and Shannon entropy.

## Why I built this
I wanted to understand how password strength can be measured in a more practical way using Python, math, and frequency analysis.

## Features
- Detects lowercase, uppercase, digits, and symbols
- Estimates character pool size
- Calculates character-set entropy
- Calculates Shannon entropy from character frequency
- Rates password strength
- Gives simple suggestions for improvement

## How it works
This project uses two ideas:

1. Character-set entropy:
   entropy_bits = password_length * log2(character_pool_size)

2. Shannon entropy:
   H = -sum(p * log2(p))
   total_shannon_bits = H * password_length

Character-set entropy estimates possible complexity.
Shannon entropy reflects actual repetition in the password.

## Project structure
```text
paste your tree here
```

## Run locally
```bash
python password_entropy_calculator.py
```

## Example input
Example password:
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
- How entropy is used in password analysis
- How repetition affects unpredictability
- How to structure a small Python CLI project cleanly

## Future improvements
- Add batch password testing from a file
- Export reports to JSON
- Add unit tests