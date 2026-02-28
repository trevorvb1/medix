from mcp.server.fastmcp import FastMCP
from typing import Optional, ClassVar
import logging
import threading

class MedixMCP:

    _server: ClassVar[Optional[FastMCP]] = None
    _lock: ClassVar[threading.Lock] = threading.Lock()

    @classmethod
    def get(cls) -> FastMCP:
        if cls._server is not None:
            return cls._server
        with cls._lock:
            if cls._server is None:
                try:
                    cls._server = FastMCP("medix")
                except Exception as e:
                    logging.error(f"Failed to initialise Medix server.\n{e}")
        assert cls._server is not None
        return cls._server

mcp = MedixMCP.get()
