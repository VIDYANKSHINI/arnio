"""
arnio._core
Internal module that imports the C++ extension.
"""

import os
import sys

# On Windows, Python 3.8+ does not load DLLs from PATH automatically.
# We scan PATH for directories containing g++.exe or runtime DLLs and add them.
if sys.platform == "win32":
    for path in os.environ.get("PATH", "").split(os.pathsep):
        if path and os.path.isdir(path):
            if (
                os.path.exists(os.path.join(path, "g++.exe"))
                or os.path.exists(os.path.join(path, "libstdc++-6.dll"))
                or os.path.exists(os.path.join(path, "libgcc_s_seh-1.dll"))
            ):
                try:
                    os.add_dll_directory(path)
                except Exception:
                    pass
    # Also support the winlibs package installed via winget
    winlibs_path = r"C:\Users\VIDYANKSHINI\AppData\Local\Microsoft\WinGet\Packages\BrechtSanders.WinLibs.POSIX.UCRT_Microsoft.Winget.Source_8wekyb3d8bbwe\mingw64\bin"
    if os.path.exists(winlibs_path):
        try:
            os.add_dll_directory(winlibs_path)
        except Exception:
            pass

try:
    from ._arnio_cpp import (  # type: ignore[import-not-found]  # noqa: I001
        Column as _Column,  # noqa: F401
        CsvConfig as _CsvConfig,  # noqa: F401
        CsvChunkReader as _CsvChunkReader,  # noqa: F401
        CsvReader as _CsvReader,  # noqa: F401
        CsvWriteConfig as _CsvWriteConfig,  # noqa: F401
        CsvWriter as _CsvWriter,  # noqa: F401
        DType as _DType,  # noqa: F401
        Frame as _Frame,  # noqa: F401
        cast_types as _cast_types,  # noqa: F401
        clip_numeric as _clip_numeric,  # noqa: F401
        safe_divide_columns as _safe_divide_columns,  # noqa: F401
        drop_duplicates as _drop_duplicates,  # noqa: F401
        drop_nulls as _drop_nulls,  # noqa: F401
        fill_nulls as _fill_nulls,  # noqa: F401
        normalize_case as _normalize_case,  # noqa: F401
        rename_columns as _rename_columns,  # noqa: F401
        strip_whitespace as _strip_whitespace,  # noqa: F401
    )
except ImportError as e:
    raise ImportError(
        "arnio C++ extension (_arnio_cpp) not found. "
        "Please install arnio with: pip install ."
    ) from e
