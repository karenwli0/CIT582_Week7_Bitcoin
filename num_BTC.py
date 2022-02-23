import math


def num_BTC(b):
    layers = int(b / 210000)
    residual = b % 210000
    rewardPerBlock = float(50)
    totalReward = float(0)
    for i in range(0, layers):
        totalReward += rewardPerBlock * 210000
        rewardPerBlock = rewardPerBlock / 2
    totalReward += residual * rewardPerBlock
    return totalReward
