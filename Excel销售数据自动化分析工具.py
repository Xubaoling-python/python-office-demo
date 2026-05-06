'''
这个项目用到了pandas和matplotlib
pandas 是 Python 里的 “数据处理神器”
读取 / 写入 Excel、CSV、JSON、SQL 数据
像 Excel 表格一样增删改查数据
筛选、排序、分组、统计、合并表格
清洗脏数据（去重、补空值、替换）
处理百万行数据飞快


matplotlib 是 Python 最基础、最标准的画图库
画折线图、柱状图、饼图、散点图、直方图
自定义颜色、线条、标签、标题、图例
导出高清图片（PNG、PDF）
和 pandas 完美配合：数据处理完直接画图

pandas 把数据读进来 → 清洗 → 计算
matplotlib 把结果画成图表 → 直观展示

自动读取销售数据 Excel 文件
完成数据清洗（去重、处理缺失值）
生成基础统计结果（总销售额、销量 Top 商品）
生成可视化图表（月度销售趋势图）
导出分析结果到新 Excel 文件
'''
import pandas as pd
import matplotlib.pyplot as plt


# 解决matplotlib中文乱码问题
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False

# 1.读取数据Excel文件
df = pd.read_excel("销售数据.xlsx")
print("df类型:",type(df))
print("原始数据行数：",len(df))

# 2.数据清洗
# 去除重复行
df = df.drop_duplicates()
# 处理缺失值(销售额/销售为0或空的行直接删除)
# dropna 是 drop not available（丢弃缺失值）的缩写。subset 参数指定了只看这两列。只要这两列中任意一列是空的，这整行数据就会被删掉
df = df.dropna(subset=["销售额","销量"])
# df["销售额"] > 0 会返回一串 True/False 的判断结果。把它放在 df[...] 里面，pandas 就会只筛选出 True 的行。
df = df[df["销售额"] > 0]
df = df[df["销量"] > 0]
print("清洗后数据行数：", len(df))

# 3. 新增月份列，方便后续分析
df["月份"] = pd.to_datetime(df["日期"]).dt.to_period("M")


# 基础统计分析
# 1. 整体统计
total_sales = df["销售额"].sum()
total_quantity = df["销量"].sum()
print(f"总销售额：{total_sales:.2f} 元")
print(f"总销量：{total_quantity} 件")

# 2. 销量Top5商品
top5_products = df.groupby("商品名称")["销量"].sum().sort_values(ascending=False).head(5)
print("\n销量Top5商品：")
print(top5_products)

# 3. 各区域销售额统计
region_sales = df.groupby("区域")["销售额"].sum().sort_values(ascending=False)
print("\n各区域销售额：")
print(region_sales)


# 生成可视化图表
# 1. 月度销售趋势图
monthly_sales = df.groupby("月份")["销售额"].sum()
monthly_sales.plot(kind="line", marker="o", color="#1f77b4")
plt.title("月度销售趋势")
plt.xlabel("月份")
plt.ylabel("销售额（元）")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("月度销售趋势图.png")
plt.close()

# 2. 区域销售额柱状图
region_sales.plot(kind="bar", color="#ff7f0e")
plt.title("各区域销售额对比")
plt.xlabel("区域")
plt.ylabel("销售额（元）")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("区域销售额对比图.png")
plt.close()


# 导出分析结果
# 把统计结果写入新的Excel文件
with pd.ExcelWriter("销售数据分析结果.xlsx") as writer:
    # 清洗后的数据
    df.to_excel(writer, sheet_name="清洗后数据", index=False)
    # 销量Top5商品
    top5_products.to_excel(writer, sheet_name="销量Top5商品")
    # 各区域销售额
    region_sales.to_excel(writer, sheet_name="各区域销售额")

print("\n✅ 分析完成！已生成以下文件：")
print("- 月度销售趋势图.png")
print("- 区域销售额对比图.png")
print("- 销售数据分析结果.xlsx")