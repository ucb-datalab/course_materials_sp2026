"""Modern tools to style Jupyter notebooks for presentations.

Usage:
    from talktools import style, website, youtube, callout, columns

    # Style is automatically applied on import
    # Or call configure() to customize:
    configure(theme="light", font_size="120%")
"""

from IPython.display import HTML, display, YouTubeVideo, IFrame
from typing import Optional, Literal

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------

_config = {
    "theme": "light",
    "font_size": "120%",
    "primary_color": "#498AF3",
    "secondary_color": "#386BBC",
}


def configure(
    theme: Literal["light", "dark", "auto"] = "light",
    font_size: str = "120%",
    primary_color: str = "#498AF3",
    secondary_color: str = "#386BBC",
) -> None:
    """Configure presentation style.

    Args:
        theme: Color scheme - "light", "dark", or "auto" (follows system)
        font_size: Base font size (e.g., "120%", "18px")
        primary_color: Primary accent color for headers
        secondary_color: Secondary accent color for subtitles
    """
    _config.update({
        "theme": theme,
        "font_size": font_size,
        "primary_color": primary_color,
        "secondary_color": secondary_color,
    })
    _apply_style()


# -----------------------------------------------------------------------------
# URL Helpers
# -----------------------------------------------------------------------------

def _ensure_https(url: str) -> str:
    """Ensure URL has a protocol, preferring HTTPS."""
    if url.startswith(("http://", "https://")):
        return url
    return f"https://{url}"


def link(url: str, text: Optional[str] = None) -> HTML:
    """Create a styled hyperlink that opens in a new tab.

    Args:
        url: The URL to link to
        text: Display text (defaults to URL if not provided)
    """
    text = text or url
    url = _ensure_https(url)
    return HTML(f'<a href="{url}" target="_blank" class="tt-link">{text}</a>')


def website(
    url: str,
    title: Optional[str] = None,
    width: int = 800,
    height: int = 500
) -> HTML:
    """Embed a website in an iframe.

    Args:
        url: Website URL to embed
        title: Optional title shown above the iframe
        width: Iframe width in pixels
        height: Iframe height in pixels
    """
    url = _ensure_https(url)
    title_html = f'<div class="tt-embed-title"><a href="{url}" target="_blank">{title}</a></div>' if title else ""
    return HTML(f'''
        <div class="tt-embed">
            {title_html}
            <iframe src="{url}" width="{width}" height="{height}"
                    frameborder="0" allowfullscreen></iframe>
        </div>
    ''')


def youtube(video_id: str, width: int = 800, height: int = 450) -> HTML:
    """Embed a YouTube video.

    Args:
        video_id: YouTube video ID (the part after v= in the URL)
        width: Video width in pixels
        height: Video height in pixels
    """
    return HTML(f'''
        <div class="tt-embed tt-video">
            <iframe width="{width}" height="{height}"
                    src="https://www.youtube.com/embed/{video_id}"
                    frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen>
            </iframe>
        </div>
    ''')


# -----------------------------------------------------------------------------
# Layout Helpers
# -----------------------------------------------------------------------------

def columns(*contents: str, widths: Optional[list[str]] = None) -> HTML:
    """Display content in side-by-side columns.

    Args:
        *contents: HTML content for each column
        widths: Optional list of CSS widths (e.g., ["60%", "40%"])

    Example:
        columns("<img src='plot1.png'>", "<img src='plot2.png'>")
        columns("Left content", "Right content", widths=["70%", "30%"])
    """
    if widths is None:
        widths = [f"{100 // len(contents)}%" for _ in contents]

    cols_html = "".join(
        f'<div class="tt-col" style="width: {w};">{c}</div>'
        for c, w in zip(contents, widths)
    )
    return HTML(f'<div class="tt-columns">{cols_html}</div>')


