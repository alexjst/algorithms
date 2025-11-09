#!/usr/bin/env python3
"""
Script to add colored boxes to Faire interview questions LaTeX file.
"""

import re

def format_latex_file(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()

    # Pattern to find problem sections (problem statement through constraints)
    # This is a simplified version - we'll need to handle manually for complex cases

    # Pattern 1: Wrap "Python Solution:" blocks in solutionbox
    content = re.sub(
        r'\\textbf\{Python Solution:\}\n(\\begin\{verbatim\}.*?\\end\{verbatim\})',
        r'\\begin{solutionbox}\n\\begin{verbatim}\1\n\\end{verbatim}\n\\end{solutionbox}',
        content,
        flags=re.DOTALL
    )

    # Pattern 2: Wrap Edge Cases & Testing sections in testbox
    content = re.sub(
        r'\\textbf\{Edge Cases & Testing:\}(.*?)(?=\\textbf\{Interview Tips:|\\textit\{Source:|\\subsubsection)',
        lambda m: f'\\begin{{testbox}}\n\\textbf{{Edge Cases:}}{m.group(1)}\\end{{testbox}}\n',
        content,
        flags=re.DOTALL
    )

    with open(output_file, 'w') as f:
        f.write(content)

    print(f"Formatted file written to {output_file}")

if __name__ == "__main__":
    format_latex_file(
        "faire_interview_questions.tex",
        "faire_interview_questions_formatted.tex"
    )
