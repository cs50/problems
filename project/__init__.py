import re
import check50

@check50.check()
def exists():
    """README.md exists"""
    check50.exists("README.md")

@check50.check(exists)
def final():
    """final project details"""
    text = open("README.md").read().lower()
    if len(text) < 2500:
        raise check50.Failure(f"Description is not long enough.")
       
    urls = re.findall('https?:\/\/[\w/\-?=%.]+\.[\w/\-?=%.]+', text)
    if not urls:
        raise check50.Failure(f"Video URL is missing.")
        
