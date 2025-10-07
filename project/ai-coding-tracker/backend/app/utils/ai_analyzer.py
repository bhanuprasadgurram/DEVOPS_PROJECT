import re
from typing import Dict, List

class AIAnalyzer:
    def __init__(self):
        self.keywords = {
            "python": ["def", "class", "import", "for", "while", "if", "return"],
            "javascript": ["function", "const", "let", "var", "return", "=>"],
            "java": ["public", "private", "class", "void", "return"],
        }

    def analyze_code(self, code: str, language: str, challenge_title: str = "") -> Dict:
        analysis = {
            "quality_score": 0,
            "strengths": [],
            "suggestions": [],
            "complexity": "unknown",
            "readability": "unknown",
            "best_practices": []
        }

        lines = code.strip().split('\n')
        total_lines = len(lines)
        non_empty_lines = len([line for line in lines if line.strip()])

        analysis["quality_score"] = self._calculate_quality_score(code, language, total_lines)
        analysis["complexity"] = self._assess_complexity(code, total_lines)
        analysis["readability"] = self._assess_readability(code, non_empty_lines)
        analysis["strengths"] = self._identify_strengths(code, language)
        analysis["suggestions"] = self._generate_suggestions(code, language, total_lines)
        analysis["best_practices"] = self._check_best_practices(code, language)

        return analysis

    def _calculate_quality_score(self, code: str, language: str, total_lines: int) -> int:
        score = 50

        if total_lines > 5:
            score += 10
        if total_lines > 10:
            score += 10

        if language.lower() in ["python", "javascript"]:
            if "def " in code or "function " in code:
                score += 15
            if any(keyword in code for keyword in ["for", "while"]):
                score += 10
            if "return" in code:
                score += 5

        if re.search(r'#.*|//.*|""".*"""', code):
            score += 10

        return min(score, 100)

    def _assess_complexity(self, code: str, total_lines: int) -> str:
        complexity_indicators = len(re.findall(r'\b(for|while|if|elif|else)\b', code))

        if complexity_indicators == 0:
            return "low"
        elif complexity_indicators <= 3:
            return "moderate"
        else:
            return "high"

    def _assess_readability(self, code: str, non_empty_lines: int) -> str:
        has_comments = bool(re.search(r'#.*|//.*|/\*.*\*/|""".*"""', code))
        avg_line_length = len(code) / max(non_empty_lines, 1)

        if has_comments and avg_line_length < 80:
            return "excellent"
        elif avg_line_length < 100:
            return "good"
        else:
            return "needs improvement"

    def _identify_strengths(self, code: str, language: str) -> List[str]:
        strengths = []

        if re.search(r'#.*|//.*|""".*"""', code):
            strengths.append("Code includes helpful comments")

        if re.search(r'\bdef\s+\w+\(|function\s+\w+\(', code):
            strengths.append("Uses functions for code organization")

        if re.search(r'\breturn\b', code):
            strengths.append("Properly returns values")

        if language.lower() == "python":
            if re.search(r'^\s{4}', code, re.MULTILINE):
                strengths.append("Follows proper Python indentation")

        if not strengths:
            strengths.append("Code is concise")

        return strengths

    def _generate_suggestions(self, code: str, language: str, total_lines: int) -> List[str]:
        suggestions = []

        if not re.search(r'#.*|//.*|""".*"""', code):
            suggestions.append("Add comments to explain your logic")

        if total_lines < 5:
            suggestions.append("Consider adding more detailed implementation")

        if not re.search(r'\bdef\s+\w+\(|function\s+\w+\(', code):
            suggestions.append("Consider breaking code into reusable functions")

        if language.lower() == "python":
            if not re.search(r'^\s{4}', code, re.MULTILINE):
                suggestions.append("Ensure consistent indentation (4 spaces recommended)")

        lines = code.split('\n')
        long_lines = [i for i, line in enumerate(lines) if len(line) > 100]
        if long_lines:
            suggestions.append("Consider breaking long lines for better readability")

        if not re.search(r'\btry\b.*\bexcept\b', code, re.DOTALL):
            suggestions.append("Consider adding error handling for edge cases")

        if not suggestions:
            suggestions.append("Great work! Code looks solid.")

        return suggestions

    def _check_best_practices(self, code: str, language: str) -> List[str]:
        practices = []

        if language.lower() == "python":
            if re.search(r'^[a-z_][a-z0-9_]*\s*=', code, re.MULTILINE):
                practices.append("Uses snake_case variable naming")
            if re.search(r'^\s*""".*?"""', code, re.MULTILINE | re.DOTALL):
                practices.append("Includes docstrings")

        if language.lower() == "javascript":
            if re.search(r'\bconst\b|\blet\b', code):
                practices.append("Uses modern ES6+ syntax")
            if re.search(r'=>', code):
                practices.append("Uses arrow functions")

        if re.search(r'\bif\s+\w+\s*(==|!=|>|<|>=|<=)', code):
            practices.append("Uses conditional logic")

        if re.search(r'\b(for|while)\b', code):
            practices.append("Implements iterative solutions")

        return practices

analyzer = AIAnalyzer()
