files_lenght = {}

for n in range(1,4):
    file_name = 'task 3/' + str(n) +'.txt'    
    with open(file_name) as file:
        count = 0
        for line in file:
            count += 1
    files_lenght[file_name] = count

files_lenght = dict(sorted(files_lenght.items(), key=lambda item: item[1]))
print(files_lenght)

with open('task 3/result.txt', 'w+') as file_result:
    for file_name in files_lenght:
        with open(file_name) as file:
            file_result.write(file_name + '\n')
            file_result.write(str(files_lenght[file_name]) + '\n')
            for line in file:
                file_result.write(line)

            



