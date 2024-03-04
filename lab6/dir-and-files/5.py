list = ['Apple', 'Banana', 'Orange', 'Black']
with open('1.txt', "w") as myfile:
        for c in list:
                myfile.write("%s\n" % c)

content = open('1.txt')
print(content.read())
'''
with open("Sample.txt", "a") as f:
        for i in list:
            f.write(f"\n {i}")
'''