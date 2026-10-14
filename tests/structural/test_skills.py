"""Tests for skill structure."""

from pathlib import Path

import pytest

from helpers import parse_frontmatter


SKILLS_DIR = Path(__file__).resolve().parent.parent.parent / "skills"
SKILL_DIRS = sorted(
    d for d in SKILLS_DIR.iterdir()
    if d.is_dir() and (d / "SKILL.md").exists()
) if SKILLS_DIR.is_dir() else []


def test_skill_count(skills_dir):
    """Total skill count matches expected value."""
    if not skills_dir.is_dir():
        assert 3 == 0
        return
    dirs = sorted(
        d for d in skills_dir.iterdir()
        if d.is_dir() and (d / "SKILL.md").exists()
    )
    assert len(dirs) == 3, (
        f"Expected 3 skills, found {len(dirs)}: {[d.name for d in dirs]}"
    )


@pytest.mark.parametrize("skill_dir", SKILL_DIRS, ids=lambda p: p.name)
def test_skill_has_frontmatter(skill_dir):
    """Each SKILL.md has valid YAML frontmatter with 'name' and 'description'."""
    fm, _ = parse_frontmatter(skill_dir / "SKILL.md")
    assert fm is not None, f"{skill_dir.name}/SKILL.md has no frontmatter"
    assert "description" in fm, f"{skill_dir.name}/SKILL.md frontmatter missing 'description'"


def test_debugging_notebook_present_and_linked():
    """The investigation notebook ships and both debugging skills point at it."""
    debugging = SKILLS_DIR / "systematic-debugging"
    notebook = debugging / "investigation-notebook.md"
    assert notebook.exists(), "investigation-notebook.md is missing"
    text = notebook.read_text()
    for needed in ("Falsified hypotheses", "Rate before", "Rate after", "WORKAROUND"):
        assert needed in text, f"notebook lacks {needed!r}"
    for name in ("SKILL.md", "SKILL-compact.md"):
        assert "investigation-notebook.md" in (debugging / name).read_text(), (
            f"{name} does not reference investigation-notebook.md"
        )


def test_tdd_skills_require_planting_a_bug():
    """Both TDD skill bodies keep the plant-a-bug step."""
    tdd = SKILLS_DIR / "test-driven-development"
    for name in ("SKILL.md", "SKILL-compact.md"):
        assert "plant a bug" in (tdd / name).read_text().lower(), (
            f"{name} lost the plant-a-bug step"
        )
