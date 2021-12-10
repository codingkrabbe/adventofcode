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


def get_completion_score(opening_element: str) -> int:
    if opening_element == '(':
        return 1
    elif opening_element == '[':
        return 2
    elif opening_element == '{':
        return 3
    elif opening_element == '<':
        return 4
    else:
        print('Something went wrong. Tried to get completion score for "' + opening_element + '"')


def parse_elements(elements: list):
    top_elem = None
    stack = []
    for element in elements:
        current_elem = element
        if len(stack) == 0:
            stack.append(current_elem)
        else:
            stack = update_stack(stack, top_elem, current_elem)
        top_elem = stack[-1]
    return stack


def get_final_score(scores):
    scores.sort()
    return scores[len(scores) // 2]


def main():
    lines = open('input.txt', 'r').readlines()
    incomplete_lines = lines.copy()
    total_completion_scores = []
    for line in lines:
        elements = list(line.strip())
        try:
            _ = parse_elements(elements)
        except ChunkParseError:
            incomplete_lines.remove(line)
    for line in incomplete_lines:
        elements = list(line.strip())
        stack = parse_elements(elements)
        total_completion_score = 0
        while len(stack) > 0:
            elem = stack.pop()
            total_completion_score = 5 * total_completion_score + get_completion_score(elem)
        total_completion_scores.append(total_completion_score)
    final_score = get_final_score(total_completion_scores)
    print('Final completion score: ' + str(final_score))



if __name__ == '__main__':
    main()
