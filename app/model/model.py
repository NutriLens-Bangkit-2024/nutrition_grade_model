import tensorflow as tf

import numpy as np
from pathlib import Path
import os
from sklearn import preprocessing

BASE_DIR = Path(__file__).resolve(strict=True).parent

model = tf.keras.models.load_model(os.path.join(BASE_DIR, 'nutrigrade_model.h5'),compile=False)

# classes = [
#     "A",
#     "B",
#     "C",
#     "D",
#     "E"
# ]

def predict_nutriscore(energi, protein, lemak, karbohidrat, serat, natrium):
    index_to_grade = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
    input_data = np.array([[energi, protein, lemak, karbohidrat, serat, natrium]], dtype=np.float32)
    normalized_arr = preprocessing.normalize(input_data)
    predict = model.predict(normalized_arr)
    max_index = np.argmax(predict)
    grade = index_to_grade[max_index]

    return grade

