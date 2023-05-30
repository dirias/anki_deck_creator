deep_neural_networks_concepts = [
    ("Why seek to build an artificial intelligence?", "To replicate some of the functions of a human being."),
    ("What is machine learning?", "The ability of a machine to learn a process based on the data it receives."),
    ("What are the first models based on?", "Simple perceptron (single neuron) represented by a mathematical model."),
    ("How does a neuron work?", "It has inputs, processing and discrimination, and an output."),
    ("What is the basic functioning of a perceptron?", "The weights are multiplied by the inputs, passed through the discriminator, and inputted into an activation function, which can be the sigmoid function."),
    ("What is machine learning used for?", "Answering questions and processing data."),
    ("What are dendrites?", "Locations where information enters the neuron."),
    ("What is the function of the nucleus in a neuron?", "Center for information processing."),
    ("What is the axon in a neuron?", "Connector between the nucleus and the terminals."),
    ("What is synapse in the context of neurons?", "Connections between neurons."),
    ("What determines whether information is transmitted to other neurons based on the activation level of the input information?", "The activation level of the input information."),
    ("What factors influence the intensity with which information is transmitted between neurons?", "The activity being followed and the module of neural networks being involved."),
    ("What are the weights in an artificial neuron?", "Strength of connection between the inputs and the nucleus."),
    ("What is the function of bias in an artificial neuron?", "Determines whether information is transmitted to the following neurons."),
    ("What are the 'out' connections in an artificial neuron?", "Connections between neurons."),
    ("What do activation functions in an artificial neuron imitate?", "Learning processes in a more natural way.")
]

deep_neural_networks = [
    ("What do deep neural networks do?", "Increase the number of layers and neurons to interpret increasingly complex patterns."),
    ("What is Gradient Descent?", "It is an algorithm that optimizes a neural network to minimize error."),
    ("How does Gradient Descent work?", "It uses curve optimization to progressively approach the minimum point."),
    ("What is Backpropagation?", "It is an iterative process that allows finding the minimum of a function."),
    ("What is involved in training a neural network?", "It involves initializing the weights with random values, obtaining the network's evaluation result, comparing it with the desired result, calculating the error, and adjusting the weights and bias."),
    ("What is the objective of training a neural network?", "To find the values of weights and bias that yield the minimum of the cost function."),
    ("What is the goal of Gradient Descent?", "To achieve total optimization of each of the neurons that compose the neural network."),
    ("What is repeated during the training of a neural network?", "Comparison of results, error calculation, and adjustment of weights and bias until a success criterion is met in relation to the training data."),
    ("What is bias in an artificial neuron?", "It is a discriminator that determines whether information is transmitted to the following neurons."),
    ("What are the weights in an artificial neuron?", "They are the strength of connection between the inputs and the nucleus of an artificial neuron.")
]

tensorflow = [
    ("What is TensorFlow?", "It started as an open-source library but is now a complete development environment."),
    ("Besides being a library, what does TensorFlow offer?", "It offers not only libraries for programming AI models but also tools for visualizing, optimizing, and sharing our models with the rest of the world."),
    ("What are the basic steps to create a simple application in TensorFlow?", "Having the data, designing your model, training it, verifying that the training was correct, and using it to make predictions.")
]

tensorflow_vs_tfjs_differences = [
    ("What capabilities does TF.js add to any web application?", "You can add machine learning capabilities."),
    ("Where can you create and train models with TF.js?", "You can create and train models in the Browser or on a Node server."),
    ("What can you do with TF.js in your JavaScript environment?", "You can use pre-trained models."),
    ("What is the difference in garbage collection between JavaScript and TensorFlow.js?", "Unlike JavaScript code, objects and variables used by TensorFlow.js are not automatically released from memory when they go out of scope."),
    ("Which function is used in TensorFlow.js to clean up intermediate tensors?", "You need to use the `tf.tidy()` function."),
    ("What functions exist in TensorFlow.js to measure performance and profile execution?", "There are functions to measure performance and profile flows and models."),
    ("What are some of the main classes in TensorFlow.js?", "Some main classes include Tensors, Models, Layers, Operations, Training, Performance, Environment, Constraints, Initializers, Regularizers, Data, Visualization, Utils, Backends, Browser, Metrics, and Callbacks.")
]

activation_functions = [
    ("What are activation functions?",
     "Activation functions are mathematical functions applied to the output of a neuron or node in a neural network, introducing non-linearity and determining the firing behavior of the neuron."),

    ("What is the purpose of using activation functions in neural networks?",
     "Activation functions introduce non-linearity, enabling neural networks to learn and represent complex patterns and relationships in the data."),

    ("What are some commonly used activation functions?",
     "Some commonly used activation functions include sigmoid, tanh, ReLU, leaky ReLU, softmax, ELU, Step function, and Sign function."),

    ("What is the sigmoid function and its concept?",
     "The sigmoid function maps the input to a smooth, S-shaped curve between 0 and 1. It is used in logistic regression and early neural networks for binary classification tasks."),

    ("What is the tanh function and its concept?",
     "The tanh function is similar to the sigmoid function but ranges from -1 to 1. It is commonly used in hidden layers of neural networks."),

    ("What is the ReLU function and its concept?",
     "The ReLU function returns the input value if it is positive and zero otherwise. It is widely used in deep learning models to address the vanishing gradient problem."),

    ("What is the leaky ReLU function and its concept?",
     "The leaky ReLU function is an extension of the ReLU function that allows small negative values. It helps mitigate the 'dead' neuron problem in deep neural networks."),

    ("What is the softmax function and its concept?",
     "The softmax function is used in the output layer of a neural network for multi-class classification. It converts raw outputs into a probability distribution over the classes, ensuring the sum of probabilities is 1."),

    ("What is the ELU function and its concept?",
     "The ELU (Exponential Linear Unit) function is similar to the ReLU function for positive inputs, but it allows negative inputs to have non-zero outputs. It helps alleviate the dying ReLU problem and can improve network performance."),

    ("What is the Step function and its concept?",
     "The Step function is a threshold function that outputs 0 or 1 based on a specific threshold. It is a simple binary function, commonly used in early neural network models."),

    ("What is the Sign function and its concept?",
     "The Sign function, also known as the signum or sign function, returns the sign of a real number (-1 for negative, 0 for zero, and 1 for positive values). While related to the Step function, it provides a continuous sign value rather than a binary output.")
]



