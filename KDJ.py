import matplotlib.pyplot as plt

class KDJ:
    def __init__(self, period, high, low, close):
        self.period = period
        self.high   = high
        self.low    = low
        self.close  = close
        self.WindowH   = self.high.rolling(period).max()
        self.WindowL   = self.low.rolling(period).min()
        self.K = (self.close - self.WindowL)/(self.WindowH - self.WindowL)*100
        self.D = self.K.rolling(15).mean()
        
    def plot(self, window = None):
        fig = plt.figure()
        if window is not None:
            self.D.ix[ -window : ].plot(label = "D")
            self.K.ix[ -window : ].plot(label = "K")
            self.close.ix[ -window : ].plot(label = "Close")
        else:
            self.D.plot(label = "D")
            self.K.plot(label = "K")
            self.close.plot(label = "Close")
        fig.legend()
        fig.show()
