import re

# the file path
# file_path = './input_test'
file_path = './input'

# == Specific code for part 2
# Match any of the words, with overlappoing ones (the funny...)
regex1 = re.compile(r'(oneight|one|twone|two|threight|three|four|fiveight|five|six|seven|eightwo|eighthree|eight|nineight|nine)')
# build the dict
word_to_digit = {
'one': '1',
'two': '2',
'three': '3',
'four': '4',
'five': '5',
'six': '6',
'seven': '7',
'eight': '8',
'nine': '9',
'oneight': '18',
'twone': '21',
'threight': '38',
'fiveight': '58',
'eightwo': '82',
'eighthree': '83',
'nineight': '98',
}
# replace spelled-out words with digits
def replace_words_with_digits(match):
    digit_word = match.group(1)
    return word_to_digit.get(digit_word)

# == Same regex as for part one
regex2 = re.compile(r'^\D*(\d).*?(\d)?\D*$')

calibration_value = 0

with open(file_path, 'r') as file:
    line_nb = 0 # just for printing line number
    for line in file:
        line_nb += 1
        # transform the line into digits
        # use the substitution func to do the job
        result1 = regex1.sub(replace_words_with_digits, line.strip())
        # if result1:
        #     print(f"{line_nb} Line : {line.strip()}| New line : {result1}")
        # do the job as for part one
        result2 = regex2.match(result1.strip())
        if result2:
            first_digit = result2.group(1)
            last_digit = result2.group(2) or first_digit
            print(f"{line_nb} Current calibration : {first_digit}{last_digit}")
            calibration_value += int(first_digit)*10 + int(last_digit)

print(f"==> Sum of all the calibration values : {calibration_value}")
