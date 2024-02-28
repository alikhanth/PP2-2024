import re

def convert_to_camel(snake):
    camel = re.sub(r'_([a-z])', lambda match: match.group(1).upper(),snake)
    return camel

snake = "This_function_converts_snake_to_camel"
camel = convert_to_camel(snake)
print(camel)
