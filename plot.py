import pylab as plt
from collections import deque
import time
import random
import numpy as np
plt.ion()

class BasePlot(object):
    def __init__(self, fig, history=8):
        self.ax = fig.ax
        self.history = history
        self.x_vals = []
        self.y_vals = []
        fig.add_child(self)

    def add_value(self, val, stamp=None):
        if stamp is None:
            stamp = time.time()
        self.x_vals.append(stamp)
        self.y_vals.append(val)

        self.delete_old()
        self.refresh_plot_obj()

    def delete_old(self):
        i = 0
        while i < len(self.x_vals)-1 and \
                (time.time() - self.x_vals[i]) > self.history:
            i+=1

        self.x_vals = self.x_vals[i:]
        self.y_vals = self.y_vals[i:]

    def reset(self):
        self.x_vals = []
        self.y_vals = []

    def refresh_plot_obj(self):
        pass

    def get_y_limits(self):
        return (min(self.y_vals), max(self.y_vals))

    def get_x_limits(self):
        return (min(self.x_vals), max(self.x_vals))


class LinePlot(BasePlot):
    def __init__(self, fig, history=8):
        super(LinePlot, self).__init__(fig, history)
        self.line = self.ax.plot([1], [1])[0]

    def refresh_plot_obj(self):
        self.line.set_xdata(self.x_vals)
        self.line.set_ydata(self.y_vals)


class VerticalLines(BasePlot):
    def __init__(self, fig, history=8, starty=0, endy=1, lw=1, color="r"):
        super(VerticalLines, self).__init__(fig, history)
        self.starty = starty
        self.endy = endy
        self.value_added = False
        self.lw = lw
        self.color = color
        self.lines = self.ax.vlines(time.time(), self.starty, self.endy, color=self.color, lw=self.lw)

    def add_value(self, stamp=None):
        super(VerticalLines, self).add_value(0,stamp=stamp)
        self.value_added = True

    def refresh_plot_obj(self):
        self.lines.remove()
        self.lines = self.ax.vlines(self.x_vals, self.starty, self.endy, color=self.color, lw=self.lw)
        self.value_added = False

    def get_y_limits(self):
        return (self.starty, self.endy)

    def get_x_limits(self):
        return None


class Figure(object):
    # length: Which time window this figure should show
    # rolling figure: If the figure should always show the last
    # 'length' values from time.time() and keep rolling even if the plots
    # within are not updated. If false, the figure will snap to the extent of
    # the plots shown within.
    def __init__(self, length, rolling_figure=True):
        self.children = []
        self.length = length
        self.rolling_figure = rolling_figure
        self.fig = plt.figure()
        self.ax = plt.subplot(111)

    def refresh(self):
        limits = [child.get_y_limits() for child in self.children]
        self.ax.set_ylim(min([x[0] for x in limits]),
                         max([x[1] for x in limits]))

        if self.rolling_figure:
            self.ax.set_xlim(time.time() - self.length, time.time())
        else:
            limits = [child.get_x_limits() for child in self.children]
            self.ax.set_xlim(min([x[0] for x in limits]),
                             max([x[1] for x in limits]))
        self.fig.canvas.show()

    def add_child(self, child):
        self.children.append(child)



if __name__== "__main__":
    #plt.ion()
    fig = Figure(10)

    lp = LinePlot(fig)
    vl = VerticalLines(fig)
    i = 0
    while True:
        lp.add_value(random.random())
        if random.random() > .9:
            print "added"
            vl.add_value()
        fig.refresh()
        fig.fig.savefig("im{:0>3d}.png".format(i))
        i+=1
        time.sleep(.1)

