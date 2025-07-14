import subprocess
from pathlib import Path
from .ProcessingStrategy import Processing_Strategy

class BlackAndWhiteProcessing(Processing_Strategy):
    def process(self, file_path: Path, output_dir: Path):

        cmd = [
            "darktable-cli",
            str(file_path),
            str(output_dir),
            "--core",
            "--disable-opencl"
        ]

        subprocess.run(cmd, check=True)