import numpy as np
import matplotlib.pyplot as plt

# 물질명: L-Cystine, L-Phenylalanine, o-Tyrosine, Biopterin, ADP

data = np.array([14.88, 13.45, 21.52, 7.25, 2.96])

noise = np.random.normal(0, 1, 5)

anomaly = np.round(data + noise, 2)  # 데이터에 noise 추가. 임의의 데이터 역할

print(data)

# data와 anomaly fit. 임의의 데이터와 표준 데이터 fit. 관계식 찾아내기.
# 찾아낸 후에는 식으로 정리할 것

#def fit(A, B):
    #fp1 = np.polyfit(A, B, 1)
    #f1 = np.poly1d(fp1)  # 관계식 f1
    #return f1

#f1 = fit(anomaly, data)

# print(f1)  # 함수를 프린트한 결과 ax+b 형태로 나옴.

#x = np.arange(0, 31, 0.01)
#plt.figure()
#plt.plot(x, f1(x))  # 함수에 따라 결과값 출력
#plt.show()

# print(f1(14.5))  # 특정 x값 넣으면 fit된 값 출력 이 값으로 화학종 다시 찾기.

#def find_nearest(totalRT, fitRT): # 가장 가까운 예상값 구하기
#    totalRT = np.asarray(totalRT)
#    idx = (np.abs(totalRT - fitRT)).argmin()
#    return totalRT[idx]

#print(find_nearest(data, f1(14.0))) # 예상값 출력. 이것을 화학종 이름으로 되돌리기. dict.
