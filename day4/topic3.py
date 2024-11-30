from manim import Text, Code, Paragraph
from manim import Write, Unwrite, AnimationGroup as Parallel
from manim import UP, DOWN
from manim import WHITE, BLUE

from codetxt import *
from topic import Topic

class Topic3(Topic):
    title: Text = Text("public void execute() {}", font_size=24, **code_kwargs).to_edge(UP).shift(DOWN * 0.5)
    
    code = Code(
        code = """
public void execute() {
    System.out.println("execute() called");

    drivetrain.move(0.5, 0);
}
""".strip(),
        language="java",
        font_size=18
    ).shift(UP)
    footer = Text("Execute method example", font_size=14).next_to(code, DOWN)

    txtargs = {
        "font_size": 28,
        "color": WHITE,
        "t2c": {
            "1.": BLUE,
            "2.": BLUE,
            "3.": BLUE,
        },
        "alignment": "center"
    }

    point1 = Paragraph("1. The execute method is run every tick", "where the command is in the \"scheduled\" box", **txtargs).shift(DOWN * 1.5)
    point2 = Paragraph("2. The execute method is run every 20ms.", **txtargs).next_to(point1, DOWN)
    point3 = Paragraph("3. The execute method is the main body of the \"while loop\"", **txtargs).next_to(point2, DOWN)

    slide: int = -1
    num_slides: int = 3
    items = [point1, point2, point3]

    def create(self):
        return Parallel(
            Write(self.code, run_time=0.75),
            Write(self.footer, run_time=0.75),
        )
    
    def next_slide(self):
        self.slide += 1
        return Write(self.items[self.slide], run_time=0.75)
    
    def destroy(self):
        return Parallel(
            Unwrite(self.code, run_time=0.25),
            Unwrite(self.footer, run_time=0.25),
            *[Unwrite(item, run_time=0.25) for item in self.items]
        )
    
