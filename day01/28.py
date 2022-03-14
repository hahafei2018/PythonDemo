# dict1 = {
#     "张三": 2,
#     "田七": 4,
#     "李四": 3,
#     "马六": 2,
#     "王五": 1,
#     "陈八": 2,
#     "赵九": 2
# }
# for i in dict1.items():
#     if i[1] == 2:
#         print(i[0])


city = {
    "北京": {
        "东城": "景点",
        "朝阳": "娱乐",
        "海淀": "大学"
    },
    "深圳": {
        "罗湖": "老城区",
        "南山": "IT男聚集",
        "福田": "华强北"
    },
    "上海": {
        "黄浦": "xxxx",
        "徐汇": "xxxx",
        "静安": "xxxx"
    }
}

print(city["北京"]["东城"])

city["北京"]["东城"] = "故宫在这"
city["北京"]["昌平"] = "传智在这"
city["北京"]["海淀"] = ["清华", "北大", "北邮"]
city["北京"]["海淀"].append("北影")

for index, i in enumerate(city["北京"]):
    print(index+1, i)

for index, i in enumerate(city["北京"]["海淀"]):
    print(index+1, i)


