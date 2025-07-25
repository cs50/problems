import check50
import re


# Reuse quality check functions from curriculum
KEYBOARD_PATTERNS = [
    'qwert', 'asdf', 'zxcv', 'poiuy', 'lkjh', 'mnbv',
    'qazw', 'wsxe', 'edcr', 'rfvt', 'tgby', 'yhnu',
    'ujmi', 'iklo', 'olp;', 'plok', 'okij', 'jiuh',
    'uiop', 'iopa', 'opas', 'pasd', 'sdfg', 'dfgh',
    'fghj', 'ghjk', 'hjkl', 'jkl;', 'xcvb', 'cvbn',
    'vbnm', 'bnm,', 'nm,.', 'wasd', 'awsd'
]

VOWELS = set('aeiouAEIOU')


def check_for_keyboard_mashing(words):
    """Check if text contains keyboard mashing patterns."""
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
    
    return mashing_count > word_count * 0.4


def check_for_vowelless_words(words):
    """Check if text contains too many words without vowels."""
    word_count = len(words)
    nonsense_words = 0
    
    for word in words:
        if len(word) < 5:
            continue
        if not any(char in VOWELS for char in word):
            nonsense_words += 1
    
    return nonsense_words > word_count * 0.3


def check_language_detection(content):
    """Use langdetect to check if text is meaningful."""
    try:
        from langdetect import detect, LangDetectException
        try:
            detect(content)
            return False
        except LangDetectException:
            return True
    except ImportError:
        return False


def validate_essay_response(content, question_num, min_words=None, max_words=None):
    """Validate an essay response for a given question."""
    # Check if TODO is still present
    if "TODO" in content:
        raise check50.Failure(
            f"Question {question_num} still contains TODO. "
            "Please replace TODO with your response"
        )
    
    # Check if response is empty/blank
    if not content:
        if min_words and min_words == 1:
            raise check50.Failure(
                f"Question {question_num} is blank. "
                "Please provide at least one word"
            )
        elif max_words and not min_words:
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
        if min_words == 1:
            raise check50.Failure(
                f"Question {question_num} is blank. "
                "Please provide at least one word"
            )
        else:
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
    
    # Skip quality checks for short answers (less than 10 words)
    if word_count < 10:
        return
    
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
    """pedagogy.md exists"""
    check50.exists("pedagogy.md")


@check50.check(exists)
def question_0_answered():
    """exactly one framework selected in Question 0"""
    # Read the pedagogy.md file
    with open("pedagogy.md", "r") as f:
        content = f.read()

    # Extract Question 0 section - flexible pattern
    question_0_match = re.search(r'### 0\..*?choice\.\s*(.*?)(?=### 1\.)', content, re.DOTALL)

    if not question_0_match:
        raise check50.Failure("Could not find Question 0 in pedagogy.md")

    question_0_content = question_0_match.group(1)

    # Count checked boxes (handling variations like [X], [x], [ X ], etc.)
    checked_boxes = re.findall(r'\[\s*[Xx]\s*\]', question_0_content)

    if len(checked_boxes) == 0:
        raise check50.Failure(
            "No framework selected in Question 0. "
            "Please mark exactly one framework with [X]"
        )
    elif len(checked_boxes) > 1:
        raise check50.Failure(
            f"{len(checked_boxes)} frameworks selected in Question 0. "
            "Please select only one framework"
        )
    
    # Store whether "Other" is selected for Question 1 validation
    global other_selected
    other_selected = bool(re.search(r'\[\s*[Xx]\s*\]\s*Other', question_0_content))


@check50.check(exists)
def question_1_answered():
    """Question 1 answered appropriately based on Question 0 selection"""
    # Read the pedagogy.md file
    with open("pedagogy.md", "r") as f:
        content = f.read()

    # Check if "Other" was selected in Question 0
    question_0_match = re.search(r'### 0\..*?choice\.\s*(.*?)(?=### 1\.)', content, re.DOTALL)
    if question_0_match:
        question_0_content = question_0_match.group(1)
        other_selected = bool(re.search(r'\[\s*[Xx]\s*\]\s*Other', question_0_content))
    else:
        raise check50.Failure("Could not find Question 0 to check 'Other' selection")

    # Extract Question 1 section - flexible pattern
    question_1_match = re.search(r'### 1\..*?marks\)\.\s*(.*?)(?=### 2\.)', content, re.DOTALL)

    if not question_1_match:
        raise check50.Failure("Could not find Question 1 in pedagogy.md")

    question_1_content = question_1_match.group(1).strip()

    # Check if TODO is still present
    if "TODO" in question_1_content:
        raise check50.Failure(
            "Question 1 still contains TODO. "
            "Please replace TODO with your response"
        )
    
    # Check based on whether "Other" was selected
    if other_selected:
        # "Other" was selected, so Question 1 needs a real answer
        if not question_1_content:
            raise check50.Failure(
                "Question 1 is blank. Since you selected 'Other' in Question 0, "
                "please specify the educational standard framework you will use"
            )
        elif question_1_content.lower().strip() in ["not applicable", "n/a", "na"]:
            raise check50.Failure(
                "Question 1 should specify a framework name since you selected 'Other' in Question 0"
            )
    else:
        # "Other" was NOT selected, so Question 1 should be "not applicable"
        if not question_1_content:
            raise check50.Failure(
                "Question 1 is blank. Since you did not select 'Other' in Question 0, "
                "please write 'not applicable'"
            )
        elif question_1_content.lower().strip() not in ["not applicable", "n/a", "na"]:
            raise check50.Failure(
                "Question 1 should be 'not applicable' since you did not select 'Other' in Question 0"
            )


