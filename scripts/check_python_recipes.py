from __future__ import annotations

from importlib.util import find_spec
from pathlib import Path
import py_compile
import runpy
import sys


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    recipe_files = sorted((root / "python").rglob("*.py"))
    for path in recipe_files:
        py_compile.compile(str(path), doraise=True)

    import_smoke_enabled = find_spec("cutemarkets") is not None
    if import_smoke_enabled:
        for path in recipe_files:
            runpy.run_path(str(path), run_name="__cutemarkets_cookbook_smoke__")
    else:
        print("cutemarkets SDK not installed; skipping optional Python import smoke.")

    print(f"validated_python_recipes={len(recipe_files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
