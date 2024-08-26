# 定义帮扶措施的字典
support_measures = {
    "一级帮扶": {
        "心理": "开展心理讲座，谈心谈话",
        "学业": "开展线上线下学业辅导",
        "经济": "发放学习大礼包，实现微心愿"
    },
    "二级帮扶": {
        "心理": "开展心理辅导和转介医院",
        "学业": "开展生涯规划与指导和高校研学",
        "经济": "打造爱心小屋，发放助学金"
    }
}

# 问答流程函数
def ask_question(prompt):
    while True:
        answer = input(prompt + " (是/否): ").strip()
        if answer == "是":
            return 1
        elif answer == "否":
            return 0
        else:
            print("请输入有效的答案: 是 或 否。")

# 收集心理问题的回答
def collect_mental_health_data():
    anxiety = ask_question("最近一段时间，你是否经常感到焦虑、紧张或不安？")
    depression = ask_question("有没有经常感到抑郁、悲伤或失落？")
    irritability = ask_question("是否容易发脾气或情绪激动？")
    happiness = ask_question("最近有没有经历过特别开心或兴奋的事情？")
    return {
        'Anxiety': anxiety,
        'Depression': depression,
        'Irritability': irritability,
        'Happiness': happiness
    }

# 收集学业问题的回答
def collect_academic_data():
    grades_qualified = ask_question("成绩是否合格？")
    truancy = ask_question("是否有厌学逃学情绪？")
    return {
        'Grades_Qualified': grades_qualified,
        'Truancy': truancy
    }

# 收集经济问题的回答
def collect_economic_data():
    while True:
        try:
            family_income = int(input("家庭月收入多少？: ").strip())
            return {'Family_Income': family_income}
        except ValueError:
            print("请输入有效的数字。")

# 评估心理状况
def evaluate_mental_health(mental_data):
    mental_issues = [mental_data['Anxiety'], mental_data['Depression'], mental_data['Irritability'], mental_data['Happiness']]
    if sum(mental_issues) >= 2:
        return "二级帮扶", support_measures["二级帮扶"]["心理"]
    else:
        return "一级帮扶", support_measures["一级帮扶"]["心理"]

# 评估学业状况
def evaluate_academic_status(academic_data):
    if academic_data['Grades_Qualified'] == 0:
        return "一级帮扶", support_measures["一级帮扶"]["学业"]
    elif academic_data['Truancy'] == 1:
        return "二级帮扶", support_measures["二级帮扶"]["学业"]
    else:
        return "无需帮扶", None

# 评估经济状况
def evaluate_economic_status(economic_data):
    if economic_data['Family_Income'] < 750:
        return "二级帮扶", support_measures["二级帮扶"]["经济"]
    elif 750 <= economic_data['Family_Income'] < 1500:
        return "一级帮扶", support_measures["一级帮扶"]["经济"]
    else:
        return "无需帮扶", None

# 综合评估
def evaluate_child(mental_data, academic_data, economic_data):
    mental_evaluation = evaluate_mental_health(mental_data)
    academic_evaluation = evaluate_academic_status(academic_data)
    economic_evaluation = evaluate_economic_status(economic_data)

    return {
        "心理帮扶等级": mental_evaluation[0],
        "心理帮扶措施": mental_evaluation[1],
        "学业帮扶等级": academic_evaluation[0],
        "学业帮扶措施": academic_evaluation[1],
        "经济帮扶等级": economic_evaluation[0],
        "经济帮扶措施": economic_evaluation[1]
    }

# 主程序
def main():
    print("请根据以下问题回答“是”或“否”。\n")

    # 收集各项数据
    mental_data = collect_mental_health_data()
    academic_data = collect_academic_data()
    economic_data = collect_economic_data()

    # 综合评估
    evaluation_result = evaluate_child(mental_data, academic_data, economic_data)

    # 打印评估结果
    print("\n评估结果:")
    for key, value in evaluation_result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
