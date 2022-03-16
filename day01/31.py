math = ["张三", "田七", "李四", "马六"]
english = ["李四", "王五", "田七", "陈八"]
art = ["陈八", "张三", "田七", "赵九"]
music = ["李四", "田七", "马六", "赵九"]

print(set(math).intersection(set(music)))
print(set(math).intersection(set(english), set(music)))
print(set(math).intersection(set(english), set(art), set(music)))
print(set(math).difference(set(music)))
print(len(set(math).union(set(music))))

