from mcp.server.fastmcp import FastMCP
from typing import Optional, ClassVar
from dotenv import load_dotenv
import logging
import threading
import os

load_dotenv(
    override=True
)
class MedixMCP:

    MEDIX_SERVER_HOST: str = os.getenv("MEDIX_SERVER_HOST")
    MEDIX_SERVER_PORT: str = os.getenv("MEDIX_SERVER_PORT")

    config = {
        "host": MEDIX_SERVER_HOST,
        "port": int(MEDIX_SERVER_PORT),
        "stateless_http": True,
        "streamable_http_path": "/mcp",
    }

    _server: ClassVar[Optional[FastMCP]] = None
    _lock: ClassVar[threading.Lock] = threading.Lock()

    @classmethod
    def get(cls) -> FastMCP:
        if cls._server is not None:
            return cls._server
        with cls._lock:
            if cls._server is None:
                try:
                    cls._server = FastMCP(
                        name="medix",
                        **cls.config
                    )
                except Exception as e:
                    logging.error(f"Failed to initialise Medix server.\n{e}")
        assert cls._server is not None
        return cls._server
