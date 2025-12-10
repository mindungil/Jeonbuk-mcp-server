from pathlib import Path

def load_md_templates() -> tuple[str, str, str, str, str, str]:
    """
    Load Markdown templates for PowerPoint, Excel, Word, HWP, and Markdown generation tools.

    Returns:
        tuple[str, str, str, str, str, str]: A tuple containing the Markdown templates for
        PowerPoint, Excel, Word, HWP, Markdown, and MCP Instructions respectively.
    """

    try:
        # Load Markdown template files
        with open(Path("template", "powerpoint.md"), "r", encoding="utf-8") as f:
            POWERPOINT_TEMPLATE = f.read()

        with open(Path("template", "excel.md"), "r", encoding="utf-8") as f:
            EXCEL_TEMPLATE = f.read()

        with open(Path("template", "word.md"), "r", encoding="utf-8") as f:
            WORD_TEMPLATE = f.read()

        with open(Path("template", "hwp.md"), "r", encoding="utf-8") as f:
            HWP_TEMPLATE = f.read()

        with open(Path("template", "markdown.md"), "r", encoding="utf-8") as f:
            MARKDOWN_TEMPLATE = f.read()

        with open(Path("template", "mcp_instructions.md"), "r", encoding="utf-8") as f:
            MCP_INSTRUCTIONS = f.read()

        return (
            POWERPOINT_TEMPLATE,
            EXCEL_TEMPLATE,
            WORD_TEMPLATE,
            HWP_TEMPLATE,
            MARKDOWN_TEMPLATE,
            MCP_INSTRUCTIONS
        )

    except Exception as e:
        raise RuntimeError(f"Error loading Markdown templates: {e}")

