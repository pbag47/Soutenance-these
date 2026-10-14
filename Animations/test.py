
import manim

manim.config.media_width = "75%"
manim.config.verbosity = "WARNING"
manim.config.transparent = True
manim.config.format = "webm"


print(manim.__version__)

class CircleToSquare(manim.Scene):
    def construct(self):
        blue_circle = manim.Circle(color=manim.BLUE, fill_opacity=0.5)
        green_square = manim.Square(color=manim.GREEN, fill_opacity=0.8)
        self.play(manim.Create(blue_circle))
        self.wait()
        
        self.play(manim.Transform(blue_circle, green_square))
        self.wait()


if __name__ == "__main__":
    scene = CircleToSquare()
    scene.render()
    print("OK")


