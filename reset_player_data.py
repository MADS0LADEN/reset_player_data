import os

folder = 'PlayerData'

n = 0
deleted = 0
kept = 0

for filename in os.listdir(folder):
    if filename.__contains__('.ignore'):
        continue
    file_path = os.path.join(folder, filename)
    with open(os.path.join(folder, filename), 'r') as file:
        lines = file.readlines()
        line2 = lines[2].replace('\n', '')

        if line2 == '0':
            deleted +=1
            if os.path.isfile(file_path):
                status = 'Deleted'
                os.remove(file_path)

        else:
            kept +=1
            wfile = open(os.path.join(folder, filename), 'w')
            if wfile.writable:
                status = 'Changed'
                lines[1] = '0\n'
                wfile.writelines(lines)
                wfile.close
    
        n+=1
    print(f'#{n} {filename}: {status}')

print(f'Deleted: {deleted}\nKept: {kept}\nAmount: {n}')