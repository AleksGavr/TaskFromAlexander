import time

mass = []
File = 'C:/Text.txt'  # здесь указываем путь к необходимому текстовому файлу
lines = open(File).readlines()
string = [line.rstrip() for line in lines]
for i in string:
    new = i.split()
    mass.append(new)
Array = sum(mass, [])
print(Array)
print('\n')
input("Начинаем?")
print("\n")
m = len(Array)
NewArray = []
lim = 3  # указываем длину строк из которых надо собрать новый массив
i = 0
start = time.time()
while i < m:
    if len(Array[i]) <= lim:
        NewArray.append(Array[i])
    i = i + 1
# print(f'Новый массив соответствующий условиям задачи: {NewArray}')
end = time.time()
print(end - start)
