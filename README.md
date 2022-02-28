# light-keras-plot
A lightweight library for plotting especially the keras subclass model.  
The library only has 27 lines, and you only need to add 3 line to the model.  
# Usage
See Usage.ipynb to see more.  
tf.keras.util.plot_model is a powerful tool to visualize a model, while it can't directly plot a subclassed model. After several times trying, finnaly I find a way to automatically catch the input_shape and meanwhile have the minimal code to change.
