import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['axes.unicode_minus'] = False  ## 마이나스 '-' 표시 제대로 출력
import seaborn as sns

from scipy import stats
import statsmodels.api as sm

df = pd.read_csv("RT_predict_confirm.csv")

X = df['Experimental_RT']
y = df['Predicted_RT']
Residual = y - X

# print(df['Experimental_RT'].describe())
# print(df['Predicted_RT'].describe())

def outliers_iqr(data):
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - (iqr * 1.5)
    upper_bound = q3 + (iqr * 1.5)
    return np.where((data > upper_bound) | (data < lower_bound))


outlier_index = outliers_iqr(Residual)[0]
print(outlier_index[0])
outlier1 = df['Dns_SMILES'][outlier_index[0]]
print(outlier1)
#print(len(outlier_index))

# df_1 = df.drop(outlier_index, axis=0)
# X1 = df_1['Experimental_RT']
# y1 = df_1['Predicted_RT']
#
# plt.scatter(X1, y1)
# plt.show()
