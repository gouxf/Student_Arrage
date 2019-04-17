#!/usr/bin/python3
import time
import json

# 1、打印提示
print("*" * 30)
print("学生寝室管理系统V1.0")
print("1、添加一个学生信息")
print("2、删除一个学生信息")
print("3、修改一个学生信息")
print("4、查询一个学生信息")
print("5、显示所有学生信息")
print("6、打印各寝室人员列表")
print("7、调整寝室人员分配")
print("8、退出系统")
print("*" * 30)
dic = {"N_100":0, "N_101":0, "N_102":0, "N_200":0, "N_201":0, "N_202":0}
student_list = [] #定义一个空列表，存储字典数据
student_list.append(dic)
print(student_list)
arrang_num = " "

def LuRu():
    new_id = str(input("请输入学号："))
    new_name = str(input("请输入姓名："))
    new_age = int(input("请输入年龄："))
    new_sex = str(input("请输入性别（男/女）："))
    # 定义一个字典存储学生信息
    student_info = {}
    student_info["id"] = new_id
    student_info["name"] = new_name
    student_info["age"] = new_age
    student_info["sex"] = new_sex
    ishand = str(input("是否手动安排寝室号(y/n):"))
    if ishand == 'y':
        if new_sex == "男":
            arrang_num = str(input("请输入寝室号（100/101/102）："))
        if new_sex == "女":
            arrang_num = str(input("请输入寝室号（200/201/202）："))
        student_info["num"] = arrang_num
        if arrang_num == "100": student_list[0]["N_100"] = student_list[0]["N_100"] + 1
        if arrang_num == "101": student_list[0]["N_101"] = student_list[0]["N_101"] + 1
        if arrang_num == "102": student_list[0]["N_102"] = student_list[0]["N_102"] + 1
        if arrang_num == "200": student_list[0]["N_200"] = student_list[0]["N_200"] + 1
        if arrang_num == "201": student_list[0]["N_201"] = student_list[0]["N_201"] + 1
        if arrang_num == "202": student_list[0]["N_202"] = student_list[0]["N_202"] + 1
        print(student_list)
    if ishand == 'n':
        if new_sex == "男":
            if student_list[0]["N_100"] < 4:
                arrang_num = "100"
                student_list[0]["N_100"] += 1
            elif student_list[0]["N_101"] < 4:
                arrang_num = "101"
                student_list[0]["N_101"] += 1
            elif student_list[0]["N_102"] < 4:
                arrang_num = "102"
                student_list[0]["N_102"] += 1
            else:
                print("已经没有多余的寝室安排！")
        if new_sex == "女":
            if student_list[0]["N_200"] < 4:
                arrang_num = "200"
                student_list[0]["N_200"] += 1
            elif student_list[0]["N_201"] < 4:
                arrang_num = "201"
                student_list[0]["N_201"] += 1
            elif student_list[0]["N_202"] < 4:
                arrang_num = "202"
                student_list[0]["N_202"] += 1
            else:
                print("已经没有多余的寝室安排！")
        print("ok")
        print(student_list)
    else:
        pass
    student_info["num"] = arrang_num
    student_list.append(student_info)
    with open("hello.txt", "w", encoding='utf-8') as fp:
        fp.write(json.dumps(student_list, indent=50))
    print("已完成录入")
    print(student_list)

