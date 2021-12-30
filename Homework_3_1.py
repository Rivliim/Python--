def num_translate (eng):
    numbers = {'zero' : 'ноль' ,
               'one' : 'один' ,
               'two' : 'два' ,
               'three' : 'три' ,
               'four' : 'четыре' ,
               'five' : 'пять' ,
               'six' : 'шесть' ,
               'seven': 'семь',
               'eight' : 'восемь' ,
               'nine' : 'девять' ,
               'ten' : 'десять' }
    return  numbers.get(eng , None)

print (num_translate('ten'))
print (num_translate('twenty'))