@check50.check(exists)
def question_2_answered():
    """Question 2 answered with at least 10 words"""
    # Read the pedagogy.md file
    with open("pedagogy.md", "r") as f:
        content = f.read()

    # Extract Question 2 section - flexible pattern
    question_2_match = re.search(r'### 2\..*?standard\.\s*(.*?)(?=### 3\.)', content, re.DOTALL)

    if not question_2_match:
        raise check50.Failure("Could not find Question 2 in pedagogy.md")

    question_2_content = question_2_match.group(1).strip()
    
    # Validate with minimum 10 words
    validate_essay_response(question_2_content, 2, min_words=10)


@check50.check(exists)
def question_3_answered():
    """Question 3 answered with at least 10 words"""
    # Read the pedagogy.md file
    with open("pedagogy.md", "r") as f:
        content = f.read()

    # Extract Question 3 section - flexible pattern
    question_3_match = re.search(r'### 3\..*?lesson\?\s*(.*?)(?=### 4\.)', content, re.DOTALL)

    if not question_3_match:
        raise check50.Failure("Could not find Question 3 in pedagogy.md")

    question_3_content = question_3_match.group(1).strip()
    
    # Validate with minimum 10 words
    validate_essay_response(question_3_content, 3, min_words=10)


@check50.check(exists)
def question_4_answered():
    """Question 4 answered with at least one word"""
    # Read the pedagogy.md file
    with open("pedagogy.md", "r") as f:
        content = f.read()

    # Extract Question 4 section - flexible pattern
    question_4_match = re.search(r'### 4\..*?objective\?\s*(.*?)(?=##)', content, re.DOTALL)

    if not question_4_match:
        raise check50.Failure("Could not find Question 4 in pedagogy.md")

    question_4_content = question_4_match.group(1).strip()
    
    # Validate with minimum 1 word
    validate_essay_response(question_4_content, 4, min_words=1)


@check50.check(exists)
def question_5_answered():
    """at least one teaching value selected in Question 5 (INTO)"""
    # Read the pedagogy.md file
    with open("pedagogy.md", "r") as f:
        content = f.read()

    # Extract Question 5 section - flexible pattern
    question_5_match = re.search(r'### 5\..*?one\.\s*(.*?)(?=### 6\.)', content, re.DOTALL)

    if not question_5_match:
        raise check50.Failure("Could not find Question 5 in pedagogy.md")

    question_5_content = question_5_match.group(1)

    # Count checked boxes (handling variations like [X], [x], [ X ], etc.)
    checked_boxes = re.findall(r'\[\s*[Xx]\s*\]', question_5_content)

    if len(checked_boxes) == 0:
        raise check50.Failure(
            "No teaching values selected in Question 5. "
            "Please mark at least one teaching value with [X]"
        )


@check50.check(exists)
def question_6_answered():
    """Question 6 answered with at least 30 words"""
    # Read the pedagogy.md file
    with open("pedagogy.md", "r") as f:
        content = f.read()

    # Extract Question 6 section - flexible pattern
    question_6_match = re.search(r'### 6\..*?above\.\s*(.*?)(?=##)', content, re.DOTALL)

    if not question_6_match:
        raise check50.Failure("Could not find Question 6 in pedagogy.md")

    question_6_content = question_6_match.group(1).strip()
    
    # Validate with minimum 30 words
    validate_essay_response(question_6_content, 6, min_words=30)


@check50.check(exists)
def question_7_answered():
    """at least one teaching value selected in Question 7 (THROUGH)"""
    # Read the pedagogy.md file
    with open("pedagogy.md", "r") as f:
        content = f.read()

    # Extract Question 7 section - flexible pattern
    question_7_match = re.search(r'### 7\..*?one\.\s*(.*?)(?=### 8\.)', content, re.DOTALL)

    if not question_7_match:
        raise check50.Failure("Could not find Question 7 in pedagogy.md")

    question_7_content = question_7_match.group(1)

    # Count checked boxes (handling variations like [X], [x], [ X ], etc.)
    checked_boxes = re.findall(r'\[\s*[Xx]\s*\]', question_7_content)

    if len(checked_boxes) == 0:
        raise check50.Failure(
            "No teaching values selected in Question 7. "
            "Please mark at least one teaching value with [X]"
        )


