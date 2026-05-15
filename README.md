这个仓库用来存放我的一些小练习和小项目。目前做的小项目有实时检测车辆系统以及一个电商分析的小项目。
关于电商分析小项目。
# Online Retail 电商销售分析 (小项目)

## 项目背景
对 Online Retail 数据集进行快速销售分析，旨在探索销售情况、核心市场和热销商品，为业务决策提供支持。

## 分析目标
- 计算核心业务 KPI
- 分析销售的国家分布
- 探索销售时间趋势
- 找出热销商品

## 技术栈
- SQL (MySQL / Navicat)
- Python (Pandas, Matplotlib, Seaborn)
- 数据清洗、聚合分析、可视化

## 关键洞察

1. **英国是核心市场**  
   贡献约 **88%** 的销售额，其他欧洲国家占比很小。

2. **销售规模**  
   总销售额约 £2,076,086，平均客单价 £475.19。

3. **销售趋势**  
   2010 年销售存在明显季节波动，7 月为高峰期。

4. **热销商品**  
   "PAPER CRAFT, LITTLE BIRDIE" 单品销量突出，礼品和装饰类商品表现强劲。

## 可视化展示

![Top 5 Countries](top_countries.png)
![Monthly Trend](monthly_trend.png)
![Top 10 Products](top_products.png)

## 项目收获
- 掌握了端到端的 SQL 分析流程（清洗、聚合、分组、日期处理）
- 学会使用 Python 进行数据可视化
- 培养了业务洞察和故事化表达能力

## 如何运行
1. 下载本仓库
2. 使用 Navicat 导入 `data.csv`
3. 运行 `analysis.sql` 中的查询
4. 运行 `visualization.ipynb` 生成图表