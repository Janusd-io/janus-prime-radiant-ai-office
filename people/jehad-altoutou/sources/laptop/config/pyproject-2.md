---
type: source
source_type: laptop
title: pyproject
slug: pyproject-2
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/pyproject.toml
original_size: 714
original_ext: .toml
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:36Z"
---

# pyproject

_Extracted from `brightbean-studio/pyproject.toml` on 2026-05-14._

```toml
[tool.ruff]
target-version = "py312"
line-length = 120

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W", "UP", "B", "SIM"]
ignore = [
    "E501",  # line too long (handled by ruff format)
]

[tool.ruff.lint.isort]
known-first-party = ["apps", "config"]

[tool.mypy]
python_version = "3.12"
plugins = ["mypy_django_plugin.main"]
ignore_missing_imports = true

[tool.django-stubs]
django_settings_module = "config.settings.development"

[tool.pytest.ini_options]
DJANGO_SETTINGS_MODULE = "config.settings.test"
python_files = ["tests.py", "test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --tb=short"

[tool.coverage.run]
source = ["apps"]
omit = ["*/migrations/*", "*/tests/*"]

```