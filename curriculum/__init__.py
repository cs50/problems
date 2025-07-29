import check50
import re

# Fine Tuning
KEYBOARD_MASHING_THRESHOLD = 0.2
NO_VOWELS_THRESHOLD = 0.3

# Keyboard patterns commonly used in mashing
KEYBOARD_PATTERNS = [
    'qwert', 'asdf', 'zxcv', 'poiuy', 'lkjh', 'mnbv',
    'qazw', 'wsxe', 'edcr', 'rfvt', 'tgby', 'yhnu',
    'ujmi', 'iklo', 'olp;', 'plok', 'okij', 'jiuh',
    'uiop', 'iopa', 'opas', 'pasd', 'sdfg', 'dfgh',
    'fghj', 'ghjk', 'hjkl', 'jkl;', 'xcvb', 'cvbn',
    'vbnm', 'bnm,', 'nm,.', 'wasd', 'awsd', 'aaa',
    'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh',
    'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'ooo',
    'ppp', 'qqq', 'rrr', 'sss', 'ttt', 'uuu', 'vvv',
    'www', 'xxx', 'yyy', 'zzz'
]

# Vowels for checking nonsense words
VOWELS = set('aeiouAEIOU')


def check_for_keyboard_mashing(words):
    """
    Check if text contains keyboard mashing patterns.
    Returns True if too many words look like keyboard mashing.
    """
    word_count = len(words)
    mashing_count = 0
    
    for word in words:
        word_lower = word.lower()
        # Check for keyboard patterns
        for pattern in KEYBOARD_PATTERNS:
            if pattern in word_lower:
                mashing_count += 1
                break
        # Check for repeated characters (e.g., "aaaa", "ssss")
        for i in range(len(word_lower) - 3):
            if len(set(word_lower[i:i+4])) == 1:
                mashing_count += 1
                break
    
    # If more than 20% of words look like keyboard mashing
    return mashing_count > word_count * KEYBOARD_MASHING_THRESHOLD


def check_for_vowelless_words(words):
    """
    Check if text contains too many words without vowels.
    Returns True if too many long words lack vowels.
    """
    word_count = len(words)
    nonsense_words = 0
    
    for word in words:
        # Skip short words and punctuation
        if len(word) < 5:
            continue
        # Check if word has no vowels
        if not any(char in VOWELS for char in word):
            nonsense_words += 1
    
    # If more than 30% of words look like nonsense words
    return nonsense_words > word_count * NO_VOWELS_THRESHOLD


def check_language_detection(content):
    """
    Use langdetect to check if text is meaningful.
    Returns True if text appears to be gibberish.
    """
    try:
        from langdetect import detect, LangDetectException
        try:
            detect(content)
            return False  # Language detected, text is likely meaningful
        except LangDetectException:
            return True  # No language detected, likely gibberish
    except ImportError:
        # If langdetect is not available, skip this check
        return False


