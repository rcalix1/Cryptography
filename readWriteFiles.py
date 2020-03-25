file1 = open('input.txt', 'r')

print file1.read()

file1.close()

file2 = open('input.txt','a')

for i in range(10):
    file2.write('data ' + str(i) + '\n'  )


file2.close()
