def plotable(silent=False):
    '''
    Used on model.build to call tf.keras.utils.plot_model
    '''
    
    def decorate(func):
        @wraps(func)
        def wrapper(self,input_shape):
            result=func(self,input_shape)

            if not silent:
                from tensorflow.keras import layers
                from IPython.display import display
                if isinstance(input_shape,(tuple,tf.TensorShape)):
                    inputs=layers.Input(input_shape[1:])
                elif isinstance(input_shape,list):
                    inputs=[layers.Input(s[1:]) for s in input_shape]
                else:
                    raise AssertionError

                outputs=self.call(inputs)
                model=tf.keras.Model(inputs=inputs,outputs=outputs)
                display(tf.keras.utils.plot_model(model,show_shapes=True))
            return result
        return wrapper
    return decorate
