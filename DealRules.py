def read_file(path):
    txt = ''
    with open(path, 'r') as f:
        for line in f:
            txt += line
    return txt


def deal_content(content: str):
    result = []
    for line in content:
        if line.startswith('full:') or line.startswith('.regexp:'):
            continue
        else:
            line += f'*.{line}'
        result.append(line)
    return result


def output_file(path: str, content: list):
    with open(path, 'w') as f:
        for line in content:
            f.write(line)


def deal_list(head_path: str, content_path: str, need_head: bool, output_path: str):
    head = read_file(head_path)
    content = read_file(content_path)
    if need_head:
        result = deal_content(f'{head}\n{content}')
    else:
        result = deal_content(content)

    output_file(output_path, result)


deal_list('direct-list-head.txt', 'direct-list.txt', True, r'out/direct-list.txt')
deal_list('proxy-list-head.txt', 'proxy-list.txt', False, r'out/proxy-list.txt')
