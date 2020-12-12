import datetime
import hashlib
from time import sleep


def gen_number(first, last):
    if first != 0 and last != 0:
        gen_list = [i for i in range(first, last + 1)]
        for ind, val in enumerate(gen_list):
            sleep(0.1)
            time_now = datetime.datetime.now()
            hash_time = hashlib.md5(str(time_now).encode())
            hash_bytes = bytes(hash_time.hexdigest(), encoding="utf_8")[:1]
            if hash_bytes > b'8':
                element = gen_list.pop(ind)
                gen_list.insert(ind + 1, element)
            else:
                element = gen_list.pop(ind)
                gen_list.insert(ind - 1, element)
        gen_dict = {f'elem_{i}': i for i in gen_list}
        return gen_list, gen_dict


print(gen_number(1, 18))
