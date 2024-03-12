import time

from transliterate import translit
import os
from glob import glob

dic = {'Ь': '', 'ь': '', 'Ъ': '', 'ъ': '', 'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
       'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'E', 'ё': 'e', 'Ж': 'h', 'ж': 'h',
       'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i', 'Й': 'I', 'й': 'i', 'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l',
       'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r',
       'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'h', 'х': 'h',
       'Ц': 'c', 'ц': 'c', 'Ч': 'h', 'ч': 'h', 'Ш': 'h', 'ш': 'h', 'Щ': 'h', 'щ': 'h', 'Ы': 'Y',
       'ы': 'y', 'Э': 'E', 'э': 'e', 'Ю': 'u', 'ю': 'u', 'Я': 'a', 'я': 'a'}

_files = glob(os.path.join('./', '*.yaml'))
for i in _files:
    with open(i, 'r+') as file:
        text = file.read()
        file.truncate(0)
        file.close()
    for j in dic.items():
        text = text.replace(j[0], j[1])
    time.sleep(2)
    with open(i, 'r+', encoding='UTF-8') as file:
        file.write(text)
