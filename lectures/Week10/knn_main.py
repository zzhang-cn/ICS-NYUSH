import matplotlib.pylab as pylab
import knn
import random
import sample
import util

LABELS = ('a','b','c')

# Onclick event for the graph (you can add new points & have them classified in real time)
def onclick(event):
    # Creating a new point and finding the k nearest neighbours
    new = sample.Sample('', [event.xdata, event.ydata], '')
    knn.knn(new, data, K)

    data.append(new)
    pylab.scatter([new.getFeatures()[0]], \
                  [new.getFeatures()[1]], \
                  label=new.getLabel(), \
                  marker=MARKERS[LABELS.index(new.getLabel())], \
                  color=COLORS[LABELS.index(new.getLabel())])
    pylab.draw()
    
# Making up data points for the KNN live demo
def make_data(n):
    C = [random.choice(LABELS) for x in range(n)]
    linear_data = [ sample.Sample(C[x], [x/(float(SCALE)), x/(float(SCALE))], C[x]) for x in range(n) ]
    mean = 0
    std = DEV * SCALE
    
    noise = util.genDistribution(mean, std, mean, std, n, '')
    data = [linear_data[i] + noise[i] for i in range(n)]
    return data

if __name__ == "__main__":

    # Consts for x/y scale, deviation limit, number of samples, choice of k, class names
    # ALTER THESE PARAMETERS TO CREATE DIFFERENT TEST SETS
    SCALE = 10
    DEV = 0.2
    SAMPLES = 100
    K = 3
    
    # Sets of labels, markers and colors for plotting
    # Every extra label is a new class. Try not to have more than 5 or so classes
    # (because the color markers become hard to distinguish)
    LABELS = ('a','b','c')
    MARKERS = util.make_cmarkers()
    COLORS = util.make_cmap()
    
    # Generating random data
    data = make_data(SAMPLES)

    # Connecting the onclick event to the onclick handler
    fig = pylab.figure()
    cid = fig.canvas.mpl_connect('button_press_event', onclick)

    # Plotting the randomly generated data
    for l in range(len(LABELS)):
        m = MARKERS[l]
        x = [ data[d].getFeatures()[0] for d in range(len(data)) if data[d].getLabel() == LABELS[l] ]
        y = [ data[d].getFeatures()[1] for d in range(len(data)) if data[d].getLabel() == LABELS[l] ]
        pylab.scatter(x,y,label=LABELS[l],marker=m,color=COLORS[l])

    pylab.show()
