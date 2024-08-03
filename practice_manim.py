from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.rotate(PI / 4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

    class SquareAndCircle(Scene):
        def construct(self):
            circle = Circle()
            circle.set_fill(PINK, opacity=0.5)

            square = Square()
            square.set_fill(BLUE, opacity=0.5)
            square.next_to(circle, RIGHT, buff=0.5)

            self.play(Create(circle), Create(square))
            class AnimatedSquareToCircle(Scene):
                    def construct(self):
                        circle = Circle()  # create a circle
                        square = Square()  # create a square

            self.play(Create(square))  # show the square on screen
            self.play(square.animate.rotate(PI / 4))  # rotate the square
            self.play(Transform(square, circle))  # transform the square into a circle
            self.play(
                square.animate.set_fill(PINK, opacity=0.5)
            )  # color the circle on screen


