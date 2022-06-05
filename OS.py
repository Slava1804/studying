import os
import subprocess

a = int(input('0 - Узнать имя вашей операционной системы.'
'\n1 - Запускает командную строку.'
'\n2 - Открывает искомый файл.'
'\n3 - Создать текстовый файл.'
'\n4 - Создать любой файл(с указанием расширения).'      
'\n5 - Создание директорий.'
'\n6 - Удалить файл.'
'\n7 - Узнать размер файла.'
'\n8 - Узнать информацию о файле.'))

if a == 0:
    print(os.name)

if a == 1:
    os.startfile('C:/WINDOWS/system32/cmd.exe')

if a == 2:
    fileName = input('Назовите имя приложения:')
    # open(fileName)
    # os.system(fileName+'.exe')                      ДОДЕЛАТЬ!
    os.startfile('C:/WINDOWS/system32/Discord.exe')

if a == 3:
    nameFile = input('Введите наименование файла: ')
    textFile = open(nameFile + '.txt', 'w')
    ask = int(input('Для записи в файл нажмите: 1 '))
    
    if ask == 1:
        yourText = input('Введите текст, который хотите записать в файл: ')
        textFile.write(yourText)

if a == 4:
    allNameFile = input('Введите наименование файла: ')
    nameExt = input('Укажите расширение: ')
    newFile = open(allNameFile + nameExt, 'w')

if a == 5:
    num = int(input('Если хотите создать одну директорию нажмите- 1, если несколько - 2, если хотите удалить директорию нажмите- 3.'))
    if num == 1:
        nameFolder = input('Введите название директории: ')
        os.mkdir(r'C:/' + nameFolder)
    elif num == 2:
        os.makedirs(r'c:/folder/first/second/third') # ДОДЕЛАТЬ!
    elif num == 3:
        folderDel = input('Напишите название директории, которую хотите удалить: ')
        os.rmdir(r'C:/' + folderDel)

if a == 6:
    wayFile = input('Укажите путь: ')
    askDelete = input('Назовите имя файла, который хотите удалить: ')
    nameExtDel = input('Укажите расширение: ')
    os.remove(r'C:/'+ wayFile + '/' + askDelete + nameExtDel)

if a == 7:
    sizeAsk = input('Укажите название файла: ')
    sizeAskExt = input('Укажите расширение: ')
    print(os.path.getsize('C://' + sizeAsk + sizeAskExt ))

if a == 8:
    inAsk = input('Укажите название файла: ')
    print(os.stat(inAsk + '.txt'))
