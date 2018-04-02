# /usr/bin/env python3

# coding:utf-8



dict = {

    "你好": "你好",

    "很高兴见到您": "我也很能高兴见到你",

    "你喜欢吃什么水果 ": "我喜欢橘子",

    "你今年多大了": "27 岁了",

    "你很漂亮": "谢谢"

    }

flag = ('c')

work = True

print('你好，我是python机器人')

print('你有时间跟我聊聊吗')

while flag == 'c' or 't':

    flag = input("你可以选择是否跟我聊天(c),还是决定练习下我的对话能力(t),或者让我推下(l)?(c/t/l)")

    if flag == "t":

        question = input("请输入你想问的:")

        answer = input("请输入问题答案:")

        dict[str(question)] = str(answer)

        print("学习成功")

        print("现在我已经学会了%d个问题" % len(dict))

        continue

    elif flag == 'c':

        if len(dict) == 0:

            print("现在我还不会回答任何问题，请先让我学习:")

            continue

        chat_word = input("谢谢你跟我聊天，你想对我说点什么?:")

        for key in sorted(dict.keys()):

            if str(chat_word) == key:

                work = True

                print(dict[key])

                break

            else:

                work = False

        if work == False:

            print("Sorry，这个问题我回答不上来")

            work = True

    elif flag == 'l':

        print("好的，那我们下次再聊")

        break

    else:

        print("请输入提示指令")

        continue