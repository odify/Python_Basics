#HANDS ON TENSORFLOW...

import tensorflow as tf
import numpy as np
from tensorflow import keras

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

model.compile(optimizer='sgd', loss='mean_squared_error')

#OUTPUT
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

model.fit(xs, ys, epochs=500)

print(model.predict([10.0]))

#OUTPUT= 31.00025749



# from setuptools import find_packages
# from setuptools import setup


# REQUIRED_PACKAGES = ['Pillow>=1.0', 'Matplotlib>=2.1', 'Cython>=0.28.1']

# setup(
#     name='object_detection',
#     version='0.1',
#     install_requires=REQUIRED_PACKAGES,
#     include_package_data=True,
#     packages=[p for p in find_packages() if p.startswith('object_detection')],
#     description='Tensorflow Object Detection Library',
# )



# UNDER CONSTRUCTION...