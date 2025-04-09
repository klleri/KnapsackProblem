# Fractional Knapsack Solver

This Python script solves the **Fractional Knapsack Problem** using a greedy algorithm. It determines the maximum value of items that can be included in a knapsack of a given capacity, allowing items to be taken fractionally. The algorithm prioritizes items with the highest value-to-weight ratio.

## Features

* Solves the Fractional Knapsack problem.
* Uses a greedy approach based on the highest value/weight ratio.
* Reads input data (capacity, item values, and weights) from a text file.
* Handles fractional amounts of items.
* Includes basic error handling for file issues and invalid data formats.
* Correctly handles items with zero weight (treats them as having infinite value density, taking them first if they have positive value).
* Provides informative console output detailing which items (or fractions) are taken.
* Written in Python 3, focusing on clarity and efficiency.

## Input File Format

The script reads data from a text file (default: `knapsack.txt`). The file must be UTF-8 encoded and follow this format:

1.  Number of items (integer). _(Note: This number isn't strictly used by the algorithm itself but is expected in the format)._
2.  Knapsack capacity (integer or float). Must be non-negative.
3.  Each line represents an item, containing its `value` and `weight`, separated by a space (both should be non-negative integers or floats).

## How to Run

1.  **Save the code:** Save the refactored Python code as a `.py` file (e.g., `knapsack_solver.py`).
2.  **Prepare the input file:** Create a text file (e.g., `knapsack.txt`) in the same directory with the format described above. If `knapsack.txt` doesn't exist, the script will create a sample file for testing when run without arguments.
3.  **Execute from the terminal:**

    ```bash
    python knapsack_solver.py [input_filename]
    ```
