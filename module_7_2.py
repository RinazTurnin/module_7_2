from pprint import pprint


def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for string in strings:
            file.write(string + '\n')
    with open(file_name, 'r', encoding='utf-8') as file_two:
        file_position = file_two.tell()
        strings_positions[(1, file_position)] = file_two.readline().replace('\n', '')
        file_position = file_two.tell()
        strings_positions[(2, file_position)] = file_two.readline().replace('\n', '')
        file_position = file_two.tell()
        strings_positions[(3, file_position)] = file_two.readline().replace('\n', '')
        file_position = file_two.tell()
        strings_positions[(4, file_position)] = file_two.readline().replace('\n', '')
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