def validate_essay_response(content, question_num, min_words=None, max_words=None):
    """
    Validate an essay response for a given question.
    Performs all standard checks: TODO, blank, word count, and quality.
    
    Args:
        content: The response text
        question_num: Question number for error messages
        min_words: Minimum word count (optional)
        max_words: Maximum word count (optional)
    """
    # Check if TODO is still present
    if "TODO" in content:
        raise check50.Failure(
            f"Question {question_num} still contains TODO. "
            "Please replace TODO with your response"
        )
    
    # Check if response is empty/blank
    if not content:
        if max_words and not min_words:
            raise check50.Failure(
                f"Question {question_num} is blank. "
                f"Please provide a response of {max_words} words or less"
            )
        else:
            raise check50.Failure(
                f"Question {question_num} is blank. "
                f"Please provide a response of at least {min_words} words"
            )
    
    # Count words
    words = content.split()
    word_count = len(words)
    
    # Check minimum word count
    if min_words and word_count < min_words:
        raise check50.Failure(
            f"Question {question_num} has only {word_count} words. "
            f"Please provide at least {min_words} words (you need {min_words - word_count} more)"
        )
    
    # Check maximum word count
    if max_words and word_count > max_words:
        raise check50.Failure(
            f"Question {question_num} has {word_count} words. "
            f"Please limit your response to {max_words} words or less (remove {word_count - max_words} words)"
        )
    
    # Check for keyboard mashing
    if check_for_keyboard_mashing(words):
        raise check50.Failure(
            f"Question {question_num} appears to contain keyboard mashing or nonsense text. "
            "Please provide a thoughtful, meaningful response"
        )
    
    # Check for words without vowels
    if check_for_vowelless_words(words):
        raise check50.Failure(
            f"Question {question_num} contains too many words without vowels. "
            "Please provide a meaningful response using proper words"
        )
    
    # Check language detection
    if check_language_detection(content):
        raise check50.Failure(
            f"Question {question_num} appears to contain gibberish or random characters. "
            "Please provide a meaningful response"
        )


@check50.check()
def exists():
    """curriculum.md exists"""
    check50.exists("curriculum.md")


@check50.check(exists)
def question_0_answered():
    """at least one course selected in Question 0"""
    # Read the curriculum.md file
    with open("curriculum.md", "r") as f:
        content = f.read()

    # Extract Question 0 section (between ## 0. and ## 1.)
    # Using re.DOTALL to match across newlines
    question_0_match = re.search(r'## 0\.(.*?)## 1\.', content, re.DOTALL)

    if not question_0_match:
        raise check50.Failure("Could not find Question 0 in curriculum.md")

    question_0_content = question_0_match.group(1)

    # Count checked boxes (handling variations like [X], [x], [ X ], etc.)
    checked_boxes = re.findall(r'\[\s*[Xx]\s*\]', question_0_content)

    if len(checked_boxes) == 0:
        raise check50.Failure(
            "No courses selected in Question 0. "
            "Please mark at least one course with [X]"
        )


@check50.check(exists)
def question_1_answered():
    """at least one artifact selected in Question 1"""
    # Read the curriculum.md file
    with open("curriculum.md", "r") as f:
        content = f.read()

    # Extract Question 1 section (between ## 1. and ## 2.)
    # Using re.DOTALL to match across newlines
    question_1_match = re.search(r'## 1\.(.*?)## 2\.', content, re.DOTALL)

    if not question_1_match:
        raise check50.Failure("Could not find Question 1 in curriculum.md")

    question_1_content = question_1_match.group(1)

    # Count checked boxes (handling variations like [X], [x], [ X ], etc.)
    checked_boxes = re.findall(r'\[\s*[Xx]\s*\]', question_1_content)

    if len(checked_boxes) == 0:
        raise check50.Failure(
            "No artifacts selected in Question 1. "
            "Please mark at least one computational artifact with [X]"
        )


@check50.check(exists)
def question_2_answered():
    """Question 2 answered (TODO replaced)"""
    # Read the curriculum.md file
    with open("curriculum.md", "r") as f:
        content = f.read()

    # Extract Question 2 section (between ## 2. and ## 3.)
    # More flexible pattern that works with or without paragraph break
    question_2_match = re.search(r'## 2\..*?below\.\s*(.*?)(?=## 3\.)', content, re.DOTALL)

    if not question_2_match:
        raise check50.Failure("Could not find Question 2 in curriculum.md")

    question_2_content = question_2_match.group(1).strip()

    # Check if TODO is still present
    if "TODO" in question_2_content:
        raise check50.Failure(
            "Question 2 still contains TODO. "
            "Please replace TODO with your response "
            "(or write 'none' if not applicable)"
        )
    
    # Check if response is empty/blank
    if not question_2_content:
        raise check50.Failure(
            "Question 2 is blank. "
            "Please provide a response "
            "(or write 'none' if not applicable)"
        )


