import math
from collections import Counter

def detect_character_sets(password):
    """
    Checks the password to see which character categories are present.
    Returns a dictionary of boolean flags for each category.
    """
    flags = {
        "lower": False, "upper": False, "digit": False, "symbol": False
    }
    
    for char in password:
        if char.islower():
            flags["lower"] = True
        elif char.isupper():
            flags["upper"] = True
        elif char.isdigit():
            flags["digit"] = True
        else:
            # If it's not a letter or a number, we consider it a symbol
            flags["symbol"] = True
            
    return flags


def calculate_pool_size(flags):
    """
    Calculates the total character pool size based on which character 
    categories are present in the password.
    """
    pool_size = 0
    
    # Standard character set sizes
    if flags["lower"]:
        pool_size += 26
    if flags["upper"]:
        pool_size += 26
    if flags["digit"]:
        pool_size += 10
    if flags["symbol"]:
        pool_size += 32  # Common symbols on a standard keyboard
        
    return pool_size


def calculate_charset_entropy(length, pool_size):
    """
    Calculates the theoretical maximum entropy based on the password length
    and the size of the character pool.
    """
    # Prevent math errors if pool is 0 or 1 (log2(1) is 0, log2(0) is error)
    if length <= 0 or pool_size <= 1:
        return 0.0
        
    return length * math.log2(pool_size)


def calculate_shannon_entropy(password):
    """
    Calculates Shannon entropy based on the actual frequency of characters
    in the provided password.
    Returns a tuple: (entropy_per_character, total_shannon_bits)
    """
    length = len(password)
    if length <= 0:
        return 0.0, 0.0
        
    # Build a frequency table using Counter
    frequencies = Counter(password)
    
    entropy_per_char = 0.0
    for count in frequencies.values():
        # p is the probability of this character appearing at any given spot
        p = count / length
        # Add to the entropy sum: -p * log2(p)
        entropy_per_char -= p * math.log2(p)
        
    total_shannon_bits = entropy_per_char * length
    
    return entropy_per_char, total_shannon_bits


def rate_password(entropy_bits):
    """
    Returns a simple strength rating string based on character-set entropy.
    """
    if entropy_bits < 28:
        return "Very Weak"
    elif 28 <= entropy_bits < 36:
        return "Weak"
    elif 36 <= entropy_bits < 60:
        return "Moderate"
    elif 60 <= entropy_bits < 128:
        return "Strong"
    else:
        return "Very Strong"


def generate_feedback(password, flags, entropy_bits, shannon_bits):
    """
    Generates the 'Why' and 'Suggestions' lists for the final report.
    """
    why_reasons = []
    suggestions = []
    
    length = len(password)
    unique_chars = len(set(password))
    
    # --- Generate "Why" reasons ---
    if length >= 12:
        why_reasons.append("- Good length")
    elif length >= 8:
        why_reasons.append("- Acceptable length")
    else:
        why_reasons.append("- Too short")
        
    # Check how many character types are used
    types_used = sum(flags.values())
    if types_used >= 3:
        why_reasons.append("- Uses multiple character types")
    elif types_used == 2:
        why_reasons.append("- Uses a mix of character types")
    else:
        why_reasons.append("- Lacks character variety")
        
    # Compare Charset entropy vs Shannon entropy to detect repetition
    # If Shannon is significantly lower, it means there's repetition
    if entropy_bits > 0 and shannon_bits < entropy_bits * 0.6:
        why_reasons.append("- Repetition significantly lowers actual entropy")
    elif entropy_bits > 0 and shannon_bits < entropy_bits * 0.85:
        why_reasons.append("- Some repetition lowers actual entropy slightly")

    # --- Generate "Suggestions" ---
    if length < 12:
        suggestions.append("- Increase length to at least 12 characters")
        
    if not flags["lower"]:
        suggestions.append("- Add lowercase letters")
        
    if not flags["upper"]:
        suggestions.append("- Add uppercase letters")
        
    if not flags["digit"]:
        suggestions.append("- Add digits")
        
    if not flags["symbol"]:
        suggestions.append("- Add symbols for a larger character pool")
        
    # Check for repeated characters
    if unique_chars < length * 0.8:
        suggestions.append("- Avoid repeated characters or patterns")
        
    return why_reasons, suggestions


def print_report(password, length, unique_chars, flags, pool_size, 
                 charset_entropy, shannon_per_char, shannon_total, 
                 rating, why_reasons, suggestions):
    """
    Formats and prints the final analysis report to the terminal.
    """
    print("-" * 40)
    print("Password Entropy Calculator")
    print("-" * 40)
    
    # Use f-strings for clean formatting
    print(f"Password length: {length}")
    print(f"Unique characters: {unique_chars}")
    
    print("\nCharacter sets used:")
    print(f"- Lowercase: {'Yes' if flags['lower'] else 'No'}")
    print(f"- Uppercase: {'Yes' if flags['upper'] else 'No'}")
    print(f"- Digits: {'Yes' if flags['digit'] else 'No'}")
    print(f"- Symbols: {'Yes' if flags['symbol'] else 'No'}")
    
    print(f"\nCharacter pool size: {pool_size}")
    print(f"Character-set entropy: {charset_entropy:.2f} bits")
    
    print(f"\nShannon entropy per character: {shannon_per_char:.2f} bits")
    print(f"Total Shannon entropy: {shannon_total:.2f} bits")
    
    print(f"\nStrength rating: {rating}")
    
    print("\nWhy:")
    if why_reasons:
        for reason in why_reasons:
            print(reason)
    else:
        print("- Password is empty")
        
    print("\nSuggestions:")
    if suggestions:
        for suggestion in suggestions:
            print(suggestion)
    else:
        print("- Looks good! No immediate changes needed.")
        
    print("-" * 40)


def main():
    """
    Main function to run the Password Entropy Calculator.
    """
    # Prompt user for input (using input() hides the password in some terminals, 
    # but getpass is safer. Sticking to standard input() as requested for simplicity).
    password = input("Enter a password to analyze: ")
    
    # Handle empty password edge case safely
    if not password:
        print("\nError: Please enter a valid password.")
        return
        
    # 1. Detect character sets
    flags = detect_character_sets(password)
    
    # 2. Calculate pool size
    pool_size = calculate_pool_size(flags)
    
    # 3. Get basic counts
    length = len(password)
    unique_chars = len(set(password))
    
    # 4. Calculate entropies
    charset_entropy = calculate_charset_entropy(length, pool_size)
    shannon_per_char, shannon_total = calculate_shannon_entropy(password)
    
    # 5. Rate the password
    rating = rate_password(charset_entropy)
    
    # 6. Generate feedback
    why_reasons, suggestions = generate_feedback(
        password, flags, charset_entropy, shannon_total
    )
    
    # 7. Print the formatted report
    # Adding a newline before the report for cleaner terminal output
    print() 
    print_report(
        password=password,
        length=length,
        unique_chars=unique_chars,
        flags=flags,
        pool_size=pool_size,
        charset_entropy=charset_entropy,
        shannon_per_char=shannon_per_char,
        shannon_total=shannon_total,
        rating=rating,
        why_reasons=why_reasons,
        suggestions=suggestions
    )

if __name__ == "__main__":
    main()