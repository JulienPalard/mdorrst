# Designed to simplify the reinforcement learning.
# It can do the following:
- simplify the construction of neural networks 
- automatically construct the shadow neural network with NO human efforts.
- simplify the building of the gradient functions
- offer a simple interface to different game environments, e.g., openAI gym, Flappybird.


# Quick Start 
```
python DDPG/DDPG.py 
```
In this example, I implemented the DDPG [1] algorithm and run it against an openAI gym game. 
```
python DQN/DQN.py
```
In this example, I implemented the DQN [2] algorithm and run it against the Flappybird game.

# Technical Details
Before using the library:
```
class Actor:
    # variables into a bag
    # ema wrapper
    # gradient wrapper
    def __init__(self, session, state_size, action_size):
        hidden1Size = 200
        hidden2Size = 200

        self.session = session

        self.W1 = self.weight_variable(shape = [state_size, hidden1Size])
        self.B1 = self.bias_variable(shape=[hidden1Size])
        self.W2 = self.weight_variable(shape=[hidden1Size, hidden2Size])
        self.B2 = self.bias_variable(shape=[hidden2Size])
        self.W3 = self.weight_variable(shape=[hidden2Size, action_size])
        self.B3 = self.bias_variable(shape=[action_size])

        self.InputStates = tf.placeholder("float", shape=[None, state_size])
        self.H1 = tf.nn.relu(tf.matmul(self.InputStates, self.W1) + self.B1)
        self.H2 = tf.nn.relu(tf.matmul(self.H1, self.W2) + self.B2)
        self.out = tf.matmul(self.H2, self.W3) + self.B3


        self.Qgradient = tf.placeholder(tf.float32, [None, action_size])

        self.gradient = tf.gradients(self.out, [self.W1, self.B1, self.W2, self.B2, self.W3, self.B3], -self.Qgradient)
        zipped = zip(self.gradient, [self.W1, self.B1, self.W2, self.B2, self.W3, self.B3])
        self.apply = tf.train.AdamOptimizer(1e-6).apply_gradients(zipped)

        ema = tf.train.ExponentialMovingAverage(0.999)
        self.target_update = ema.apply([self.W1, self.B1, self.W2, self.B2, self.W3, self.B3])
        self.target_net = [ema.average(var) for var in [self.W1, self.B1, self.W2, self.B2, self.W3, self.B3]]
        self.target_InputStates = tf.placeholder("float", shape=[None, state_size])
        self.target_H1 = tf.nn.relu(tf.matmul(self.target_InputStates, self.target_net[0]) + self.target_net[1])
        self.target_H2 = tf.nn.relu(tf.matmul(self.target_H1, self.target_net[2]) + self.target_net[3])
        self.target_predict = tf.matmul(self.target_H2, self.target_net[4]) + self.target_net[5]
        
```
After using the library:
```
class Actor(NN):
    def __init__(self, session, hasShadowNet, state_size, action_size, hidden_state_size):
        NN.__init__(self, session, hasShadowNet)
        # nothing special:
        inputLayer = self.buildInputLayer("inputStates", shape=[None, state_size])
        h1 = self.buildLinearReluWire(inputLayer, [state_size, hidden_state_size])
        #for i in range(numOfHiddenLayers-1): # repeat (numOfHiddenLayers-1) times
        h1 = self.buildLinearReluWire(h1, [hidden_state_size, hidden_state_size])
        out = self.buildLinearWire(h1, [hidden_state_size, action_size])
        self.setOutLayer(out)
```
## simplify the construction of neural networks
The idea is that we automatically define the weight and bias variables for you based on the shape of the weight (shape of bias is determined by the last dimension of weight). 

## automatically construct the shadow neural network with NO human efforts.
For better stability, we often need to construct a shadown neural network by applying ExponentialMovingAverage to (the weight/bias variables of) the original neural network. However, construction of the shadow network is not easy: (1) you need to use the tf.train.ExponentialMovingAverage APIs to calculate the smoothed weight/bias variables, (2) you need to reconstruct, with these variables, a network that has the same structure as the original network. Our library lifts this burden by simply removing it. All you need to do is to set the parameter hasShadowNet of the NN.__init__ as True. We will automatically handle all the rest for you.

## simplify the building of the gradient functions
We automatically detect the weight/bias variables and calculate the gradient of the output over them.
All you need to do is specify the neural network with our APIs. Remember to specify the output layer:
```
   self.setOutLayer(out)
```

## offer a simple interface to different game environments, e.g., openAI gym, Flappybird.
```
class GameEngine:
    def __init__(self):
        print("game engine initialized")
    def initialState(self):
        raise NotImplementedError( "Should have implemented this, return R, S, T" )
    def step(self, action, state=None):
        raise NotImplementedError( "Should have implemented this" )
class OpenAIGameEngine(GameEngine):
    ...
class FlappyBirdGameEngine(GameEngine):
    ... 
```
## for details about the algorithm & results, please refer to the <a href="https://rl123blog.wordpress.com/">Blog</a>.


# References
- 1 CONTINUOUS  CONTROL  WITH  DEEP  REINFORCEMENT LEARNING
- 2 Playing Atari with Deep Reinforcement Learning
