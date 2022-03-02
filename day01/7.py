name = input("what is your name: ")
sex = input("what is your sex: ")
job = input("what is your job: ")
phonenum = input("what is your number: ")
print("-"*10+" information of "+name+" "+"-"*10)
# info = '''name: {}
# sex: {}
# job: {}
# phonenum: {}'''.format(name, name, sex, job, phonenum)

info = "name: %s\nsex: %s\njob: %s\nphonenum: %s"
print(info % (name, sex, job, phonenum))
