# MathPlotter - 数学函数可视化工具

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)


## 项目概述

MathPlotter 是一个基于 Web 的数学函数可视化工具，支持实时生成二维函数图像。通过简洁的网页界面，用户可输入包含常见数学函数和运算符的表达式（如 `sin(x)*exp(-x/5)`），系统将自动解析并在交互式画布上呈现精确的函数曲线。项目采用安全表达式解析机制，适用于教育演示、科研分析和算法调试等场景。

## 核心特性

✅ **实时动态绘图**  
✅ **安全表达式解析**（支持 10+ 数学函数）  
✅ 自适应坐标轴范围  
✅ 智能错误检测（非法字符/复数/无效运算）  
✅ 响应式网页设计（桌面/移动端适配）  
✅ 跨平台兼容（macOS/Windows/Linux）

## 技术栈

- **Web框架**: Flask 2.3
- **数学计算**: NumPy 1.24 + SymPy 1.12
- **可视化**: Matplotlib 3.7
- **前端**: 原生HTML5/CSS3
- **构建工具**: Python venv

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/liqian_liukaining/MathPlotter.git

# 进入目录
cd MathPlotter

# 安装依赖
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt

# 启动服务
python app.py
```
访问 `http://localhost:5000` 开始使用

## 功能演示

```text
示例输入：
- 基础函数：x**2 + 3*x - 5
- 三角函数：sin(x)*cos(2*x)
- 指数函数：exp(-x/5)*sqrt(abs(x))
```

## 许可证

本项目采用 [MIT 许可证](LICENSE)，您可自由：
- 修改并用于商业项目
- 进行私有部署
- 二次分发

唯一要求：保留原始版权声明

## 贡献指南

欢迎通过 Issues 提交功能建议或 Bug 报告，提交 PR 前请：
1. 确保通过基础测试套件
2. 更新相关文档
3. 遵循 PEP8 代码规范


**项目结构预览**
```
/MathPlotter
├── app.py                 # 主程序
├── requirements.txt       # 依赖清单
├── LICENSE
├── README.md
├── static
│   ├── css
│   │   └── style.css      # 样式表
│   └── demo-screenshot.png
└── templates
    └── index.html         # 前端模板
