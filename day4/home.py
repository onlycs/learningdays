from manim import Text, Code
from manim import Write, Transform, Create, Unwrite, AnimationGroup as Parallel
from manim import UP, DOWN

from codetxt import t2c

class Home:
    subtitle_orig = Text("An Example Command", font_size=42).to_edge(UP).shift(DOWN * 0.5)
    subtitle = subtitle_orig.copy()

    code_orig = Code(
        code = """
public class ExampleCommand extends Command {
    public ExampleCommand() {
        ...
    }

    public void initialize() {
        ...
    }

    public void execute() {
        ...
    }

    public boolean isFinished() {
        ...
    }

    public void end(boolean interrupted) {
        ...
    }
}
        """.strip(),
        language="java",
        font_size=18
    ).shift(DOWN)

    code = code_orig.copy()

    def init(self):
        return Parallel(
            Write(self.subtitle, run_time=0.75),
            Write(self.code, run_time=0.75),
        )

    def transition_in(self):
        self.code.line_numbers = self.code_orig.line_numbers.copy()
        self.code.background_mobject = self.code_orig.background_mobject.copy().set_z_index(-1)
        self.subtitle = self.subtitle_orig.copy()

        return Parallel(
            Write(self.code.line_numbers, run_time=0.75),
            Create(self.code.background_mobject, run_time=0.75),
            Write(self.subtitle, run_time=0.75),
            Transform(self.code.code, self.code_orig.code.copy(), run_time=0.725),
        )

    def transition_out(self, title: Text):
        return Parallel(
            Unwrite(self.subtitle, run_time=0.25),
            Unwrite(self.code.background_mobject, run_time=0.25),
            Unwrite(self.code.line_numbers, run_time=0.25),
            Transform(self.code.code, title, run_time=0.75),
        )
    
    def destroy(self):
        return Parallel(
            Unwrite(self.subtitle, run_time=0.25),
            Unwrite(self.code, run_time=0.25),
            Unwrite(self.code.line_numbers, run_time=0.25),
            Unwrite(self.code.background_mobject, run_time=0.25),
        )