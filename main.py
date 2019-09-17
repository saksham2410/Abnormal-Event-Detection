# import Tracker
from tracker import Tracker

# Create Tracker instance with parameters
t = Tracker(videoPath="try6.mov", hsvLow=(39, 0, 27), hsvHigh=(130, 255, 74))

# Alternatively:
#   t = Tracker()
#   t.setVideo("inputName.mov")
#   t.setThresh((39, 0, 27), (130, 255, 74))

# Track, with the image width being reset to 700p
# Notably, output needs to be a .avi to work properly
t.track(outputName="outputName.avi", resizeWidth=700)
t.setScale()
# Release video capture
t.release()

# Compute motion values
t.computeMotion()

# Plot positions
t.plotPos()
t.plotPos(comp=True, cont=True)

# Plot speed and velocity components
t.plotVel()
t.plotVel(comp=True, cont=True)

# Plot acceleration and its components
t.plotAcc()
t.plotAcc(comp=True, cont=True)

# Show all plots
t.showPlots()