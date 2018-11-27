frames_path = '/Users/EthanWang/Discord_Bot/frames.txt'
frame = ''
with open(frames_path, 'r') as file:
    data = file.readlines()
    for line in data:
        frame += line
count = 0
while count < len(data[0].rstrip()):
    frame = 'O'
    print(frame)
    count += 1
