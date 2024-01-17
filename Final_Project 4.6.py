import pandas as pd
import matplotlib.pyplot as plt

#檔案讀取
df = pd.read_excel('dist4-6.xlsx')

# 根據標籤進行數據讀取
dimension = df['\nDimension'].tolist()
pre_test_data = df['pre-test'].tolist()
post_test_data = df['post-test'].tolist()
data_labels = df['class'].tolist()

# 創建數據變數，
data = {'Dimension': dimension,
        'class': data_labels,
        'Pre_Test': pre_test_data,
        'Post_Test': post_test_data}

df_combined = pd.DataFrame(data)

# 使用 groupby對不同向度進行分組
grouped_df = df_combined.groupby('Dimension')

# 創建一個圖表，每個主题對應一个子圖表
fig, axes = plt.subplots(len(grouped_df), 1, figsize=(8, 6), sharex=True)

# 迭代每个向度，建立子圖表
for i, (name, group) in enumerate(grouped_df):
    bars=group.plot(kind='bar', x='class', y=['Pre_Test', 'Post_Test'], ax=axes[i], rot=0)
    for bar in bars.patches:
        axes[i].text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height():.2f}',
                     ha='center', va='bottom',weight='bold',color='black')
    axes[i].set_ylabel('Score')
    axes[i].set_title(f'{name}')

# 添加標籤和標題
plt.xlabel('class')

# 調整子圖表間距
plt.tight_layout()

# 顯示圖表
plt.show()
