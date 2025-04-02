PI = 3.14159265358979323846

m = 36 * 0.001  # kg
g = 9.8  # m/s^2
R = 20 * 0.001  # m


def agrAccel(a: list[float]) -> list[float]:
    r = [0.0 for _ in  range(4)]
    for i in range(4):
        k1 = i + 1
        k2 = i + 5
        t1 = a[k1 - 1]
        t2 = a[k2 - 1]
        r[i] = 2*PI*(k1*t2-k2*t1)/(t1*t1*t2-t2*t2*t1)
        r[i] = round(r[i], 4)
    return r

if __name__ == "__main__":
    res = list(map(float, input("输入阻力矩下的数据；").split()))
    ten = list(map(float, input("输入拉力矩下的数据：").split()))
    print("阻力矩下的角速度（rad/s）:")
    accRes = agrAccel(res)
    for i in range(4):
        print(accRes[i])
    print("阻力矩下的平均角速度（rad/s）:")
    beta1 = sum(accRes)/4
    print(beta1)
    print("拉力矩下的角速度（rad/s）:")
    accTen = agrAccel(ten)
    for i in range(4):
        print(accTen[i])
    print("拉力矩下的平均角速度（rad/s）:")
    beta2 = sum(accTen)/4
    print(beta2)
    print("转动惯量（kg*m^2）:")
    print(round(m*R*(g-R*beta2)/(beta2-beta1), 8))




