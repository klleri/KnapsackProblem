# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24  2019
Refactored on Tue Apr 2 2025

knapsack problem 

Solves the Fractional Knapsack problem using a greedy approach.

Reads item values (yield/rendimento) and weights (peso) from a file,
calculates the value-to-weight ratio, and fills the knapsack
prioritizing items with the highest ratio, allowing fractions of items.

File Format ('knapsack.txt' or specified filename):
Line 1: Number of items (integer) 
Line 2: Knapsack capacity (float or integer)
Line 3 onwards: value weight (space-separated, float or integer)

@author: Lucas
"""
import sys # Used for exiting cleanly on critical errors

def solve_fractional_knapsack(filename="knapsack.txt"):
    """
    Reads knapsack data from a file, calculates the maximum value using
    a greedy approach based on value/weight ratio.

    Args:
        filename (str): The path to the input file.

    Returns:
        float: The maximum total value achievable in the knapsack.
               Returns None if an error occurs during file processing or
               if the input format is invalid.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]

        if len(lines) < 2:
            print(f"Error: File '{filename}' is too short. Needs at least capacity and one item line (or just capacity if no items).")
            return None

        # Read capacity
        try:
            # Use float for capacity to handle potential fractional capacities
            capacity = float(lines[1])
            if capacity < 0:
                print("Error: Knapsack capacity cannot be negative.")
                return None
        except ValueError:
            print(f"Error: Invalid capacity value '{lines[1]}' on line 2.")
            return None

        # Read items and calculate ratios
        items = []
        # Start reading items from the third line (index 2)
        for i, line in enumerate(lines[2:], start=3):
            parts = line.split()
            if len(parts) != 2:
                print(f"Warning: Skipping malformed line {i}: '{line}' - Expected 'value weight'")
                continue
            try:
                value = float(parts[0])
                weight = float(parts[1])

                if weight < 0 or value < 0:
                    print(f"Warning: Skipping line {i}: '{line}' - Value and weight must be non-negative.")
                    continue

                # Handle zero-weight items: If value is positive, they have infinite ratio.
                # We prioritize them if the knapsack has capacity.
                if weight == 0:
                    if value > 0:
                        print(f"Info: Taking item from line {i} with value {value} and zero weight.")
                        items.append({'value': value, 'weight': 0, 'ratio': float('inf'), 'line': i})

                    else:
                         # Zero value, zero weight - ignore
                        continue
                else:
                    ratio = value / weight
                    items.append({'value': value, 'weight': weight, 'ratio': ratio, 'line': i})

            except ValueError:
                print(f"Warning: Skipping invalid numeric data on line {i}: '{line}'")
                continue

        # Sort items by value-to-weight ratio in descending order
        # Items with infinite ratio (zero weight) will naturally come first
        items.sort(key=lambda item: item['ratio'], reverse=True)

        total_value = 0.0
        remaining_capacity = capacity

        # Fill the knapsack greedily
        for item in items:
            if remaining_capacity <= 0:
                # Knapsack is full, no need to check more items
                break

            if item['weight'] == 0 and item['value'] > 0:
                 total_value += item['value']
                 # Doesn't consume capacity, so continue to next item.

            elif item['weight'] <= remaining_capacity:
                # Take the whole item if it fits
                print(f"Taking item from line {item['line']} (Value: {item['value']}, Weight: {item['weight']})")
                total_value += item['value']
                remaining_capacity -= item['weight']
            else:
                # Take a fraction of the item if only part fits
                fraction = remaining_capacity / item['weight']
                value_taken = item['value'] * fraction
                print(f"Taking {fraction*100:.2f}% of item from line {item['line']} (Value: {value_taken:.2f}, Weight: {remaining_capacity:.2f})")
                total_value += value_taken
                remaining_capacity = 0 # Knapsack is now full
                break

        return total_value

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None

# Main execution block
if __name__ == "__main__":
    input_filename = 'knapsack.txt' # Or get from command line arguments

    # Create a dummy 'knapsack.txt' file for testing if it doesn't exist
    import os
    if not os.path.exists(input_filename):
        print(f"Creating a sample '{input_filename}' for testing.")
        with open(input_filename, 'w', encoding='utf-8') as f:
            f.write("3\n")       # Number of items (example)
            f.write("50\n")      # Capacity (example)
            f.write("60 10\n")   # Item 1: value 60, weight 10 (ratio 6)
            f.write("100 20\n")  # Item 2: value 100, weight 20 (ratio 5)
            f.write("120 30\n")  # Item 3: value 120, weight 30 (ratio 4)
            #f.write("50 0\n")    # Example: Item with zero weight

    max_knapsack_value = solve_fractional_knapsack(input_filename)

    if max_knapsack_value is not None:
        print("-" * 30)
        print(f"The maximum value achievable in the knapsack is: {max_knapsack_value:.2f}")
        print("-" * 30)
    else:
        print("Could not calculate the knapsack value due to errors.")
        sys.exit(1) 
