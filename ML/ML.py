import Perceptron
#激活函数
def f(x):
    return 1 if x > 0 else 0

def train():
    p = Perceptron.Perceptron(2,f)
    p.train([[1,1],[0,0],[1,0],[0,1]], [1,0,0,0], 10, 0.1)
    return p

if __name__ == '__main__': 
    # 训练and感知器
    perception = train()
    print(perception)

    print('1 and 1 = %d' % perception.predict([1, 1]))
    print('0 and 0 = %d' % perception.predict([0, 0]))
    print('1 and 0 = %d' % perception.predict([1, 0]))
    print('0 and 1 = %d' % perception.predict([0, 1]))