from manim import *

config.background_color = BLACK #DARK_BLUE
config.frame_height = 10
config.frame_widthe = 10

config.pixel_height = 500
config.pixel_width = 500

class ChangedDefaults(Scene):
    def construct(self):
        Text.set_default(color=GREEN, font_size=100)
        t = Text("Hello World!", color=RED)
        self.add(t)

        t2 = Text("Goodbye!", font_size=50, color=YELLOW).next_to(t, DOWN)
        self.add(t2)


class Positioning(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)

        #next_to method
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN)
        green_dot.next_to(red_dot, RIGHT + UP)
        self.add(green_dot, red_dot)

        #shift
        s = Square(color=ORANGE)
        s.shift(2 * UP + 4 * RIGHT)
        self.add(s)

        #move_to
        c = Circle(color=PURPLE)
        c.move_to([-3, -2, 0])
        self.add(c)

        #align_to
        c2 = Circle(radius=0.5, color=RED, fill_opacity=0.5)
        c3 = c2.copy().set_color(YELLOW)
        c4 = c2.copy().set_color(ORANGE)
        c2.align_to(s, UP)
        c3.align_to(s, RIGHT)
        c4.align_to(s, UP + RIGHT)
        self.add(c2, c3, c4)

class CriticalPoints(Scene):
    def construct(self):
        c = Circle(color=GREEN, fill_opacity=0.5)
        self.add(c)

        for d in [(0,0,0), UP, UR, RIGHT, DR, DOWN, DL, LEFT, UL]:
            self.add(Cross(scale_factor=0.2).move_to(c.get_critical_point(d)))

        s = Square(color=RED, fill_opacity=0.5)
        s.move_to([1,0,0], aligned_edge=LEFT)
        self.add(s)

from manim.utils.unit import Percent, Pixels

class UsefulUnits(Scene):
    def construct(self):
        for perc in range(5,51,5):
            self.add(Circle(color=RED, radius=perc * Percent(X_AXIS)))
            self.add(Square(color=GREEN, side_length=2*perc * Percent(Y_AXIS)))

            d = Dot()
            d.shift(100 * Pixels * RIGHT)
            self.add(d)

class Grouping(Scene):
    def construct(self):
        red_dot = Dot(color=RED)
        green_dot= Dot(color=GREEN).next_to(red_dot, RIGHT)
        blue_dot = Dot(color=BLUE).next_to(red_dot, UP)
        dot_group = VGroup(red_dot, blue_dot, green_dot)
        dot_group.to_edge(RIGHT)
        self.add(dot_group)

        circles = VGroup(*[Circle(radius=0.1) for _ in range(10)])
        circles.arrange(UP, buff=0.4)
        self.add(circles)

        stars = VGroup(*[Star(color=YELLOW, fill_opacity=0.75).scale(0.5) for _ in range(20)])
        stars.arrange_in_grid(4, 5, buff=0.2)
        self.play(Create(stars, run_time=5))
