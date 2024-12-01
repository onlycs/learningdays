from manim import NumberPlane, Scene, Text
from manim import Write, Succession as Sequence, Wait
from manim_slides.slide.manim import Slide

from title import Title
from home import Home

from topic import TopicScheduler
from topic1 import Topic1
from topic2 import Topic2
from topic3 import Topic3
from topic4 import Topic4
from topic5 import Topic5

class Day4(Slide, Scene):
    def construct(self):
        s = TopicScheduler(
            [
                Title(), 
                Topic1(), 
                Topic2(), 
                Topic3(),
                Topic4(),
                Topic5(),
            ],
            Home(),
        )

        self.next_slide()
        slide = 0

        while slide < s.num_slides:
            self.next_slide()
            self.play(Sequence(
                s.next_slide(),
                Wait(0.1)
            ))
            slide += 1

        self.next_slide()

        self.play(s.destroy())
        self.play(Write(Text("Questions?", font_size=48)))