import re

def convert_to_snake(camel):
    snake = re.sub(r'(?<!^)([A-Z])', r'_\1', camel).lower()
    return snake

camel = "ThisFunctionConvertsToSnake"
snake = convert_to_snake(camel)
print(snake)
