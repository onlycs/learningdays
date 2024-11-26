from manim import *
from manim import AnimationGroup as Parallel

class Title:
    title = Text("Learning Day 3")
    desc = Text("A Robot's Control Flow").shift(DOWN)

    def transition_in(title = title, desc = desc):
        return Parallel(Write(title, run_time=0.75), Write(desc, run_time=0.75))

    def transition_out(title = title, desc = desc):
        return Parallel(Unwrite(title, run_time=0.25), desc.animate.scale(0.5).to_corner(UL))