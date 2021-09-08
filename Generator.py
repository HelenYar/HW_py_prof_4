import hashlib


def hash_line(path):
    h = hashlib.md5()

    with open(path, encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            h.update(line.encode('utf-8'))
            yield h.hexdigest()


generator = hash_line('input_file.txt')

for item in generator:
    print(item)