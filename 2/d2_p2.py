import os

def is_ascending_perfect(line):
    """
    Checks if a line is perfectly ascending with each subsequent number
    being between 1 and 3 greater than the previous one.
    """
    if not line or len(line) == 1:
        return True

    prev = line[0]
    for i in range(1, len(line)):
        num = line[i]
        if not (1 <= (num - prev) <= 3):
            return False
        prev = num
    return True

def is_descending_perfect(line):
    """
    Checks if a line is perfectly descending with each subsequent number
    being between 1 and 3 less than the previous one.
    """
    if not line or len(line) == 1:
        return True

    prev = line[0]
    for i in range(1, len(line)):
        num = line[i]
        if not (1 <= (prev - num) <= 3): # Corrected condition for descending
            return False
        prev = num
    return True

safe_reports_count = 0
data = []

# Construct the correct path to the input file
file_path = '2/d2_input.txt'

try:
    with open(file_path, 'r') as file:
        for line_str in file:
            line_str = line_str.strip()
            if not line_str: # Skip empty lines
                continue
            intline = [int(number) for number in line_str.split()]
            data.append(intline)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please ensure it exists.")
    exit()

for original_line in data:
    is_current_line_safe = False

    # 1. Check if the original line is safe without any removal
    if len(original_line) <= 1: # A line with 0 or 1 element is always safe
        is_current_line_safe = True
    elif sorted(original_line) == original_line:
        if is_ascending_perfect(original_line):
            is_current_line_safe = True
    elif sorted(original_line, reverse=True) == original_line: # Check if it's perfectly descending
        if is_descending_perfect(original_line):
            is_current_line_safe = True

    if is_current_line_safe:
        safe_reports_count += 1
        continue # Move to the next report

    # 2. If not safe, try removing one level
    for i in range(len(original_line)):
        temp_line = original_line[:i] + original_line[i+1:]

        if len(temp_line) <= 1: # A line with 0 or 1 element is always safe
            is_current_line_safe = True
            break
        elif sorted(temp_line) == temp_line:
            if is_ascending_perfect(temp_line):
                is_current_line_safe = True
                break
        elif sorted(temp_line, reverse=True) == temp_line:
            if is_descending_perfect(temp_line):
                is_current_line_safe = True
                break
    
    if is_current_line_safe:
        safe_reports_count += 1

print(safe_reports_count)