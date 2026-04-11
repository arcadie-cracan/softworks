from typing import Tuple
from pathlib import Path
from importlib.resources import files
import virtue
import softworks


def virtue_data_reg_paths() -> Tuple[Path]:
    return (
        files(softworks) / "data_reg" / "SdmPy.data.reg",
        files(softworks) / "data_reg" / "SdmSkill.data.reg",
        files(softworks) / "data_reg" / "SdmPptx.data.reg",
        files(softworks) / "data_reg" / "SdmXlsx.data.reg",
        files(softworks) / "data_reg" / "SdmPdf.data.reg",
        files(softworks) / "data_reg" / "SdmHtml.data.reg",
        )

@virtue.hookimpl
def virtue_register_skill_package():
    return {
        "python_package_name": "softworks",
        "skill_package_name": "Softworks",
        "cdsinit_paths": (files(softworks) / "softworks.cdsinit.ils"),
        "cdslibmgr_paths": (files(softworks) / "softworks.cdsLibMgr.il"),
        "cds_dev_libraries": {
            "virtue_dev_project": (files(virtue) / "softworks_dev_work"),
        },
        "data_reg_paths": virtue_data_reg_paths(),
    }
