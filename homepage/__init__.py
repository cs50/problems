import os
import re

import check50


# helper
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
    """pages link to each other"""
    pages = html_pages()
    href_re = re.compile(r"""href\s*=\s*["']([^"']+)["']""", re.I)

    for p in pages:
        html = open(p).read()
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
        page = open(p).read()
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
        if "bootstrap" in open(p).read().lower():
            return

    raise check50.Failure(
        "Bootstrap not detected",
        help="Use Bootstrap on at least one page of your site."
    )


@check50.check(four_pages)
def stylesheet():
    """styles.css is linked"""
    for p in html_pages():
        if "styles.css" in open(p).read().lower():
            return

    raise check50.Failure(
        "styles.css not linked",
        help="Link your own stylesheet (styles.css) from at least one page."
    )


@check50.check(four_pages)
def css_rules():
    """styles.css uses at least 5 selectors and 5 distinct properties"""
    css = open("styles.css").read()

    # Count number of rule blocks
    selector_count = css.count("{")

    # Set of any "name:" occurrences
    props_count = len(set(re.findall(r"([a-zA-Z-]+)\s*:", css)))

    if selector_count < 5:
        raise check50.Failure("styles.css does not appear to use at least 5 selectors")

    if props_count < 5:
        raise check50.Failure("styles.css does not appear to use at least 5 CSS properties")


@check50.check(four_pages)
def javascript():
    """JavaScript is used"""
    for p in html_pages():
        if "<script" in open(p).read().lower():
            return

    raise check50.Failure(
        "no scripts detected",
        help="Have you included some javascript via a script tag?"
    )


@check50.check(required_files)
def specification():
    """specification.txt contains required information"""
    spec = open("specification.txt").read().lower()

    if "javascript" not in spec or "bootstrap" not in spec:
        raise check50.Failure(
            "specification.txt does not describe JavaScript and/or Bootstrap",
            help="Have you included a one-sentence description of how you used JavaScript and Bootstrap?"
        )
    if len(spec.split()) < 25:
        raise check50.Failure(
            "specification.txt seems incomplete ",
            help="Have you listed the 10 HTML tags and 5 CSS properties you’ve used?"
        )
