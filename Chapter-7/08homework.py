
while True:
    print("=======================")
    print("♥ welcome Hogwarts ! ♥")
    print("=======================")
    func01 = ["♥ 1 . 添加学生", "♥ 2 . 查看学生", "♥ 3 . 修改学生信息", "♥ 4 . 删除学生", "♥ 5 . 返回"]
    func02 = ["♥ 1 . 查看所有学生","♥ 2 . 按姓名查找","♥ 3 . 按学号查找","♥ 4 . 返回"]
    for i in func01:
        print(i)
    chooise = int(input("请选择1-5："))
    if chooise == 1:
        student_num = 0
        dict01 = []
        while chooise == 1:
            student_num = student_num + 1
            name = str(input("请输入学生姓名："))
            age = int(input("请输入学生年龄："))
            Tel = int(input("请输入学生电话："))
            new_dict2 ={"学号":0,"姓名":0,"年龄":0,"电话":0}
            new_dict2["学号"] = student_num
            new_dict2["姓名"] = name
            new_dict2["年龄"] = age
            new_dict2["电话"] = Tel
            # new_dict = ("学号:00%d  姓名:%s  年龄:%d  电话：%d "%(student_num,name,age,Tel))
            dict01.append(new_dict2)
            print("添加成功")
            msg1 = input("1 继续\n2 返回")
            if msg1 == "1":
                continue
            else:
                break
    elif chooise == 2:
        for i in dict01:
            print(i)
        for j in func02:
            print(j)
        chooise2 = input("请选择1-4：")
        while chooise2 == 4:
            break
    elif chooise == 3:
        pass




















