
from direct.actor.Actor import Actor

node_path = Actor('Model path', {
    'Animation Name 1': 'Animation Path 1',
    'Animation Name 2': 'Animation Path 2'
})

# Basic animation playing
actor.play('Animation Name')
actor.loop('Animation Name')
actor.stop()

actor.pose('Animation Name', 0)

actor.play('Animation Name', fromFrame=10)
actor.loop('Animation Name', fromFrame=24, toFrame=36)

actor.pose('Animation Name', 30)
actor.loop('Animation Name', restart=0, fromFrame=24, toFrame=36)

# Return the total number of frame in the anumation
print(actor.getNumFrames('Animation Name'))

# Returns a string containing the name of the current playing animation
print(actor.getCurrentAnim())

# Returns the current frame of the animation
print(actor.getCurrentFrame('Animation Name'))

# AnimControl
# provides control aver a certain animation

# Get the AnimControl
myAnimControl = actor.getAnimControl('Animation Name')

# Returns a boolean whether the animation is playing or not
myAnimControl.isPlaying()

# Return the current frame number
myAnimControl.getFrame()

# Returns the speed of the animation in frame per second
# myAnimControl

# Returns a floating-point frame number exceeding the framecount. Not recommended
myAnimControl.getFullFframe()

# Returns an integer frame number exceeding the framecount. Not recommended
myAnimControl.getFullFrame()

# Return the number of the next frame on the queue
myAnimControl.getNextFrame()

# Returns the total number of frames
myAnimControl.getNumFrames()

# Returns the playrate.
myAnimControl.getPlayRate()

# Start playing the animation in a loop
myAnimControl.loop()


