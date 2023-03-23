def max1(a,b):
    if a>b:
        return a
    # else:   не обязательно, потому что return прекращает работу программы
    return b
# для того, чтобы импортировать модуль
import module     #название файла
module.max1(5,9)     # . + имя функции

from module import max1
print (max1(5,9))

from module import * # импортитровать все функции из модуля 

import module as m      # сократить имя
print (m.max1(5,9))

