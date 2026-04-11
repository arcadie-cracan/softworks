"""
Updates or creates the specified user's code workspace (folder layout, .vscode).

**SOFTWORKS_VSCODE_WORKSPACE** should point to either:

- a **directory** (the code workspace root; created as needed), or
- a **.code-workspace** file (first ``folders[].path`` in the JSON is the root; relative paths
  are resolved against the file's directory).

If unset, Softworks uses ``<effective project root>/softworks_workspace`` and prints a
warning to stderr. The effective project root is ``SOFTWORKS_PROJECT_ROOT`` when set,
otherwise the current working directory.

Example:
   python3 -m softworks.workspace.code_workspace
   python3 -m softworks.workspace.code_workspace --print-root

"""
from __future__ import annotations

import json
import os
import sys
from importlib.resources import path
from pathlib import Path
from shutil import copyfile

from softworks.workspace.workspace_files import dotvscode as dotvscode_res
import softworks.workspace.workspace_files as workspace_files_pkg


def _effective_project_root() -> Path:
    """SOFTWORKS_PROJECT_ROOT when set, else cwd (resolved)."""
    r = (os.environ.get("SOFTWORKS_PROJECT_ROOT") or "").strip()
    if r:
        return Path(r).expanduser().resolve(strict=False)
    return Path.cwd().resolve()


def _root_from_code_workspace_file(ws_file: Path) -> Path:
    data = json.loads(ws_file.read_text(encoding="utf-8"))
    folders = data.get("folders") or []
    if not folders:
        return ws_file.parent
    raw = folders[0].get("path", ".")
    return (ws_file.parent / raw).resolve()


def _resolve_layout() -> str:
    """Returns the absolute code workspace root path string."""
    sw = (os.environ.get("SOFTWORKS_VSCODE_WORKSPACE") or "").strip()
    if not sw:
        root = _effective_project_root()
        fb = (root / "softworks_workspace").resolve()
        print(
            "Softworks: SOFTWORKS_VSCODE_WORKSPACE is not set; "
            f"using {fb} (effective project root: {root})",
            file=sys.stderr,
            flush=True,
        )
        return str(fb)

    p = Path(sw).expanduser()
    if not p.is_absolute():
        p = Path.cwd() / p
    p = p.resolve(strict=False)
    name = p.name.lower()
    if name.endswith(".code-workspace"):
        if p.is_file():
            root = _root_from_code_workspace_file(p)
            return str(root)
        return str(p.parent)
    return str(p)


class CodeWorkspace:
    def __init__(self) -> None:
        self.user_code_workspace = _resolve_layout()

    def update(self) -> None:
        self._create_workspace()
        self._create_dotvscode_dir()
        self._create_readme()

    def _create_workspace(self) -> None:
        code_path = Path(self.user_code_workspace)
        code_path.mkdir(parents=True, exist_ok=True)
        print(f"creating user code workspace at: '{self.user_code_workspace}'")

    def _create_dotvscode_dir(self) -> None:
        dotvscode_dir = f"{self.user_code_workspace}/.vscode"
        dotvscode_path = Path(dotvscode_dir)
        if dotvscode_path.is_dir():
            print(f"\tdirectory already exists at: {dotvscode_dir}")
            return
        dotvscode_path.mkdir(parents=True, exist_ok=True)
        print(f"\tcreated {dotvscode_dir}")
        with path(dotvscode_res, "extensions.json") as extensions_json_path:
            dst = f"{dotvscode_dir}/extensions.json"
            if not Path(dst).exists():
                copyfile(src=extensions_json_path, dst=dst)
                print(f"\t\tcreated {dst}")
            else:
                print(f"\t\tfile already exists at: {dst}")

        with path(dotvscode_res, "settings.json") as settings_json_path:
            dst = f"{dotvscode_dir}/settings.json"
            if not Path(dst).exists():
                copyfile(src=settings_json_path, dst=dst)
                print(f"\tcreated {dst}")
            else:
                print(f"file already exists at: {dst}")

    def _create_readme(self) -> None:
        with path(workspace_files_pkg, "README.md") as readme_path:
            dst = f"{self.user_code_workspace}/README.md"
            if not Path(dst).exists():
                copyfile(src=readme_path, dst=dst)
                print(f"\tcreated {dst}")
            else:
                print(f"\tfile already exists at: {dst}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--print-root":
        cw = CodeWorkspace()
        sys.stdout.write(str(cw.user_code_workspace))
        sys.exit(0)
    CodeWorkspace().update()
