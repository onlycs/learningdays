from manim import *
from manim import AnimationGroup as Parallel
from manim_slides.slide.manim import Slide

from topic1 import Topic1
from topic2 import Topic2

class Home:
    subtitle = Text("Main Topics", font_size=42).to_edge(UP).shift(DOWN * 0.5)
    topic2 = Text("2. How does a robot's control flow work?", font_size=36)
    topic1 = Text("1. What is a control flow?", font_size=36).next_to(topic2, UP, buff=0.5)
    topic3 = Text("3. How do I use the control flow?", font_size=36).next_to(topic2, DOWN, buff=0.5)

    def transition_in(slideshow: Slide, topic1 = topic1, topic2 = topic2, topic3 = topic3):
        if topic1 not in slideshow.mobjects and topic2 not in slideshow.mobjects and topic3 not in slideshow.mobjects:
            return Parallel(
                Write(Home.subtitle, run_time=0.75),
                Write(topic1, run_time=0.75),
                Write(topic2, run_time=0.75),
                Write(topic3, run_time=0.75),
            )
        elif topic1 in slideshow.mobjects:
            return Parallel(
                Transform(topic1, Home.topic1),
                Write(Home.subtitle, run_time=0.75),
                Write(topic2, run_time=0.75),
                Write(topic3, run_time=0.75),
            )
        elif topic2 in slideshow.mobjects:
            return Parallel(
                Transform(topic2, Home.topic2),
                Write(Home.subtitle, run_time=0.75),
                Write(topic1, run_time=0.75),
                Write(topic3, run_time=0.75),
            )
        elif topic3 in slideshow.mobjects:
            return Parallel(
                Transform(topic3, Home.topic3),
                Write(Home.subtitle, run_time=0.75),
                Write(topic1, run_time=0.75),
                Write(topic2, run_time=0.75),
            )
        
    def transition_out(slideshow: Slide, to_topic: int | None, topic1 = topic1, topic2 = topic2, topic3 = topic3):
        if to_topic is None or to_topic > 3 or to_topic < 1:
            return Parallel(
                Unwrite(Home.subtitle, run_time=0.25),
                Unwrite(topic1, run_time=0.25),
                Unwrite(topic2, run_time=0.25),
                Unwrite(topic3, run_time=0.25),
            )
        elif to_topic == 1:
            return Parallel(
                Unwrite(Home.subtitle, run_time=0.25),
                Unwrite(topic2, run_time=0.25),
                Unwrite(topic3, run_time=0.25),
                Transform(topic1, Topic1.title),
            )
        elif to_topic == 2:
            return Parallel(
                Unwrite(Home.subtitle, run_time=0.25),
                Unwrite(topic1, run_time=0.25),
                Unwrite(topic3, run_time=0.25),
                Transform(topic2, Topic2.title),
            )
        elif to_topic == 3:
            return Parallel(
                Unwrite(Home.subtitle, run_time=0.25),
                Unwrite(topic1, run_time=0.25),
                Unwrite(topic2, run_time=0.25),
                Transform(topic3, Text("How do I use the control flow?", font_size=36).to_edge(UP).shift(DOWN * 0.5),
            ))