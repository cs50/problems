#!/usr/bin/env python3
"""
Simple Dynamic DNA Test Generator
Generates dynamic.csv and dynamic.txt with random STR sequences.
"""

import random
import csv

CSV_OUTPUT_PATH = 'databases/dynamic.csv'
TXT_OUTPUT_PATH = 'sequences/dynamic.txt'

def generate_random_str_sequence(length):
    """Generate a random STR sequence of given length."""
    bases = ['A', 'T', 'G', 'C']
    return ''.join(random.choice(bases) for _ in range(length))

def generate_dna_sequence_with_strs(str_counts):
    """Generate a DNA sequence with specified STR counts at random positions."""
    bases = ['A', 'T', 'G', 'C']
    sequence_parts = []
    
    # Add random DNA sections
    for i in range(15):
        random_length = random.randint(50, 200)
        random_dna = ''.join(random.choice(bases) for _ in range(random_length))
        sequence_parts.append(random_dna)
    
    # Insert STR blocks at random positions
    for str_seq, count in str_counts.items():
        if count > 0:
            str_block = str_seq * count
            insert_pos = random.randint(0, len(sequence_parts))
            sequence_parts.insert(insert_pos, str_block)
            
            # Add random DNA after
            random_length = random.randint(20, 100)
            random_dna = ''.join(random.choice(bases) for _ in range(random_length))
            sequence_parts.insert(insert_pos + 1, random_dna)
    
    return ''.join(sequence_parts)

def generate_test_files():
    """Generate dynamic.csv and dynamic_sequence.txt with random STRs."""
    
    # Generate 6-8 random STR sequences of different lengths
    num_strs = random.randint(6, 8)
    str_sequences = []
    
    for _ in range(num_strs):
        str_length = random.randint(3, 8)  # STR length between 3-8 bases
        str_seq = generate_random_str_sequence(str_length)
        # Ensure uniqueness
        while str_seq in str_sequences:
            str_seq = generate_random_str_sequence(str_length)
        str_sequences.append(str_seq)
    
    # Generate random counts for each STR for the Philosopher profile
    philosopher_counts = {}
    for str_seq in str_sequences:
        philosopher_counts[str_seq] = random.randint(15, 50)
    
    # Create some other profiles with different counts
    profiles = []
    for i in range(3):
        profile = {'name': f'Person{i+1}'}
        for str_seq in str_sequences:
            profile[str_seq] = random.randint(5, 30)
        profiles.append(profile)
    
    # Add Philosopher profile that matches the sequence exactly
    philosopher_profile = {'name': 'Philosopher'}
    philosopher_profile.update(philosopher_counts)
    profiles.append(philosopher_profile)
    
    # Generate CSV file
    with open(CSV_OUTPUT_PATH, 'w', newline='') as csvfile:
        fieldnames = ['name'] + str_sequences
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for profile in profiles:
            writer.writerow(profile)
    
    # Generate DNA sequence using the philosopher_counts
    dna_sequence = generate_dna_sequence_with_strs(philosopher_counts)
    
    # Save DNA sequence
    with open(TXT_OUTPUT_PATH, 'w') as f:
        f.write(dna_sequence)

if __name__ == "__main__":
    generate_test_files() 