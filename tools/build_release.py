#!/usr/bin/env python3
# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
# Required Notice: Copyright 2026 Jeongin Choe (최정인)
# License: https://polyformproject.org/licenses/noncommercial/1.0.0
"""Build equivalent .zip and .skill distributions from an explicit allowlist."""
from pathlib import Path
import hashlib
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = "weekly-childcare"
RUNTIME_FILES = ["SKILL.md", "LICENSE.md"]
RUNTIME_DIRS = ["references", "templates", "examples", "scripts", "agents", "assets", "LICENSES"]


def main():
    paths = [ROOT / f for f in RUNTIME_FILES]
    for folder in RUNTIME_DIRS:
        paths.extend(p for p in (ROOT / folder).rglob("*")
                     if p.is_file() and "__pycache__" not in p.parts and p.suffix not in (".pyc", ".pyo"))
    paths = sorted(set(paths))
    if any(p.is_symlink() for p in paths):
        raise ValueError("Release files must not be symlinks")
    out = ROOT / "dist"
    out.mkdir(exist_ok=True)
    zip_path = out / f"{NAME}.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in paths:
            relative = path.relative_to(ROOT)
            info = zipfile.ZipInfo(f"{NAME}/{relative.as_posix()}", date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    skill_path = out / f"{NAME}.skill"
    skill_path.write_bytes(zip_path.read_bytes())
    with zipfile.ZipFile(zip_path) as archive:
        if archive.testzip() is not None:
            raise ValueError("ZIP integrity check failed")
        if f"{NAME}/SKILL.md" not in archive.namelist():
            raise ValueError("Missing SKILL.md")
    (out / "SHA256SUMS.txt").write_text("".join(
        f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n" for p in (zip_path, skill_path)
    ), encoding="utf-8")
    print(f"Built {len(paths)} runtime files; equivalent .zip/.skill; {zip_path.stat().st_size} bytes each")


if __name__ == "__main__":
    main()
