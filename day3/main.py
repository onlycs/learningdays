from manim import *
from manim import AnimationGroup as Parallel, Succession as Sequence
from manim_slides.slide.manim import Slide

from title import Title
from home import Home
from topic1 import Topic1
from topic2 import Topic2

class Day3(Slide, Scene):
    def construct(self):
        self.play(Title.transition_in())
        self.next_slide()

        topic1 = Home.topic1.copy()
        topic2 = Home.topic2.copy()
        topic3 = Home.topic3.copy()

        self.play(
            Sequence(
                Title.transition_out(),
                Home.transition_in(self, topic1, topic2, topic3),
            ),
        )

        self.next_slide()

        self.play(Sequence(
            Home.transition_out(self, 1, topic1, topic2, topic3),
            Topic1.create(),
        ))

        self.next_slide()
        self.play(Topic1.shift_pointer())

        self.wait(0.3)
        self.play(Topic1.shift_pointer())
        self.play(Topic1.color_pointer())

        self.wait(0.3)
        self.next_slide()

        topic2 = Home.topic2.copy()
        topic3 = Home.topic3.copy()

        self.play(Sequence(
            Topic1.remove(),
            Home.transition_in(self, topic1, topic2, topic3),
        ))

        self.next_slide()

        self.play(Sequence(
            Home.transition_out(self, 2, topic1, topic2, topic3),
            Topic2.create(),
        ))

        self.next_slide()
        self.play(Topic2.create_step1())
        self.next_slide()
        self.play(Topic2.create_step2())
        self.next_slide()
        self.play(Topic2.create_step3())
        self.next_slide()

        topic1 = Home.topic1.copy()
        topic3 = Home.topic3.copy()
        self.play(Sequence(
            Topic2.end(),
            Home.transition_in(self, topic1, topic2, topic3),
        ))

        pass
