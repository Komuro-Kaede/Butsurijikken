import matplotlib.pyplot as plt
from matplotlib import rcParams
from Beta import agrAccel, PI, g, R
from leastSquare import least_squares, calculate_correlation

# Set font to SimHei to support Chinese characters
rcParams['font.sans-serif'] = ['SimHei']  # Use SimHei for Chinese
rcParams['axes.unicode_minus'] = False  # Ensure minus signs are displayed correctly

m = []
betas = []
t = [[] for _ in range(6)]

for i in range(6):
    datas = list(map(float, input(f"请输入第{i+1}组的质量（g）与时间（s）：").split()))
    m.append(datas[0] * 0.001)  # 转换为 kg
    t[i] = datas[1:]
    acc = agrAccel(t[i])
    betas.append(sum(acc) / 4)
    print(f"第{i+1}组的角加速度（rad/s^2）：")
    for j in range(4):
        print(acc[j])
    print(f"第{i+1}组的平均角加速度（rad/s^2）：")
    print(betas[i])

intercept, slope, x_axis_intercept = least_squares(betas, m)
print(f"截距 a: {intercept}")
print(f"斜率 b: {slope}")
print(f"x 轴截距: {x_axis_intercept}")
print(f"相关系数 r: {calculate_correlation(betas, m)}")
print("转动惯量：")
print(slope * g * R)

# 数据可视化
plt.scatter(betas, m, color='blue', label='实验数据')  # 绘制散点图
plt.plot(betas, [slope * beta + intercept for beta in betas], color='red', label='拟合直线')  # 绘制拟合直线
plt.xlabel('平均角速度 (rad/s)')
plt.ylabel('质量 (kg)')
plt.title('质量与平均角速度的关系')
plt.legend()
plt.grid()
plt.show()
