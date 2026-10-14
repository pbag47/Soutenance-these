
import manim
import numpy


manim.config.media_width = "75%"
manim.config.verbosity = "WARNING"
manim.config.transparent = True
manim.config.format = "webm"


class WienerAnimation(manim.Scene):
    def construct(self):
        number_of_samples = 100
        time_series = [t for t in range(number_of_samples)]
        input_signal = numpy.squeeze(numpy.array([numpy.random.randn() for _ in range(number_of_samples)]))
        real_process_filter = numpy.squeeze(numpy.array([0, 0, 0.5, 0.1]))
        output_signal = numpy.convolve(input_signal, real_process_filter, mode='same')

        print(input_signal.shape)
        print(output_signal.shape)
        print(len(time_series))

        # Create a time graph
        input_axes = manim.Axes(
            x_range=[0, 1],
            y_range=[0, 1],
            axis_config={"color": manim.WHITE},
        )
        output_axes = manim.Axes(
            x_range=time_series,
            y_range=output_signal,
            axis_config={"color": manim.WHITE},
        )
        wiener_equation = manim.MathTex(
            r"H_n = R_n^{-1} C_n"
        )
        self.play(manim.Create(input_axes), manim.Create(output_axes), manim.Write(wiener_equation))
        self.wait()


class CircleToSquare(manim.Scene):
    def construct(self):
        blue_circle = manim.Circle(color=manim.BLUE, fill_opacity=0.5)
        green_square = manim.Square(color=manim.GREEN, fill_opacity=0.8)
        self.play(manim.Create(blue_circle))
        self.wait()
        
        self.play(manim.Transform(blue_circle, green_square))
        self.wait()


if __name__ == "__main__":
    scene = WienerAnimation()
    scene.render()
    print("OK")


