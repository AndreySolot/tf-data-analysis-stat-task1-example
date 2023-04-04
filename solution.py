import pandas as pd
import numpy as np


chat_id = 163596104 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    log_norm_sample = np.exp(x) + 723
    return np.log(log_norm_sample - 723).mean()