def callout(
    content: str,
    kind: Literal["info", "warning", "tip", "note"] = "info",
    title: Optional[str] = None
) -> HTML:
    """Display a styled callout box.

    Args:
        content: The callout content (can include HTML)
        kind: Type of callout - "info", "warning", "tip", or "note"
        title: Optional title for the callout
    """
    icons = {"info": "💡", "warning": "⚠️", "tip": "✨", "note": "📝"}
    titles = {"info": "Info", "warning": "Warning", "tip": "Tip", "note": "Note"}

    icon = icons.get(kind, "")
    title = title or titles.get(kind, "")

    return HTML(f'''
        <div class="tt-callout tt-callout-{kind}">
            <div class="tt-callout-title">{icon} {title}</div>
            <div class="tt-callout-content">{content}</div>
        </div>
    ''')


def center(content: str) -> HTML:
    """Center content horizontally."""
    return HTML(f'<div class="tt-center">{content}</div>')


def image(
    src: str,
    alt: str = "",
    width: Optional[str] = None,
    caption: Optional[str] = None
) -> HTML:
    """Display an image with optional caption.

    Args:
        src: Image source URL or path
        alt: Alt text for accessibility
        width: Optional CSS width (e.g., "50%", "400px")
        caption: Optional caption below image
    """
    style = f'width: {width};' if width else ''
    caption_html = f'<figcaption class="tt-caption">{caption}</figcaption>' if caption else ''

    return HTML(f'''
        <figure class="tt-figure">
            <img src="{src}" alt="{alt}" style="{style}">
            {caption_html}
        </figure>
    ''')


# -----------------------------------------------------------------------------
# Style Definitions
# -----------------------------------------------------------------------------

