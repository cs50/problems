#!/usr/bin/env python3
"""
Simple Dynamic DNA Test Generator
Generates dynamic.csv and dynamic.txt with random STR sequences.
Creates 2n-1 persons total (including Philosopher) where n = number of STRs.
Pattern: Person1(1 match), Person2(2 matches), ..., Philosopher(n matches), ..., Person(2n-1)(1 match)
Creates a symmetric pyramid pattern around the Philosopher.
"""

import random
import csv
import sys
import os

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

def generate_test_files(csv_filename, txt_filename):
    """Generate CSV and TXT files with random STRs."""

    csv_output_path = os.path.join('databases', csv_filename)
    txt_output_path = os.path.join('sequences', txt_filename)
    
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
    
    # Create profiles with symmetric pattern around Philosopher
    profiles = []
    num_strs = len(str_sequences)
    person_counter = 1
    
    # First: Create n-1 profiles with progressive matching (1,2,3,...,n-1)
    for i in range(num_strs - 1):
        profile = {'name': f'Person{person_counter}'}
        matching_count = i + 1  # Person1 matches 1, Person2 matches 2, etc.
        
        for j, str_seq in enumerate(str_sequences):
            if j < matching_count:
                # Use the same value as philosopher for matching positions
                profile[str_seq] = philosopher_counts[str_seq]
            else:
                # Use random value for non-matching positions
                profile[str_seq] = random.randint(5, 30)
        profiles.append(profile)
        person_counter += 1
    
    # Add Philosopher profile that matches the sequence exactly
    philosopher_profile = {'name': 'Philosopher'}
    philosopher_profile.update(philosopher_counts)
    profiles.append(philosopher_profile)
    
    # Second: Create n-1 more profiles with decreasing matching (n-1,n-2,n-3,...,1)
    for i in range(num_strs - 1):
        profile = {'name': f'Person{person_counter}'}
        matching_count = (num_strs - 1) - i  # Decreasing: n-1, n-2, n-3, ..., 1
        
        for j, str_seq in enumerate(str_sequences):
            if j < matching_count:
                # Use the same value as philosopher for matching positions
                profile[str_seq] = philosopher_counts[str_seq]
            else:
                # Use random value for non-matching positions
                profile[str_seq] = random.randint(5, 30)
        profiles.append(profile)
        person_counter += 1
    
    # Generate CSV file
    with open(csv_output_path, 'w', newline='') as csvfile:
        fieldnames = ['name'] + str_sequences
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for profile in profiles:
            writer.writerow(profile)
    
    # Generate DNA sequence using the philosopher_counts
    dna_sequence = generate_dna_sequence_with_strs(philosopher_counts)
    
    # Save DNA sequence
    with open(txt_output_path, 'w') as f:
        f.write(dna_sequence)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 generate_dynamic_test.py <csv_filename> <txt_filename> <seed>")
        print("Example: python3 generate_dynamic_test.py arg-1.csv arg-2.txt 1980")
        sys.exit(1)
    
    csv_filename = sys.argv[1]
    txt_filename = sys.argv[2]
    random.seed(int(sys.argv[3]))
    generate_test_files(csv_filename, txt_filename)