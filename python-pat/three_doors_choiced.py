
import random

# 初始化两种策略的胜利次数
stay_win, switch_win = 0, 0
# 总的次数
sim_rounds = 10000
for i in range(sim_rounds):
    # 初始化
    doors = {
        1: "sheep",
        2: "sheep",
        3: "sheep"
    }
    doors[random.randint(1,3)] = "car"
    # 嘉宾的选择
    choice = random.randint(1,3)
    while True:
        # 主持人的选择
        i = random.randint(1,3)
        if i != choice and doors[i] == "sheep":
            # 删除主持人的选择
            doors.pop(i)
            break
    # 最终结果
    # 坚持选择
    if doors[choice] == 'car':
        stay_win += 1.0
    # 改变选择
    else:
        switch_win += 1.0
# 打印
print("stay win probability: %.2f%%" %(stay_win/sim_rounds*100))
print("switch win probability: %.2f%%" %(switch_win/sim_rounds*100))
