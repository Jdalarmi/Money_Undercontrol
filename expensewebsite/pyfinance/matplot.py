import base64
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt


def generate_pie_chart(categories, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    ax.axis('equal') 

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return f'data:image/png;base64,{image_base64}'

def generate_chart_bar(categories, values):
    fig, ax = plt.subplots()
    ax.barh(categories, values, color="green")

    plt.ylabel("Gerenciamento de gastos")

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return f'data:image/png;base64,{image_base64}'

    