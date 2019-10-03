
"""

"demo.py"

Demonstration of facial recognition system.

"""

# SETUP AND ERROR HANDLING
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
warnings.simplefilter(action="ignore", category=UserWarning)
warnings.simplefilter(action="ignore", category=RuntimeWarning)

import tensorflow as tf
try:
  tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
except AttributeError:
  tf.logging.set_verbosity(tf.logging.ERROR)

try:
  # for Pycharm
  from extras.paths import Paths
except ModuleNotFoundError:
  # for terminal
  import sys
  from paths import Paths
  sys.path.insert(1, Paths.HOME)

# ACTUAL DEMO
from facenet import *

cprint("Loading facial recognition system", attrs=["bold"], end="")
cprint("...", attrs=["bold", "blink"])
facenet = FaceNet(Paths.HOME + "/models/facenet_keras.h5")

cprint("Loading encrypted database", attrs=["bold"], end="")
cprint("...", attrs=["bold", "blink"])
facenet.set_data(Preprocessing.retrieve_embeds(Paths.HOME + "/images/encrypted.json"))

fig = plt.gcf()
plt.imshow(imread(Paths.HOME + "/images/data_example.png"))
plt.title("Example data point from database")
plt.axis("off")
fig.canvas.set_window_title("Facial recognition demo")
plt.show()

input("Press any key to continue:")

facenet.real_time_recognize(use_log=True)