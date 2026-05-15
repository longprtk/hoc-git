from pathlib import Path


def test_index_html_exists():
    assert Path("index.html").exists()


def test_style_css_exists():
    assert Path("style.css").exists()


def test_index_has_title():
    content = Path("index.html").read_text(encoding="utf-8")
    assert "Hoc Git CI/CD" in content


def test_index_has_devops_text():
    content = Path("index.html").read_text(encoding="utf-8")
    assert "Xin chào DevOps" in content