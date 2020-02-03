"""Start the SenseAPI FastAPI ASGI server."""

import uvicorn
from pathlib import Path
import sys


senseapi_package_path = Path(__file__).parent.expanduser().resolve()

# Add package parent directory to the system PATH
sys.path.insert(0, str(senseapi_package_path.parent))

# Start the Uvicorn ASGI server in development mode
# ToDo: Configure ASGI for production use
uvicorn.run(
    "senseapi.api.main:app",
    host="0.0.0.0",
    port=8000,
    reload=True,
    reload_dirs=[str(senseapi_package_path)],
)
