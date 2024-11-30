from manim import Text, Code, VGroup, SurroundingRectangle
from manim import Write, Create, Uncreate, AnimationGroup as Parallel
from manim import UP, DOWN
from manim import BLUE


from codetxt import *
from topic import Topic

class Topic1(Topic):
    title: Text = Text("public ExampleCommand() {}", font_size=24, **code_kwargs).to_edge(UP).shift(DOWN * 0.5) 
    
    code = Code(
        code = 
            """
final Drivetrain drivetrain;
final Arm arm;

public ExampleCommand(Drivetrain drivetrain, Arm arm) {
    this.drivetrain = drivetrain;
    this.arm = arm;

    addRequirements(drivetrain, arm);
}
            """.strip(),
        language = "java",
    )

    lines: list[VGroup] = code.code.lines[0]

    bbox1obj = lines[3].submobjects[21:-2]
    bbox2obj = lines[:2]
    bbox3obj = [
        mobj
        for sublist in [l.submobjects[4:] for l in lines[4:6]]
        for mobj in sublist
    ]
    bbox4obj = lines[7].submobjects[4:]

    bbox_args = {
        "buff": 0.1,
        "corner_radius": 0.2,
        "color": BLUE,
        "stroke_width": 2,
    }

    bbox1 = SurroundingRectangle(VGroup(*bbox1obj), **bbox_args)
    bbox2 = SurroundingRectangle(VGroup(*bbox2obj), **bbox_args)
    bbox3 = SurroundingRectangle(VGroup(*bbox3obj), **bbox_args)
    bbox4 = SurroundingRectangle(VGroup(*bbox4obj), **bbox_args)

    current_slide: int = -1
    num_slides: int = 4
    items = [bbox1, bbox2, bbox3, bbox4]

    def create(self):
        return Parallel(
            Write(self.code, run_time=0.75),
        )
    
    def next_slide(self):
        self.current_slide += 1
        bbox = self.items[self.current_slide]

        if self.current_slide == 0:
            return Create(bbox, run_time=0.75)

        return Parallel(
            Uncreate(self.items[self.current_slide - 1], run_time=0.25),
            Create(bbox, run_time=0.75),
        )
    
    def destroy(self):
        return Parallel(
            Uncreate(self.code, run_time=0.25),
            Uncreate(self.items[self.current_slide], run_time=0.25),
        )