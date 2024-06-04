from tensorflow.keras.models import load_model
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/model.h5", "rb") as f:
    model = load_model(f)

# classes = [
#     "A",
#     "B",
#     "C",
#     "D",
#     "E"
# ]

def predict_nutriscore(energi, protein, lemak, karbohidrat, serat, natrium):
    index_to_grade = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
    input_data = np.array([[energi, protein, lemak, karbohidrat, serat, natrium]])
    predict = model.predict(input_data)
    max_index = np.argmax(predict)
    grade = index_to_grade[max_index]

    return grade