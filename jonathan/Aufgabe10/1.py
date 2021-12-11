class Error(Exception):
    pass


class ChunkParseError(Error):
    pass


def update_stack(stack: list, top_elem: str, element: str) -> list:
    if matching_pair(top_elem, element):
        stack.pop()
        return stack
    elif opening_char(element):
        stack.append(element)
        return stack
    else:
        raise ChunkParseError


def matching_pair(first: str, second: str) -> bool:
    if first == '(' and second == ')':
        return True
    elif first == '[' and second == ']':
        return True
    elif first == '{' and second == '}':
        return True
    elif first == '<' and second == '>':
        return True
    else:
        return False


def opening_char(element: str) -> bool:
    return element == '(' or element == '[' or element == '{' or element == '<'


def get_error_score(element: str) -> int:
    if element == ')':
        return 3
    elif element == ']':
        return 57
    elif element == '}':
        return 1197
    elif element == '>':
        return 25137
    else:
        print('Something went wrong. Tried to get error score for "' + element + '"')


def main():
    lines = open('input.txt', 'r').readlines()
    stack = []
    top_elem = None
    current_elem = None
    total_error_score = 0
    for line in lines:
        elements = list(line.strip())
        try:
            for element in elements:
                current_elem = element
                if len(stack) == 0:
                    stack.append(current_elem)
                else:
                    stack = update_stack(stack, top_elem, current_elem)
                top_elem = stack[-1]
        except ChunkParseError:
            total_error_score += get_error_score(current_elem)
    print('Total Error Score: ' + str(total_error_score))


if __name__ == '__main__':
    main()
