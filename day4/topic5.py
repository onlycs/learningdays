from manim import Text, Code, Paragraph, VGroup, SurroundingRectangle
from manim import Write, Unwrite, AnimationGroup as Parallel, Create, Uncreate, VMobject
from manim import UP, DOWN
from manim import WHITE, BLUE

from codetxt import *
from topic import Topic

class Topic5(Topic):
    title: Text = Text("public void end(boolean interrupted) {}", font_size=24, **code_kwargs).to_edge(UP).shift(DOWN * 0.5)
    
    code = Code(
        code = """
public void end(boolean interrupted) {
    drivetrain.stop();
    arm.stop();
}
""".strip(),
        language="java",
        font_size=18
    ).shift(UP)
    footer = Text("isFinished method example", font_size=14).next_to(code, DOWN)

    txtargs = {
        "font_size": 28,
        "color": WHITE,
        "t2c": {
            "1.": BLUE,
            "2.": BLUE,
            "3.": BLUE,
        },
        "t2f": {
            "interrupted": "monospace",
            "CommandScheduler": "monospace",
        },
        "alignment": "center"
    }

    lines: list[VGroup] = code.code.lines[0]
    bbox1obj = lines[0].submobjects[len("public void end"):-2]
    bbox2obj = [
        mobj
        for sublist in [l.submobjects[4:] for l in lines[1:-1]]
        for mobj in sublist
    ]

    bbox_args = {
        "buff": 0.1,
        "corner_radius": 0.2,
        "color": BLUE,
        "stroke_width": 2,
    }

    bbox1 = SurroundingRectangle(VGroup(*bbox1obj), **bbox_args)
    bbox2 = SurroundingRectangle(VGroup(*bbox2obj), **bbox_args)
    point1 = Paragraph("1. The end method runs once a command has finished", **txtargs).shift(DOWN * 1.5)
    point2 = Paragraph("2. interrupted is true when the CommandScheduler", "\"destroys\" the command", **txtargs).next_to(point1, DOWN)
    point3 = Paragraph("3. All ending logic goes in this part. It is what runs after the while loop", **txtargs).next_to(point2, DOWN)

    slide: int = -1
    num_slides: int = 3
    items = [point1, [point2, bbox1], [point3, bbox2]]

    def create(self):
        return Parallel(
            Write(self.code, run_time=0.75),
            Write(self.footer, run_time=0.75),
        )
    
    def next_slide(self):
        self.slide += 1

        if self.slide == 0: return Write(self.items[self.slide], run_time=0.75)
        elif self.slide == 1:
            return Parallel(
                Write(self.items[self.slide][0], run_time=0.75),
                Create(self.items[self.slide][1], run_time=0.75),
            )
        elif self.slide == 2:
            return Parallel(
                Write(self.items[self.slide][0], run_time=0.75),
                Create(self.items[self.slide][1], run_time=0.75),
                Uncreate(self.items[self.slide - 1][1], run_time=0.25),
            )
    
    def destroy(self):
        return Parallel(
            Unwrite(self.code, run_time=0.25),
            Unwrite(self.footer, run_time=0.25),
            *[Unwrite(item, run_time=0.25) for item in self.items if isinstance(item, VMobject)],
            *[[Unwrite(item[0], run_time=0.25), Uncreate(item[1], run_time=0.25)] for item in self.items if isinstance(item, list)]
        )
    
