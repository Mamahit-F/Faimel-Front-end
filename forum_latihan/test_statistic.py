import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import drive

try:
    total_students = data.shape[0]
    print(f"Total siswa: {total_students}")
except Exception as e:
    print(f"Terjadi kesalahan saat menghitung total siswa: {e}")