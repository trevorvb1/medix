from medix.server import MedixMCP

def main() -> None:
    mcp = MedixMCP.get()
    mcp.run(
        transport="streamable-http"
    )

if __name__ == "__main__":
    main()
