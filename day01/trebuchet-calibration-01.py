import re

# the file path
file_path = './input'

regex = re.compile(r'^\D*(\d).*?(\d)?\D*$')

calibration_value = 0

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read and print each line
    line_nb = 0
    for line in file:
        line_nb += 1
        result = regex.match(line.strip())
        if result:
            first_digit = result.group(1)
            last_digit = result.group(2) or first_digit
            print(f"{line_nb} Current calibration : {first_digit}{last_digit}")
            calibration_value += int(first_digit)*10 + int(last_digit)

print(f"==> Sum of all the calibration values : {calibration_value}")
