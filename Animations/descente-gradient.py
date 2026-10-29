
import plotly
import numpy


x = numpy.arange(0, 1, 0.01)
error = -5*x + 2
error_squared = numpy.square(error)


fig_error = plotly.graph_objects.Figure(
    layout=dict(
        title_text=r"$\text{Erreur}~e_n$",
        title_font_size=30,
        template="plotly_dark",
        autosize=False,
        width=350,
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
        xaxis_title_text=r"$H_n(i)$",
        xaxis_title_font_size=20,
        xaxis_exponentformat = "power",
        yaxis_title_text=r"$e_n$",
    )
)
fig_error.add_trace(
    plotly.graph_objects.Scatter(
        x=x,
        y=error,
        name="Erreur en fonction d'une composante de H_n",
        showlegend=False,
    ),
)

fig_error_squared = plotly.graph_objects.Figure(
    layout=dict(
        title_text=r"$\text{Erreur quadratique}~e_n^2$",
        title_font_size=30,
        template="plotly_dark",
        autosize=False,
        width=350,
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
        xaxis_title_text=r"$H_n(i)$",
        xaxis_title_font_size=20,
        xaxis_exponentformat = "power",
        yaxis_title_text=r"$e_n^2$",
    )
)
fig_error_squared.add_trace(
    plotly.graph_objects.Scatter(
        x=x,
        y=error_squared,
        name="Erreur quadratique en fonction d'une composante de H_n",
        showlegend=False,
    ),
)

if __name__ == "__main__":
    fig_error.show()
    fig_error.write_image("fig_grad_error.png")
    fig_error_squared.show()
    fig_error_squared.write_image("fig_grad_error_squared.png")