def _get_style_css() -> str:
    """Generate the CSS based on current configuration."""

    primary = _config["primary_color"]
    secondary = _config["secondary_color"]
    font_size = _config["font_size"]
    theme = _config["theme"]

    # Theme-specific colors
    if theme == "dark":
        bg_color = "#1a1a2e"
        text_color = "#eaeaea"
        code_bg = "#2d2d44"
        callout_bg = "#2d2d44"
    else:
        bg_color = "#ffffff"
        text_color = "#333333"
        code_bg = "#f5f5f5"
        callout_bg = "#f8f9fa"

    theme_query = "@media (prefers-color-scheme: dark)" if theme == "auto" else ""

    return f'''
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Fira+Code&display=swap');

    /* CSS Custom Properties */
    :root {{
        --tt-primary: {primary};
        --tt-secondary: {secondary};
        --tt-font-size: {font_size};
        --tt-bg: {bg_color};
        --tt-text: {text_color};
        --tt-code-bg: {code_bg};
        --tt-callout-bg: {callout_bg};
        --tt-font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        --tt-font-mono: 'Fira Code', 'SF Mono', Consolas, monospace;
        --tt-radius: 8px;
        --tt-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }}

    /* Base styles - works in both Jupyter Notebook and JupyterLab */
    .jp-RenderedHTMLCommon,
    .rendered_html {{
        font-family: var(--tt-font-sans);
        font-size: var(--tt-font-size);
        line-height: 1.6;
        color: var(--tt-text);
    }}

    /* Headers */
    .jp-RenderedHTMLCommon h1,
    .rendered_html h1 {{
        color: var(--tt-primary);
        font-weight: 700;
        font-size: 2.2em;
        line-height: 1.2;
        margin: 0.5em 0;
        text-align: center;
        border-bottom: 3px solid var(--tt-primary);
        padding-bottom: 0.3em;
    }}

    .jp-RenderedHTMLCommon h2,
    .rendered_html h2 {{
        color: var(--tt-secondary);
        font-weight: 600;
        font-size: 1.6em;
        margin: 0.8em 0 0.4em;
    }}

    .jp-RenderedHTMLCommon h3,
    .rendered_html h3 {{
        color: var(--tt-secondary);
        font-weight: 600;
        font-size: 1.3em;
        margin: 0.8em 0 0.4em;
    }}

    /* Code */
    .jp-RenderedHTMLCommon code,
    .rendered_html code {{
        font-family: var(--tt-font-mono);
        background: var(--tt-code-bg);
        padding: 0.2em 0.4em;
        border-radius: 4px;
        font-size: 0.9em;
    }}

    .jp-RenderedHTMLCommon pre,
    .rendered_html pre {{
        background: var(--tt-code-bg);
        padding: 1em;
        border-radius: var(--tt-radius);
        overflow-x: auto;
    }}

    /* Custom classes */
    .talk_title {{
        color: var(--tt-primary);
        font-size: 2.5em;
        font-weight: 700;
        line-height: 1.2;
        text-align: center;
        margin: 0.5em 0;
    }}

    .subtitle {{
        color: var(--tt-secondary);
        font-size: 1.5em;
        font-weight: 500;
        text-align: center;
        margin: 0.5em 0 1em;
    }}

    /* Talktools components */
    .tt-link {{
        color: var(--tt-primary);
        text-decoration: none;
        border-bottom: 2px solid transparent;
        transition: border-color 0.2s;
    }}

    .tt-link:hover {{
        border-bottom-color: var(--tt-primary);
    }}

    .tt-embed {{
        margin: 1em 0;
    }}

    .tt-embed-title {{
        font-weight: 600;
        margin-bottom: 0.5em;
    }}

    .tt-embed iframe {{
        border-radius: var(--tt-radius);
        box-shadow: var(--tt-shadow);
    }}

    .tt-video {{
        text-align: center;
    }}

    .tt-columns {{
        display: flex;
        gap: 1.5em;
        align-items: flex-start;
        margin: 1em 0;
    }}

    .tt-col {{
        flex: 1;
    }}

    .tt-center {{
        text-align: center;
    }}

    .tt-figure {{
        text-align: center;
        margin: 1em 0;
    }}

    .tt-figure img {{
        max-width: 100%;
        border-radius: var(--tt-radius);
        box-shadow: var(--tt-shadow);
    }}

    .tt-caption {{
        font-size: 0.9em;
        color: var(--tt-secondary);
        margin-top: 0.5em;
        font-style: italic;
    }}

    /* Callouts */
    .tt-callout {{
        background: var(--tt-callout-bg);
        border-left: 4px solid var(--tt-primary);
        border-radius: var(--tt-radius);
        padding: 1em 1.5em;
        margin: 1em 0;
    }}

    .tt-callout-title {{
        font-weight: 600;
        margin-bottom: 0.5em;
    }}

    .tt-callout-info {{ border-left-color: #3498db; }}
    .tt-callout-warning {{ border-left-color: #f39c12; }}
    .tt-callout-tip {{ border-left-color: #27ae60; }}
    .tt-callout-note {{ border-left-color: #9b59b6; }}

    /* Tables */
    .jp-RenderedHTMLCommon table,
    .rendered_html table {{
        border-collapse: collapse;
        margin: 1em 0;
        width: 100%;
    }}

    .jp-RenderedHTMLCommon th,
    .rendered_html th {{
        background: var(--tt-primary);
        color: white;
        padding: 0.75em 1em;
        text-align: left;
    }}

    .jp-RenderedHTMLCommon td,
    .rendered_html td {{
        padding: 0.75em 1em;
        border-bottom: 1px solid #ddd;
    }}

    .jp-RenderedHTMLCommon tr:hover,
    .rendered_html tr:hover {{
        background: var(--tt-callout-bg);
    }}
    </style>
    '''


def _apply_style() -> None:
    """Apply the current style configuration."""
    display(HTML(_get_style_css()))


# -----------------------------------------------------------------------------
# Legacy compatibility
# -----------------------------------------------------------------------------

def prefix(url: str) -> str:
    """Legacy function - use _ensure_https instead."""
    return _ensure_https(url)


def simple_link(url: str, name: Optional[str] = None) -> str:
    """Legacy function - returns raw HTML string for a link."""
    name = name or url
    url = _ensure_https(url)
    return f'<a href="{url}" target="_blank">{name}</a>'


def html_link(url: str, name: Optional[str] = None) -> HTML:
    """Legacy function - use link() instead."""
    return link(url, name)


def nbviewer(url: str, name: Optional[str] = None, width: int = 800, height: int = 450) -> HTML:
    """Embed a notebook from nbviewer (legacy function)."""
    return website(f"nbviewer.jupyter.org/url/{url}", name, width, height)


# For backwards compatibility
style = None  # Will be set on import


# -----------------------------------------------------------------------------
# Note: CSS styling is now auto-loaded via ~/.jupyter/custom/custom.css
# Call configure() to dynamically change theme, colors, or font size.
# -----------------------------------------------------------------------------
