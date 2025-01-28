# app.py
"""
MathPlotter - 数学函数可视化工具 (Python 3.9 兼容版)
版本: 1.1.1
作者: liqian_liukaining
更新日期: 2025-01-28
"""
import sys

if sys.version_info < (3, 9):
    raise RuntimeError("需要 Python 3.9 或更高版本")

from flask import Flask, render_template, request
import numpy as np
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import sympy
from sympy import SympifyError

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

SAFE_FUNCTIONS = {
    'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
    'sqrt': np.sqrt, 'log': np.log, 'exp': np.exp,
    'abs': np.abs, 'pi': np.pi, 'e': np.e
}


def safe_evaluator(expression, x_values):
    x_sym = sympy.Symbol('x')
    try:
        parsed = sympy.parse_expr(
            expression,
            local_dict={'x': x_sym},
            transformations=(
                sympy.parsing.sympy_parser.standard_transformations
            )
        )

        if parsed.free_symbols - {x_sym}:
            raise ValueError("仅允许使用变量x")

        func = sympy.lambdify(x_sym, parsed, modules=['numpy', SAFE_FUNCTIONS])
        y = func(x_values)

        if np.iscomplexobj(y):
            y = np.real(y)
            if np.isnan(y).any():
                raise ValueError("存在无效的复数计算结果")

        return y

    except SympifyError:
        raise ValueError("表达式解析失败")
    except Exception as e:
        raise ValueError(f"计算错误: {str(e)}")


@app.route('/', methods=['GET', 'POST'])
def plot_generator():
    context = {
        'plot_url': None,
        'error': None,
        'form_data': {'formula': '', 'x_min': '-10', 'x_max': '10'}
    }

    if request.method == 'POST':
        context['form_data'] = request.form.to_dict()
        try:
            x_min = float(context['form_data']['x_min'])
            x_max = float(context['form_data']['x_max'])
            x_min, x_max = sorted([x_min, x_max])

            x = np.linspace(x_min, x_max, 500)
            y = safe_evaluator(context['form_data']['formula'], x)

            if np.isnan(y).any() or np.isinf(y).any():
                raise ValueError("计算结果包含无效值")

            plt.figure(figsize=(10, 6))
            plt.plot(x, y, color='#007bff', linewidth=2)
            plt.title(f"函数图像: {context['form_data']['formula']}")
            plt.grid(True, linestyle='--', alpha=0.7)

            buffer = BytesIO()
            plt.savefig(buffer, format='png', dpi=100)
            context['plot_url'] = base64.b64encode(buffer.getvalue()).decode()
            plt.close()

        except ValueError as e:
            context['error'] = f"输入错误: {str(e)}"
            plt.close()
        except Exception as e:
            context['error'] = f"系统错误: {str(e)}"
            plt.close()

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)