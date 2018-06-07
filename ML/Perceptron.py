from functools import reduce

class Perceptron(object):
    def __init__(self, paramCount, activator):
        self.activator = activator
        self.weights = [0.0 for _ in range(paramCount)]
        self.bias = 0.0

    def __str__(self):
        return 'weights\t:%s\nbias\t:%f\n' % (self.weights, self.bias)

    #预测
    def predict(self, params):
        return self.activator(reduce(lambda a,b : a + b,
                    map(lambda x_w : x_w[0] * x_w[1],
                        zip(params, self.weights)), 0.0) + self.bias)

    #训练
    def train(self, params, labels, iterationCount, rate):
        for _ in range(iterationCount):
            self.iteration(params,labels,rate)

    #迭代
    def iteration(self, params, labels, rate):
        samples = zip(params, labels)
        for (param, label) in samples:
            self.setWeights(param, self.predict(param), label, rate)

    #更新权重
    def setWeights(self, param, output, label, rate):
        delta = label - output
        self.weights = list(map(lambda x_w : x_w[1] + rate * delta * x_w[0],zip(param,self.weights)))
        self.bias += rate * delta