@check50.check(exists)
def question_8_answered():
    """Question 8 answered with at least 30 words"""
    # Read the pedagogy.md file
    with open("pedagogy.md", "r") as f:
        content = f.read()

    # Extract Question 8 section - flexible pattern
    question_8_match = re.search(r'### 8\..*?steps\.\s*(.*?)(?=### 9\.)', content, re.DOTALL)

    if not question_8_match:
        raise check50.Failure("Could not find Question 8 in pedagogy.md")

    question_8_content = question_8_match.group(1).strip()
    
    # Validate with minimum 30 words
    validate_essay_response(question_8_content, 8, min_words=30)


@check50.check(exists)
def question_9_answered():
    """Question 9 answered with at least 30 words"""
    # Read the pedagogy.md file
    with open("pedagogy.md", "r") as f:
        content = f.read()

    # Extract Question 9 section - flexible pattern
    question_9_match = re.search(r'### 9\..*?steps\.\s*(.*?)(?=##)', content, re.DOTALL)

    if not question_9_match:
        raise check50.Failure("Could not find Question 9 in pedagogy.md")

    question_9_content = question_9_match.group(1).strip()
    
    # Validate with minimum 30 words
    validate_essay_response(question_9_content, 9, min_words=30)


@check50.check(exists)
def question_10_answered():
    """at least one teaching value selected in Question 10 (BEYOND)"""
    # Read the pedagogy.md file
    with open("pedagogy.md", "r") as f:
        content = f.read()

    # Extract Question 10 section - flexible pattern
    question_10_match = re.search(r'### 10\..*?one\.\s*(.*?)(?=### 11\.)', content, re.DOTALL)

    if not question_10_match:
        raise check50.Failure("Could not find Question 10 in pedagogy.md")

    question_10_content = question_10_match.group(1)

    # Count checked boxes (handling variations like [X], [x], [ X ], etc.)
    checked_boxes = re.findall(r'\[\s*[Xx]\s*\]', question_10_content)

    if len(checked_boxes) == 0:
        raise check50.Failure(
            "No teaching values selected in Question 10. "
            "Please mark at least one teaching value with [X]"
        )


@check50.check(exists)
def question_11_answered():
    """Question 11 answered with at least 30 words"""
    # Read the pedagogy.md file
    with open("pedagogy.md", "r") as f:
        content = f.read()

    # Extract Question 11 section - flexible pattern
    question_11_match = re.search(r'### 11\..*?steps\.\s*(.*?)(?=### 12\.)', content, re.DOTALL)

    if not question_11_match:
        raise check50.Failure("Could not find Question 11 in pedagogy.md")

    question_11_content = question_11_match.group(1).strip()
    
    # Validate with minimum 30 words
    validate_essay_response(question_11_content, 11, min_words=30)


@check50.check(exists)
def question_12_answered():
    """Question 12 answered with at least 30 words"""
    # Read the pedagogy.md file
    with open("pedagogy.md", "r") as f:
        content = f.read()

    # Extract Question 12 section - flexible pattern
    question_12_match = re.search(r'### 12\..*?steps\.\s*(.*?)(?=### 13\.)', content, re.DOTALL)

    if not question_12_match:
        raise check50.Failure("Could not find Question 12 in pedagogy.md")

    question_12_content = question_12_match.group(1).strip()
    
    # Validate with minimum 30 words
    validate_essay_response(question_12_content, 12, min_words=30)


@check50.check(exists)
def question_13_answered():
    """Question 13 answered with at least 30 words"""
    # Read the pedagogy.md file
    with open("pedagogy.md", "r") as f:
        content = f.read()

    # Extract Question 13 section - flexible pattern
    question_13_match = re.search(r'### 13\..*?steps\.\s*(.*?)(?=##)', content, re.DOTALL)

    if not question_13_match:
        raise check50.Failure("Could not find Question 13 in pedagogy.md")

    question_13_content = question_13_match.group(1).strip()
    
    # Validate with minimum 30 words
    validate_essay_response(question_13_content, 13, min_words=30)


@check50.check(exists)
def question_14_answered():
    """Question 14 answered with at least 30 words"""
    # Read the pedagogy.md file
    with open("pedagogy.md", "r") as f:
        content = f.read()

    # Extract Question 14 section - flexible pattern (to end of file)
    question_14_match = re.search(r'### 14\..*?reflection\?\s*(.*?)$', content, re.DOTALL)

    if not question_14_match:
        raise check50.Failure("Could not find Question 14 in pedagogy.md")

    question_14_content = question_14_match.group(1).strip()
    
    # Validate with minimum 30 words
    validate_essay_response(question_14_content, 14, min_words=30)