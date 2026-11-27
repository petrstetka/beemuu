"""Launch the packaged app on the GitHub Mac, away from the source checkout."""
import pathlib
import subprocess
import sys
import tempfile
import time

app = pathlib.Path(sys.argv[1]).resolve()
log_path = pathlib.Path(sys.argv[2]).resolve()
with tempfile.TemporaryDirectory(prefix="beemuu-startup-") as cwd:
    with log_path.open("w") as log:
        process = subprocess.Popen(
            [str(app / "Contents/MacOS/beeemuu")],
            cwd=cwd,
            stdout=log,
            stderr=subprocess.STDOUT,
        )
        try:
            time.sleep(10)
            if process.poll() is not None:
                raise RuntimeError(f"App exited during startup: {process.returncode}")
        finally:
            if process.poll() is None:
                process.terminate()
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=5)
output = log_path.read_text()
print(output)
assert "community data:" in output, "Startup did not reach community-data loading"
assert "Contents/MacOS/../Resources/community" in output, "Bundled data was not discovered"
print("Packaged app stayed running for 10 seconds outside the source checkout.")
