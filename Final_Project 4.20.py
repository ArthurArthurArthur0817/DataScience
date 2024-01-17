import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 檔案讀取
df = pd.read_excel('dist4-20.xlsx')  
sum_traditional_SBL = int()
sum_traditional_PBL = int()
sum_internet_PBL = int()

Pre_test = []
Post_test = []

# 計算傳統SBL前測每題平均分数
print("Traditional SBL_Pre")
SBL_score_average1 = float(0)
for i in range(2, 17):          
    df.iat[i, 5] = ((float(df.iat[i, 1])) + (float(df.iat[i, 3]))) / 2
    SBL_score_average1 += df.iat[i, 5]
SBL_score_average1 /= 15    
print(SBL_score_average1)
Pre_test.append(SBL_score_average1)

# 計算傳統SBL後測每题平均分数
print("Traditional SBL_Post")
SBL_score_average2 = float(0)
for i in range(2, 17):          
    df.iat[i, 6] = ((float(df.iat[i, 2])) + (float(df.iat[i, 4]))) / 2
    SBL_score_average2 += df.iat[i, 6]
SBL_score_average2 /= 15
print(SBL_score_average2)    
Post_test.append(SBL_score_average2)

# 計算傳統PBL前測每題平均分數
print("Traditional PBL_Pre")
PBL_score_average1 = float(0)
for i in range(2, 17):          
    df.iat[i, 11] = ((float(df.iat[i, 7])) + (float(df.iat[i, 9]))) / 2
    PBL_score_average1 += df.iat[i, 11]
PBL_score_average1 /= 15
print(PBL_score_average1)
Pre_test.append(PBL_score_average1)

# 計算傳統PBL後測每題平均分數
print("Traditional PBL_Post")
PBL_score_average2 = float(0)
for i in range(2, 17):          
    df.iat[i, 12] = ((float(df.iat[i, 8])) + (float(df.iat[i, 10]))) / 2
    PBL_score_average2 += df.iat[i, 12]
PBL_score_average2 /= 15
print(PBL_score_average2)
Post_test.append(PBL_score_average2)

# 計算網路PBL前測每題平均分數 
print("Internrt PBL_Pre")
Int_score_average1 = float(0)
for i in range(2, 17):          
    df.iat[i, 17] = ((float(df.iat[i, 13])) + (float(df.iat[i, 15]))) / 2
    Int_score_average1 += df.iat[i, 17]
Int_score_average1 /= 15
print(Int_score_average1)
Pre_test.append(Int_score_average1)

# 計算網路PBL後測每題平均分數
print("Internet PBL_Post")
Int_score_average2 = float(0)
for i in range(2, 17):          
    df.iat[i, 18] = ((float(df.iat[i, 14])) + (float(df.iat[i, 16]))) / 2
    Int_score_average2 += df.iat[i, 18]
Int_score_average2 /= 15
print(Int_score_average2)
Post_test.append(Int_score_average2)

# 設置x軸變量
x_positions = np.arange(len(Pre_test))
print("----------------------------------------")
print("Pre-Test scroe:",Pre_test)
print("Post-Test scroe:",Post_test)

# 繪製長條圖
plt.bar(x_positions, Pre_test, width=0.2, label='Pre-Test')
plt.bar(x_positions + 0.2, Post_test, color='g', width=0.2, label='Post-Test')

# X軸/Y軸主題
plt.xlabel('Method')
plt.ylabel('Score')
plt.title('Teaching Method vs Score in Pre-Test and Post-Test')

# X軸標籤
plt.xticks(x_positions + 0.1, ['Traditional SBL', 'Traditional PBL', 'Internet PBL'])

# 在每個長條圖顯示數據
for i, value in enumerate(Pre_test):
    plt.text(i, value, f'{value:.2f}', ha='center', va='bottom', color='black')

for i, value in enumerate(Post_test):
    plt.text(i + 0.2, value, f'{value:.2f}', ha='center', va='bottom', color='black')

# 添加圖例
plt.legend()

# 顯示圖表
plt.show()