def DelStu():
    del_id = str(input("请输入要删除学生的学号："))
    del_flag = 0  # 0表示无该学生信息，1表示有该学生信息
    count = 0
    student_list_tmp = []
    while 1:
        with open(r"hello.txt", "r") as f:
            student_list = json.load(f)
        for student in student_list:
            if count == 0:
                student_list_tmp.append(student)
                count = 1
                continue
            if del_id == student["id"]:
                print("学号：%s\t姓名：%s\t年龄：%d\t性别：%s\t寝室号：%s\t" % (
                student["id"], student["name"], student["age"], student["sex"], student["num"]))
                isDel = str(input("确定删除该学生信息吗？（y/n)："))
                if isDel == "y":
                    count = 0
                    for i in student_list:
                        if count == 0:
                            if student["num"] == "100": student_list[0]["N_100"] -= 1
                            if student["num"] == "101": student_list[0]["N_101"] -= 1
                            if student["num"] == "102": student_list[0]["N_102"] -= 1
                            if student["num"] == "200": student_list[0]["N_200"] -= 1
                            if student["num"] == "201": student_list[0]["N_201"] -= 1
                            if student["num"] == "202": student_list[0]["N_202"] -= 1
                            count = 1
                            continue
                        if i["id"] != del_id:
                            student_list_tmp.append(i)
                    student_list = student_list_tmp
                    with open("hello.txt", "w", encoding='utf-8') as fp:
                        fp.write(json.dumps(student_list, indent=50))
                    print("成功删除")
                del_falg = 1
                break
            else:
                del_id = str(input("请重新输入，按0退出："))
        if del_flag == 0:
            break

def ChaStu():
    with open(r"hello.txt", "r") as ft:
        student_list = json.load(ft)
    change_id = int(input("输入被修改学生的学号："))
    change_flag = 0
    while 1:
        count = 0
        for i in student_list:
            if count == 0:
                count = 1
                continue
            if change_id == i["id"]:
                print("学号：%s\t姓名：%s\t年龄：%d\t性别：%s\t寝室号：%s\t" % (
                    i["id"], i["name"], i["age"], i["sex"], i["num"]))
                change_n = int(input("1、修改姓名\n2、修改年龄"))
                if change_n == 1: pass
                if change_n == 2: pass
            change_flag = 1
            break
        if change_flag == 0:
            change_id = int(input("输入错误，重新输入!(按0退出）："))
        if change_id == 0:
            break

def SerStu():
    with open(r"hello.txt", "r") as ft:
        student_list = json.load(ft)
    query_id = str(input("请输入学号："))
    id_flag = 0  # 0代表没有找到，1代表找到
    count = 0
    for student in student_list:
        if count == 0:
            count = 1
            continue
        if student["id"] == query_id:
            print("学号：%s\t姓名：%s\t年龄：%d\t性别：%s\t寝室号：%s\t" % (
            student["id"], student["name"], student["age"], student["sex"], student["num"]))
            id_flag = 1
            break
    if id_flag == 0:
        print("很抱歉，没有找到该学生!")
    print()

def DisStu():
    count = 0  # 0代表不打印第一个字典，1代表打印后面的字典
    with open(r"hello.txt", "r") as f:
        student_list = json.load(f)
    if len(student_list) == 1:
        print("无任何学生信息录入！")
        print()
    else:
        for student in student_list:
            if count == 0:
                count = 1
                continue
            print("学号：%s\t姓名：%s\t年龄：%d\t性别：%s\t寝室号：%s\t" % (
            student["id"], student["name"], student["age"], student["sex"], student["num"]))

def PriStu():
    with open(r"hello.txt", "r") as ft:
        student_list = json.load(ft)
    find_num = str(input("请输入查询的寝室号（100/101/102/200/201/202）："))
    num_flag = 0  # 0代表输入错误，1代表输入正确
    while 1:
        count = 0
        if find_num in "100, 101, 102, 200, 201, 202":
            print("%s寝室人员列表" % (find_num))
            for student in student_list:
                if count == 0:
                    count = 1
                    continue
                if student["num"] == find_num:
                    print("学号：%s\t姓名：%s\t年龄：%d\t性别：%s\t寝室号：%s\t" % (
                    student["id"], student["name"], student["age"], student["sex"], student["num"]))
                    num_flag = 1
                else:
                    pass
            if num_flag == 0:
                print("该寝室未安排学生入住")
            break
        else:
            find_num = str(input("输入错误!请重新输入...\n请输入查询的寝室号（100/101/102/200/201/202）："))

