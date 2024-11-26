def main [ file: string, run: string ] {
	manim-slides render $file $run
	manim-slides present $run --hide-info-window -F
}