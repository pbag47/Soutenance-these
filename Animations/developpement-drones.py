
import plotly
# import plotly.subplots
import datetime


t = [
    datetime.datetime(year=2023, month=1, day=1),
    datetime.datetime(year=2024, month=1, day=1),
    datetime.datetime(year=2025, month=1, day=1),
    datetime.datetime(year=2026, month=1, day=1),
]

registered = [
    285530,
    320814,
    387260,
    462000,
]

professionnals = [
    16232 - 5644,
    16232,
    18191,
    18191 + 2609,
]

fig_nb_drones = plotly.graph_objects.Figure(
    layout=dict(
        title_text="Nombre de drones enregistrés en France",
        title_font_size=24,
        template="plotly_dark",
        autosize=False,
        width=750,
        height=350,
        margin=dict(
            l=50,
            r=50,
            b=50,
            t=50,
        ),
        yaxis_rangemode="tozero",
        yaxis_tickfont_size=16,
        yaxis_exponentformat = "power",
        xaxis_tickfont_size=16,
        xaxis_title_text="Date",
        xaxis_title_font_size=20,
        xaxis_exponentformat = "power",
    )
)
fig_nb_drones.add_trace(
    plotly.graph_objects.Scatter(
        x=t,
        y=registered,
        name="Drones enregistrés en France",
        showlegend=False,
    ),
)

fig_nb_pro = plotly.graph_objects.Figure(
    layout=dict(
        title_text="Nombre de télépilotes professionnels en France",
        title_font_size=24,
        template="plotly_dark",
        autosize=False,
        width=750,
        height=350,
        margin=dict(
            l=50,
            r=50,
            b=50,
            t=50,
            # pad=4,
        ),
        # paper_bgcolor="rgb(16, 24, 43)",
        yaxis_rangemode="tozero",
        yaxis_tickfont_size=16,
        yaxis_exponentformat = "power",
        xaxis_tickfont_size=16,
        xaxis_title_text="Date",
        xaxis_title_font_size=20,
        xaxis_exponentformat = "power",
    )
)
fig_nb_pro.add_trace(
    plotly.graph_objects.Scatter(
        x=t,
        y=professionnals,
        name="Télépilotes professionnels en France",
        showlegend=False,
    ),
)

if __name__ == "__main__":
    fig_nb_drones.show()
    fig_nb_drones.write_image("fig_nb_drones.png")
    fig_nb_pro.show()
    fig_nb_pro.write_image("fig_nb_pro.png")
