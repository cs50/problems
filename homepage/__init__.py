import check50

import os
import re


def html_pages():
    return sorted(f for f in os.listdir(".") if f.endswith(".html"))


@check50.check()
def required_files():
    """required files exist"""
    check50.exists("index.html")
    check50.exists("styles.css")
    check50.exists("specification.txt")


@check50.check(required_files)
def four_pages():
    """contains at least 4 HTML pages including index.html"""
    pages = html_pages()
    if len(pages) < 4:
        raise check50.Failure("expected at least 4 HTML pages")


@check50.check(four_pages)
def navigation():
    """each page links to at least one other page"""
    pages = html_pages()
    href_re = re.compile(r"""href\s*=\s*["']([^"']+)["']""", re.I)

    for p in pages:
        with open(p) as f:
            html = f.read()
        for m in href_re.finditer(html):
            href = m.group(1).split("#", 1)[0].split("?", 1)[0]
            if href in pages and href != p:
                break
        else:
            raise check50.Failure("one or more pages do not link to another page")


@check50.check(four_pages)
def ten_distinct_tags():
    """contains at least 10 distinct HTML tags besides html/head/body/title"""
    tag_re = re.compile(r"<\s*([a-zA-Z][\w:-]*)\b")
    used = set()

    for p in html_pages():
        with open(p) as f:
            page = f.read()
        for m in tag_re.finditer(page):
            used.add(m.group(1).lower())
    excluded_tags = {"html", "head", "body", "title"}
    used -= excluded_tags
    if len(used) < 10:
        raise check50.Failure("fewer than 10 distinct HTML tags were found")


@check50.check(four_pages)
def bootstrap():
    """Bootstrap is used"""
    for p in html_pages():
        with open(p) as f:
            if "bootstrap" in f.read().lower():
                return

    raise check50.Failure(
        "Bootstrap not detected",
        help="Use Bootstrap on at least one page of your site."
    )


@check50.check(four_pages)
def stylesheet():
    """styles.css is linked"""
    for p in html_pages():
        with open(p) as f:
            if "styles.css" in f.read().lower():
                return

    raise check50.Failure(
        "styles.css not linked",
        help="Link your own stylesheet (styles.css) from at least one page."
    )


@check50.check(four_pages)
def css_rules():
    """styles.css uses at least 5 selectors and 5 distinct properties"""
    with open("styles.css") as f:
        css = f.read()

    rule_count = css.count("{")

    # Loose match: may also count pseudo-selectors or URL schemes, but sufficient for typical student CSS
    props_count = len(set(re.findall(r"([a-zA-Z-]+)\s*:", css)))

    if rule_count < 5:
        raise check50.Failure("styles.css does not appear to use at least 5 selectors")

    if props_count < 5:
        raise check50.Failure("styles.css does not appear to use at least 5 CSS properties")


@check50.check(four_pages)
def javascript():
    """JavaScript is used"""
    script_re = re.compile(r"<script\b([^>]*)>", re.I)
    src_re = re.compile(r"""src\s*=\s*["']([^"']*)["']""", re.I)

    for p in html_pages():
        with open(p) as f:
            html = f.read()
        for m in script_re.finditer(html):
            attrs = m.group(1)
            src_match = src_re.search(attrs)
            if not src_match or "://" not in src_match.group(1):
                return

    raise check50.Failure(
        "no custom JavaScript detected",
        help="Have you included some JavaScript via an inline <script> tag or a local .js file?"
    )


@check50.check(required_files)
def specification():
    """specification.txt contains required information"""
    with open("specification.txt") as f:
        spec = f.read().lower()

    if "javascript" not in spec or "bootstrap" not in spec:
        raise check50.Failure(
            "specification.txt does not describe JavaScript and/or Bootstrap",
            help="Have you included a one-sentence description of how you used JavaScript and Bootstrap?"
        )
    if len(spec.split()) < 25:
        raise check50.Failure(
            "specification.txt seems incomplete",
            help="Have you listed the 10 HTML tags and 5 CSS properties you’ve used?"
        )
