my_list = ['1.txt', '2.txt', '3.txt']
result_list = []
for i in my_list:
    my_dict = {}
    with open(i, 'r', encoding='utf-8') as file:
        my_dict['File name'] = i
        lines = file.readlines()
        my_dict['lines_count'] = len(lines)
        my_dict['text'] = lines
    result_list.append(my_dict)
res = sorted(result_list, key=lambda x: x['lines_count'])

with open('new_file.txt', 'w', encoding='utf-8') as file:
    for i in res:
        text = ''.join(i['text']).strip()
        count = f'{i["lines_count"]}\n'
        filename = f'{i["File name"]}\n'
        file.write(f'{filename}{count}{text}\n\n')


