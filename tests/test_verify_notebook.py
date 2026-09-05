"""Tests for scripts/verify_notebook.py.

Covers span counting across all four LaTeX delimiter styles, emoji vs
mathematical-unicode discrimination, marketing-word matching, notebook-type
classification, and an end-to-end pass/fail over the two fixture notebooks
under tests/fixtures/.
"""

import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import verify_notebook as vn  # noqa: E402


# --------------------------------------------------------------------------
# span counting
# --------------------------------------------------------------------------


class TestLatexSpans:
    def test_inline_single_dollar(self):
        assert vn.count_latex_spans("The value is $x$ here.") == 1

    def test_display_double_dollar_is_one_span(self):
        text = "before $$x = y$$ after"
        assert vn.count_latex_spans(text) == 1

    def test_double_dollar_not_double_counted_as_two_inline(self):
        # A naive char-count (text.count('$') // 2) would call this 2 spans;
        # tokenising must call it 1.
        text = "$$ \\hat{\\beta} = (X^\\top X)^{-1} X^\\top y $$"
        assert vn.count_latex_spans(text) == 1

    def test_multiple_inline_spans(self):
        text = "$a$ and $b$ and $c$"
        assert vn.count_latex_spans(text) == 3

    def test_paren_delimited_inline(self):
        text = "The term \\( \\sigma^2 \\) is the variance."
        assert vn.count_latex_spans(text) == 1

    def test_bracket_delimited_display(self):
        text = "\\[ \\nabla_\\beta L = 0 \\]"
        assert vn.count_latex_spans(text) == 1

    def test_begin_equation_block(self):
        text = "\\begin{equation}\nx = y\n\\end{equation}"
        assert vn.count_latex_spans(text) == 1

    def test_begin_align_block(self):
        text = "\\begin{align}\nx &= y \\\\\nz &= w\n\\end{align}"
        assert vn.count_latex_spans(text) == 1

    def test_begin_aligned_and_gather(self):
        assert vn.count_latex_spans("\\begin{aligned}x=y\\end{aligned}") == 1
        assert vn.count_latex_spans("\\begin{gather}x=y\\end{gather}") == 1

    def test_starred_environment(self):
        assert vn.count_latex_spans("\\begin{align*}x=y\\end{align*}") == 1

    def test_escaped_dollar_is_currency_not_math(self):
        text = "This costs \\$5 in compute."
        assert vn.count_latex_spans(text) == 0

    def test_escaped_dollar_does_not_break_later_math(self):
        text = "It costs \\$5, but $x = 1$ still holds."
        assert vn.count_latex_spans(text) == 1

    def test_mixed_delimiter_styles_all_counted(self):
        text = "$a$ then $$b$$ then \\(c\\) then \\[d\\] then \\begin{equation}e\\end{equation}"
        assert vn.count_latex_spans(text) == 5

    def test_unterminated_dollar_opens_no_span(self):
        text = "An orphan $ sign with no closer."
        assert vn.count_latex_spans(text) == 0

    def test_no_math_at_all(self):
        assert vn.count_latex_spans("Plain prose, no maths here.") == 0

    def test_display_dollar_blocks_reported_separately(self):
        total, display = vn.scan_latex("$a$ $$b$$ $$c$$")
        assert total == 3
        assert display == 2


# --------------------------------------------------------------------------
# emoji vs mathematical unicode
# --------------------------------------------------------------------------


class TestEmojiDiscrimination:
    def test_plain_text_has_no_emoji(self):
        assert vn.count_emoji("Just words and numbers 123.") == 0

    def test_rocket_and_party_emoji_counted(self):
        assert vn.count_emoji("Ship it \U0001F680 \U0001F389") == 2

    def test_dingbat_range_counted(self):
        # U+2705 WHITE HEAVY CHECK MARK falls in the 2600-27BF dingbat range.
        assert vn.count_emoji("Done \u2705") == 1

    def test_variation_selector_and_zwj_counted(self):
        assert vn.count_emoji("\uFE0F") == 1
        assert vn.count_emoji("\u200D") == 1

    def test_mathematical_unicode_exempt(self):
        text = "\u27FA \u27F9 \u2264 \u2265 \u2260 \u2208 \u2211 \u220F \u2202 \u2207"
        assert vn.count_emoji(text) == 0

    def test_mixed_math_and_emoji(self):
        text = "\u2264 is fine but \U0001F680 is not"
        assert vn.count_emoji(text) == 1