@check50.check(exists)
def question_3_answered():
    """Question 3 answered with at least 30 words"""
    # Read the curriculum.md file
    with open("curriculum.md", "r") as f:
        content = f.read()

    # Extract Question 3 section - more flexible pattern
    # Matches the question, then captures everything until the next question
    question_3_match = re.search(r'## 3\..*?students\?\s*(.*?)(?=## 4\.)', content, re.DOTALL)

    if not question_3_match:
        raise check50.Failure("Could not find Question 3 in curriculum.md")

    question_3_content = question_3_match.group(1).strip()
    
    # Use the common validation function
    validate_essay_response(question_3_content, 3, min_words=30)


@check50.check(exists)
def question_4_answered():
    """Question 4 answered with at least 30 words"""
    # Read the curriculum.md file
    with open("curriculum.md", "r") as f:
        content = f.read()

    # Extract Question 4 section - more flexible pattern
    question_4_match = re.search(r'## 4\..*?lives\?\s*(.*?)(?=## 5\.)', content, re.DOTALL)

    if not question_4_match:
        raise check50.Failure("Could not find Question 4 in curriculum.md")

    question_4_content = question_4_match.group(1).strip()
    
    # Use the common validation function
    validate_essay_response(question_4_content, 4, min_words=30)


@check50.check(exists)
def question_5_answered():
    """Question 5 answered with at least 50 words"""
    # Read the curriculum.md file
    with open("curriculum.md", "r") as f:
        content = f.read()

    # Extract Question 5 section - more flexible pattern
    question_5_match = re.search(r'## 5\..*?skills\?\s*(.*?)(?=## 6\.)', content, re.DOTALL)

    if not question_5_match:
        raise check50.Failure("Could not find Question 5 in curriculum.md")

    question_5_content = question_5_match.group(1).strip()
    
    # Use the common validation function (note: 50 words for Question 5)
    validate_essay_response(question_5_content, 5, min_words=50)


@check50.check(exists)
def question_6_answered():
    """Question 6 answered with 20 words or less"""
    # Read the curriculum.md file
    with open("curriculum.md", "r") as f:
        content = f.read()

    # Extract Question 6 section - more flexible pattern
    question_6_match = re.search(r'## 6\..*?Y\.\"\s*(.*?)(?=## 7\.)', content, re.DOTALL)

    if not question_6_match:
        raise check50.Failure("Could not find Question 6 in curriculum.md")

    question_6_content = question_6_match.group(1).strip()
    
    # Use the common validation function (note: max 20 words for Question 6)
    validate_essay_response(question_6_content, 6, max_words=20)


@check50.check(exists)
def question_7_answered():
    """Question 7 answered with at least 50 words"""
    # Read the curriculum.md file
    with open("curriculum.md", "r") as f:
        content = f.read()

    # Extract Question 7 section - more flexible pattern
    question_7_match = re.search(r'## 7\..*?skills\?\s*(.*?)(?=## 8\.)', content, re.DOTALL)

    if not question_7_match:
        raise check50.Failure("Could not find Question 7 in curriculum.md")

    question_7_content = question_7_match.group(1).strip()
    
    # Use the common validation function (note: 50 words for Question 7)
    validate_essay_response(question_7_content, 7, min_words=50)


@check50.check(exists)
def question_8_answered():
    """Question 8 answered with 20 words or less"""
    # Read the curriculum.md file
    with open("curriculum.md", "r") as f:
        content = f.read()

    # Extract Question 8 section (from ## 8. to end of file) - more flexible pattern
    question_8_match = re.search(r'## 8\..*?concepts\?\s*(.*?)$', content, re.DOTALL)

    if not question_8_match:
        raise check50.Failure("Could not find Question 8 in curriculum.md")

    question_8_content = question_8_match.group(1).strip()
    
    # Use the common validation function (note: max 20 words for Question 8)
    validate_essay_response(question_8_content, 8, max_words=20)