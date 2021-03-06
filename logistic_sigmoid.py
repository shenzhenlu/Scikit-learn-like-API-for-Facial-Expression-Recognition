import numpy as np
import matplotlib.pyplot as plt
from util import get_binary_data, sigmoid, sigmoid_cost, error_rate

class LogisticModel():
    def __init__(self):
        pass

    def fit(self, X_train, Y_train, X_val, Y_val, learning_rate=1e-6, lambda_=0.1, epochs=10000, show_fig=False):

        N, D = X_train.shape
        self.W = np.random.randn(D) * np.sqrt(1 / D)
        self.b = 0

        costs = []
        best_val_error = 1
        for i in range(epochs):
            # Forward propagation 
            Y_train_pred = self.forward(X_train)
            
            # Gradient descent
            self.W -= learning_rate * (X_train.T.dot(Y_train_pred-Y_train) + lambda_*self.W)
            self.b -= learning_rate * ((Y_train_pred-Y_train).sum() + lambda_*self.b)
        
            if i % 50 == 0:
                Y_val_pred = self.forward(X_val)
                c = sigmoid_cost(Y_val, Y_val_pred)
                costs.append(c)
                e = error_rate(Y_val, np.round(Y_val_pred))
                print("Epoch:", i, "Cost:", c, "Error rate", e)
                if e < best_val_error:
                    best_val_error = e
        print("Best validation error", best_val_error)

        if show_fig:
            plt.plot(costs)
            plt.show()

    def forward(self, X_train):
        return sigmoid(X_train.dot(self.W) + self.b)


def main():
    X_train, Y_train, X_val, Y_val = get_binary_data()

    model = LogisticModel()
    model.fit(X_train, Y_train, X_val, Y_val, show_fig=True)


if __name__ == '__main__':
    main()
