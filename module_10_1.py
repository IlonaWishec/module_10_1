import threading
import time

def write_words(word_count, file_name):
    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'Какое-то слово № {i} \n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

started = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

ended = time.time()
print(f'Работа функций {ended - started} секунд(ы)')

started_threads = time.time()

threads = []
threads.append(threading.Thread(target=write_words, args=(10, 'example5.txt')))
threads.append(threading.Thread(target=write_words, args=(30, 'example6.txt')))
threads.append(threading.Thread(target=write_words, args=(200, 'example7.txt')))
threads.append(threading.Thread(target=write_words, args=(100, 'example8.txt')))


for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

ended_threads = time.time()
print(f'Работа потоков: {ended_threads - started_threads}')
# Завершилась запись в файл example1.txt
# Завершилась запись в файл example2.txt
# Завершилась запись в файл example3.txt
# Завершилась запись в файл example4.txt
# Работа функций 34.517552614212036 секунд(ы)
# Завершилась запись в файл example5.txt
# Завершилась запись в файл example6.txt
# Завершилась запись в файл example8.txt
# Завершилась запись в файл example7.txt
# Работа потоков: 20.30927085876465