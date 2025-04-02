def least_squares(a, b):
    """
    最小二乘法计算线性回归 y = bx + a
    :param a: 一维数组，x 数据
    :param b: 一维数组，y 数据
    :return: (截距 a, 斜率 b, x 轴截距)
    """
    n = len(a)
    sum_x = sum(a)
    sum_y = sum(b)
    sum_xy = sum(x * y for x, y in zip(a, b))
    sum_x2 = sum(x ** 2 for x in a)
    
    # 计算斜率 b
    b_slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    
    # 计算截距 a
    a_intercept = (sum_y - b_slope * sum_x) / n
    
    # 计算 x 轴截距，即 y = 0 时的 x 值
    x_intercept = -a_intercept / b_slope if b_slope != 0 else None
    
    return a_intercept, b_slope, x_intercept


def calculate_correlation(a, b):
    """
    计算两个数组之间的皮尔逊相关系数
    :param a: 一维数组，x 数据
    :param b: 一维数组，y 数据
    :return: 相关系数 r
    """
    n = len(a)
    mean_a = sum(a) / n
    mean_b = sum(b) / n
        
    numerator = sum((x - mean_a) * (y - mean_b) for x, y in zip(a, b))
    denominator = (sum((x - mean_a) ** 2 for x in a) * sum((y - mean_b) ** 2 for y in b)) ** 0.5
        
    return numerator / denominator if denominator != 0 else 0

if __name__ == "__main__":
    # 示例数据
    a = [2.7418, 2.8947, 2.9945, 3.0652, 3.1394, 3.1908, 3.2171, 3.2390, 3.2657, 3.2989]
    b = [4.6, 3.7, 3, 2.525, 2.025, 1.75, 1.55, 1.475, 1.275, 1.05]

    intercept, slope, x_axis_intercept = least_squares(a, b)
    print(f"截距 a: {intercept}")
    print(f"斜率 b: {slope}")
    print(f"x 轴截距: {x_axis_intercept}")
    print(f"相关系数 r: {calculate_correlation(a, b)}")