# --------------------------------------------------------------------------
# marketing language
# --------------------------------------------------------------------------


class TestMarketingHits:
    def test_no_marketing_language(self):
        assert vn.count_marketing("A standard regression model.") == 0

    def test_single_term_case_insensitive(self):
        assert vn.count_marketing("This is a BREAKTHROUGH result.") == 1

    def test_hyphen_or_space_variant(self):
        assert vn.count_marketing("An industry-standard approach.") == 1
        assert vn.count_marketing("An industry standard approach.") == 1

    def test_multi_word_term(self):
        assert vn.count_marketing("This is the most important step.") == 1

    def test_multiple_distinct_terms(self):
        text = "A revolutionary, cutting-edge, game-changing approach."
        assert vn.count_marketing(text) == 3

    def test_whole_word_boundary_not_substring(self):
        # "amazing" should not match inside an unrelated longer word.
        assert vn.count_marketing("Thisisamazinglyunrelated") == 0


# --------------------------------------------------------------------------
# type classification
# --------------------------------------------------------------------------


class TestClassify:
    def test_a_suffix_is_theory(self):
        assert vn.classify(Path("0a_linear_regression_theory.ipynb")) == "theory"

    def test_b_suffix_is_practical(self):
        assert vn.classify(Path("1b_logistic_regression_practical.ipynb")) == "practical"

    def test_c_d_e_f_suffixes_are_practical(self):
        for letter in "cdef":
            assert vn.classify(Path(f"9{letter}_something.ipynb")) == "practical"

    def test_theory_in_filename_overrides_letter(self):
        assert vn.classify(Path("9c_rnn_theory.ipynb")) == "theory"

    def test_explicit_forced_type_wins(self):
        assert vn.classify(Path("0a_theory.ipynb"), forced="practical") == "practical"
        assert vn.classify(Path("1b_practical.ipynb"), forced="theory") == "theory"


# --------------------------------------------------------------------------
# end-to-end on fixture notebooks
# --------------------------------------------------------------------------


FIXTURES = REPO_ROOT / "tests" / "fixtures"


class TestFixturesEndToEnd:
    def test_fixtures_exist(self):
        assert (FIXTURES / "3b_fixture_practical.ipynb").is_file()
        assert (FIXTURES / "3c_fixture_failing.ipynb").is_file()

    def test_passing_fixture_passes(self, tmp_path):
        result = vn.verify_one(
            FIXTURES / "3b_fixture_practical.ipynb",
            _args(report_dir=str(tmp_path)),
            tmp_path,
        )
        assert result["passed"] is True, result["checks"]
        assert result["type"] == "practical"
        assert result["metrics"]["latex_spans"] >= vn.PRACTICAL_MIN_SPANS

    def test_failing_fixture_fails(self, tmp_path):
        result = vn.verify_one(
            FIXTURES / "3c_fixture_failing.ipynb",
            _args(report_dir=str(tmp_path)),
            tmp_path,
        )
        assert result["passed"] is False
        failed_checks = {c["name"] for c in result["checks"] if not c["ok"]}
        assert "latex_spans" in failed_checks
        assert "emoji_count" in failed_checks
        assert "marketing_hits" in failed_checks
        assert "has_title" in failed_checks
        assert "has_references" in failed_checks

    def test_cli_all_over_fixtures_exit_code(self, tmp_path, monkeypatch):
        argv = [
            str(FIXTURES / "3b_fixture_practical.ipynb"),
            str(FIXTURES / "3c_fixture_failing.ipynb"),
            "--report-dir",
            str(tmp_path),
        ]
        code = vn.main(argv)
        assert code == 1  # one of the two fixtures fails
        summary_files = list(tmp_path.glob("*.json"))
        assert len(summary_files) == 2


def _args(**overrides):
    class Args:
        type = "auto"
        execute = False
        timeout = 900
        report_dir = "reports/verify"
        record_feature = ""
        json = False
        syntax_only = False
        min_free_mb = 3000
        max_mem_mb = 2048
        threads = 4

    a = Args()
    for k, v in overrides.items():
        setattr(a, k, v)
    return a


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-q"]))
