from time import sleep
from datetime import datetime
import threading


def write_words(word_count, file_name):

    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now() # начало выполнения программы засекаем

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
time_func = time_end - time_start
print(f'Время работы функции {time_func}')

time_start = datetime.now()

thr_first = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thr_fourth = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end = datetime.now()
time_func1 = time_end - time_start
print(f'Время выполнения потоков {time_func1}')
