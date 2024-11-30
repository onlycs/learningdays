from manim import Text
from manim import Write, AnimationGroup as Parallel, Unwrite
from manim import DOWN, UL

from topic import Topic

class Title(Topic):
    title: Text = Text("Learning Day 4")
    desc = Text("Parts of a Command").shift(DOWN)
    num_slides: int = 0
    
    def next_slide(self):
        raise ValueError("No more slides")

    def create(self):
        return Parallel(Write(self.title, run_time=0.75), Write(self.desc, run_time=0.75))

    def destroy(self):
        return Parallel(Unwrite(self.title, run_time=0.25), self.desc.animate.scale(0.5).to_corner(UL)) #type: ignore