import pygal
import requests
from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse, FileResponse
from pygal.style import LightColorizedStyle, LightenStyle

app = FastAPI()


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse("favicon.ico")


@app.get("/popular")
def popular(q: str):
    res = requests.get(
        f"https://api.github.com/search/repositories?q=language:{q}&sort=stars"
    )
    if res.status_code != 200:
        return JSONResponse(res.json(), status_code=res.status_code)

    names, plot_dicts = [], []
    for item in res.json().get("items"):
        names.append(item.get("name"))
        plot_dicts.append(
            {
                "value": item.get("stargazers_count"),
                "label": item.get("description"),
                "xlink": item.get("html_url"),
            }
        )

    config = pygal.Config()
    config.x_label_rotation = 45
    config.show_legend = False
    config.truncate_label = 15
    config.show_y_guides = False
    config.width = 1000
    chart = pygal.Bar(
        config,
        style=LightenStyle(
            "#333366",
            base_style=LightColorizedStyle,
            title_font_size=24,
            label_font_size=14,
            major_label_font_size=18,
        ),
    )
    chart.title = "Most-Starred Projects on GitHub"
    chart.x_labels = names
    chart.add("", plot_dicts)
    return Response(chart.render(), media_type="image/svg+xml")