def AdjStu():
    s1_flag = 0
    s2_flag = 0
    count = 0
    print("***********调整寝室人员分配***********")
    print("1、将学生分配到另外寝室\n2、将两个学生寝室对调")
    a_n = int(input("输入寝室调配方式："))
    with open("hello.txt", "r") as f:
        student_list = json.load(f)
    if a_n == 1:
        a_s1 = str(input("请输入学生的学号："))
        for student in student_list:
            if count == 0:
                count = 1
                print("test")
                continue
            if student["id"] == a_s1:
                s1_flag = 1
                print("学号：%s\t姓名：%s\t年龄：%d\t性别：%s\t寝室号：%s\t" % (
                student["id"], student["name"], student["age"], student["sex"], student["num"]))
                if student["sex"] == "男":
                    print("100寝室已有%d人，101寝室已有%d人，102寝室已有%d人" % (
                    student_list[0]["N_100"], student_list[0]["N_101"], student_list[0]["N_102"]))
                    if student["num"] == "100": student_list[0]["N_100"] -= 1
                    if student["num"] == "101": student_list[0]["N_101"] -= 1
                    if student["num"] == "102": student_list[0]["N_102"] -= 1
                    if student["num"] == "200": student_list[0]["N_100"] -= 1
                    if student["num"] == "201": student_list[0]["N_201"] -= 1
                    if student["num"] == "202": student_list[0]["N_202"] -= 1
                    s1_num = str(input("请输入要调配到的寝室:"))
                    if s1_num == "100":
                        student_list[0]["N_100"] += 1
                        student["num"] = "100"
                        break
                    if s1_num == "101":
                        student_list[0]["N_101"] += 1
                        student["num"] = "101"
                        break
                    if s1_num == "102":
                        student_list[0]["N_102"] += 1
                        student["num"] = "102"
                        break
                if student["sex"] == "女":
                    print("200寝室已有%d人，201寝室已有%d人，202寝室已有%d人" % (
                    student_list[0]["N_200"], student_list[0]["N_201"], student_list[0]["N_202"]))
                    s1_num = str(input("请输入要调配到的寝室:"))
                    if s1_num == "200":
                        student_list[0]["N_200"] += 1
                        student["num"] = "200"
                        break
                    if s1_num == "201":
                        student_list[0]["N_201"] += 1
                        student["num"] = "201"
                        break
                    if s1_num == "202":
                        student_list[0]["N_202"] += 1
                        student["num"] = "202"
                        break
                print("寝室号输入错误")
        if s1_flag == 0:
            print("很抱歉，没有找到该学生!")
    if a_n == 2:
        s1_flag = 0
        s2_flag = 0
        a_s1 = str(input("请输入学生1的学号："))
        while 1:
            count = 0
            for student in student_list:
                if count == 0:
                    count = 1
                    continue
                if a_s1 == student["id"]:
                    s1_num = student["num"]
                    s1_flag = 1
                    break
            if s1_flag == 0:
                print("该学生不存在！")
                a_s1 = str(input("请输入学生1的学号："))
        a_s2 = str(input("请输入学生2的学号："))
        while 1:
            count = 0
            for student in student_list:
                if count == 0:
                    count = 1
                    continue
                if a_s2 == student["id"]:
                    s2_num = student["num"]
                    s2_flag = 1
                    break
            if s1_flag == 0:
                print("该学生不存在！")
                a_s2 = str(input("请输入学生2的学号："))
        for student in student_list:
            if student["id"] == a_s1:
                student["num"] = s2_num
            if student["id"] == a_s2:
                student["num"] = s1_num
    with open("hello.txt", "w") as fp:
        fp.write(json.dumps(student_list, indent=50))
while True:
    #2、获取用户输入
    num = int(input("请输入要进行操作的序号(1~8)："))
    while num not in range(1, 9):
        num = int(input("该选项不存在，请重选："))
    #3、根据用户输入进入相应的功能
    if num == 1:
        #3.1、录入新的学生信息
        LuRu()
    if num == 2:
        #3.2、删除一个学生信息
        DelStu()
    if num == 3:
        #3.3、修改一个学生信息
        ChaStu()
    if num == 4:
        #3.4、查询一个学生信息
        SerStu()
    if num == 5:
        #3.5、显示所有学生信息
        DisStu()
    if num == 6:
    #3.6、打印各寝室人员列表
        PriStu()
    if num == 7:
    #3.7、调整寝室人员分配
        AdjStu()
    if num == 8:
    #3.8、退出系统
        break