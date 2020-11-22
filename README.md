# How it work 
## Запускаем скрипт без параметров и получаем вывод работы в консоль 
```
python calc2.py 1 7
```
## Запускаем скрипт с параметром **--file $filename** для сохранения работы в файл 
```
python calc2.py 1 7 --file logs.txt
```
Появляется файл logs.txt с результатом работы скрипта
## Запускаем скрипт с параметром **--file $filename --append** для того чтобы файл не перезаписался а изменения добавились в конец
```
python calc2.py 1 7 --file logs.txt --append
```
