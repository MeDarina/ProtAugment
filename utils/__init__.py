from .data import *

import os

def gpu_stats(message=""):
    print("="*50)
    print(message)
    os.system("nvidia-smi --query-gpu=index,name,memory.total,memory.used --format=csv")
    print("="*50)
