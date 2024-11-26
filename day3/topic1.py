from manim import *
from manim import AnimationGroup as Parallel

class Topic1:
    title = Text("What is a control flow?", font_size=36).to_edge(UP).shift(DOWN * 0.5)
    code = Code(
        code = 
            """
System.out.println("Hello, World!");
int x = 5;
x = x + 1;
            """.strip(),
        language = "java",
    ).shift(UP * 0.75)

    code_header = Text("A normal program runs from top to bottom", font_size=24).next_to(code, UP, buff=0.25)
    code_sub = Text("This is called a control flow", font_size=24).next_to(code, DOWN, buff=0.25)
    pointer = Triangle(stroke_width=2, color=BLUE).scale(0.1).rotate(-PI/2).next_to(code, LEFT, buff=0.1).shift(UP * 0.3)

    info = Text("When the code you write is running, it will ALWAYS work like this.", font_size=24).next_to(code_sub, DOWN, buff=0.75)
    info2 = Text("We are going to learn what happens behind-the-scenes", font_size=24).next_to(info, DOWN, buff=0.25)

    def create():
        return Parallel(
            Write(Topic1.code, run_time=0.75),
            Write(Topic1.code_header, run_time=0.75),
            Write(Topic1.code_sub, run_time=0.75),
            Create(Topic1.pointer, run_time=0.25),
            Write(Topic1.info, run_time=0.75),
            Write(Topic1.info2, run_time=0.75),
        )
    
    def shift_pointer():
        return Parallel(
            Topic1.pointer.animate.shift(DOWN * 0.3),
            run_time=0.25,
        )
    
    def color_pointer():
        return Parallel(
            Topic1.pointer.animate.set_color(RED),
            run_time=0.25,
        )
    
    def remove():
        return Parallel(
            Unwrite(Topic1.info, run_time=0.25),
            Unwrite(Topic1.info2, run_time=0.25),
            Uncreate(Topic1.pointer, run_time=0.25),
            Unwrite(Topic1.code, run_time=0.25),
            Unwrite(Topic1.code_header, run_time=0.25),
            Unwrite(Topic1.code_sub, run_time=0.25),
        )