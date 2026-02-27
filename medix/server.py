from mcp.server.fastmcp import FastMCP
from typing import Any, ClassVar
import threading

class MedixMCP:

    _server: ClassVar["FastMCP | Any"] = None
    _lock: ClassVar[threading.Lock] = threading.Lock()

    @classmethod
    def get(cls) -> FastMCP:
        if cls._server is None:
            with cls._lock:
                cls._server = FastMCP("medix")
        return cls._server

mcp = MedixMCP.get()
