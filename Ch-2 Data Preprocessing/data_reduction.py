import pandas as pd
import numpy as np
data = {'Feature1': np.random.randn(100000),
        'Feature2': np.random.randn(100000),
        'feature3':np.random.randn(100000)}
df = pd.DataFrame(data)

print(f"Original Dataset size: {df.size}")

sampled_df = df.sample(frac=0.10, random_state=42)
print(f"Reduced Dataset Size: {sampled_df.shape}")