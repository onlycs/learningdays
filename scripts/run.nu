def main [ 
	file: string
	run: string
	--nogen (-n) 
] {
	if not ($nogen) {
		manim-slides render $file $run
	}

	manim-slides present $run --hide-info-window -F
}