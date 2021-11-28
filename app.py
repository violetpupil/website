import pygal
import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pygal.style import LightenStyle, LightColorizedStyle

app = FastAPI()


@app.get("/popular")
def popular(q: str):
    res = requests.get(f"https://api.github.com/search/repositories?q=language:{q}&sort=stars")
    if res.status_code != 200:
        return f"{res.status_code} {res.reason} {res.text}"

    names, plot_dicts = [], []
    for item in res.json().get('items'):
        names.append(item.get('name'))
        plot_dicts.append({
            'value': item.get('stargazers_count'),
            'label': item.get('description'),
            'xlink': item.get('html_url')
        })

    config = pygal.Config()
    config.x_label_rotation = 45
    config.show_legend = False
    config.truncate_label = 15
    config.show_y_guides = False
    config.width = 1000
    chart = pygal.Bar(config, style=LightenStyle(
        '#333366',
        base_style=LightColorizedStyle,
        title_font_size=24,
        label_font_size=14,
        major_label_font_size=18,
    ))
    chart.title = "Most-Starred Python Projects on GitHub"
    chart.x_labels = names
    chart.add('', plot_dicts)
    return HTMLResponse(chart.render())
