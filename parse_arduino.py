import plot
import serial

LIMIT_BY = 10

fig = plot.Figure(10)
lp = plot.LinePlot(fig, history=10)
vl = plot.VerticalLines(fig)

ser = serial.Serial("/dev/ttyUSB0", 115200, timeout = .1)

i = 1
while True:
    line = ser.readline()
    if line!="":
        print line
    if line.startswith("#"):
        val = float(line.split()[1])
        lp.add_value(val)
        if LIMIT_BY!=0:
            i+=1
            if (i%LIMIT_BY)==0:
                fig.refresh()
                i=1
        else:
            fig.refresh();
    elif line.startswith("!"):
        print "Added vl"
        mi, ma = lp.get_limits()
        vl.starty = mi
        vl.endy = ma
        vl.add_value()
        