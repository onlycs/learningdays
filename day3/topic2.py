from manim import *
from manim import AnimationGroup as Parallel, Succession as Sequence

class Step1:
    title = Text("Run the Subsystem \"periodic\" methods", font_size=24).shift(UP*2 + RIGHT)
    code = Code(
        code = """
class Arm extends Subsystem {
    ...
    public void periodic() {
        System.out.println("This is a periodic method");
    }
    ...
}
""".strip(),
        language="java",
        font_size=18
    ).shift(RIGHT + DOWN)
    footer = Text("Example of a periodic method in a subsystem", font_size=18).next_to(code, DOWN)

    def create():
        return Parallel(
            Write(Step1.title, run_time=1),
            Write(Step1.code, run_time=1),
            Write(Step1.footer, run_time=1),
        )
    
    def remove():
        return Parallel(
            Unwrite(Step1.title, run_time=0.25),
            Unwrite(Step1.code, run_time=0.25),
            Unwrite(Step1.footer, run_time=0.25),
        )
    
class Step2:
    title = Text('Check for button presses', font_size=24).shift(UP*2 + RIGHT)
    code = Code(
        code = """
...
controller.x().onTrue(new PivotArm());
...
""".strip(),
        language="java",
        font_size=18
    ).shift(RIGHT + DOWN)
    footer = Text("Example of a button press handler", font_size=18).next_to(code, DOWN)

    def create():
        return Parallel(
            Write(Step2.title, run_time=1),
            Write(Step2.code, run_time=1),
            Write(Step2.footer, run_time=1),
        )
    
    def remove():
        return Parallel(
            Unwrite(Step2.title, run_time=0.25),
            Unwrite(Step2.code, run_time=0.25),
            Unwrite(Step2.footer, run_time=0.25),
        )
    
class Step3:
    title = Text('Run all commands', font_size=24).shift(UP*2 + RIGHT)
    code = Code(
        code = """
public class PivotArm extends Command {
    public void initialize() {
        System.out.println("PivotArm command initialized");
    }

    public void execute() {
        System.out.println("PivotArm command executed");
    }

    public void end() {
        System.out.println("PivotArm command ended");
    }
}
""",
        language="java",
        font_size=14
    ).shift(RIGHT + DOWN)
    footer = Text("Example of a command", font_size=18).next_to(code, DOWN)

    def create():
        return Parallel(
            Write(Step3.title, run_time=1),
            Write(Step3.code, run_time=1),
            Write(Step3.footer, run_time=1),
        )
    
    def remove():
        return Parallel(
            Unwrite(Step3.title, run_time=0.25),
            Unwrite(Step3.code, run_time=0.25),
            Unwrite(Step3.footer, run_time=0.25),
        )

class Topic2:
    title = Text("How does a robot's control flow work?", font_size=24).to_corner(UL).shift(DOWN * 0.5)

    scheduler = RoundedRectangle(
        width=1,
        height=6,
        corner_radius=0.25,
        color=RED,
    ).to_corner(DL).set_fill(RED, 0.25)
    scheduler_title = Text("Command Scheduler", font_size=24).rotate(PI/2).next_to(scheduler, RIGHT, buff=-0.6)

    step_rect = RoundedRectangle(
        width=11.5,
        height=1,
        corner_radius=0.25,
        color=YELLOW,
    ).to_corner(UL).shift(DOWN + RIGHT*1.666).set_fill(YELLOW, 0.25)
    data_rect = RoundedRectangle(
        width=11.5,
        height=4.33,
        corner_radius=0.25,
    ).next_to(step_rect, DOWN, buff=0.666)

    
    def create():
        return Parallel(
            DrawBorderThenFill(Topic2.scheduler, run_time=1),
            Write(Topic2.scheduler_title, run_time=1),
        )

    def create_step1():
        return Parallel(
            DrawBorderThenFill(Topic2.step_rect, run_time=1),
            DrawBorderThenFill(Topic2.data_rect, run_time=1),
            Step1.create(),
        )
    

    def create_step2():
        return Sequence(
            Step1.remove(),
            Step2.create(),
        )
    
    def create_step3():
        return Sequence(
            Step2.remove(),
            Step3.create(),
        )
    
    def end():
        return Parallel(
            Step3.remove(),
            Unwrite(Topic2.scheduler_title, run_time=0.25),
            Unwrite(Topic2.scheduler, run_time=0.25),
            Unwrite(Topic2.step_rect, run_time=0.25),
            Unwrite(Topic2.data_rect, run_time=0.25),
        )