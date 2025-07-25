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
    """technology.md exists"""
    check50.exists("technology.md")


@check50.check(exists)
def question_0_answered():
    """Question 0 answered with at least one word"""
    # Read the technology.md file
    with open("technology.md", "r") as f:
        content = f.read()

    # Extract Question 0 section - flexible pattern
    question_0_match = re.search(r'## 0\..*?today\?\s*(.*?)(?=## 1\.)', content, re.DOTALL)

    if not question_0_match:
        raise check50.Failure("Could not find Question 0 in technology.md")

    question_0_content = question_0_match.group(1).strip()
    
    # Validate with minimum 1 word requirement
    validate_essay_response(question_0_content, 0, min_words=1)


@check50.check(exists)
def question_1_answered():
    """Question 1 answered with at least 30 words"""
    # Read the technology.md file
    with open("technology.md", "r") as f:
        content = f.read()

    # Extract Question 1 section - flexible pattern
    question_1_match = re.search(r'## 1\..*?detail\.\s*(.*?)(?=## 2\.)', content, re.DOTALL)

    if not question_1_match:
        raise check50.Failure("Could not find Question 1 in technology.md")

    question_1_content = question_1_match.group(1).strip()
    
    # Validate with 30 word minimum
    validate_essay_response(question_1_content, 1, min_words=30)


@check50.check(exists)
def question_2_answered():
    """Question 2 answered with at least 30 words"""
    # Read the technology.md file
    with open("technology.md", "r") as f:
        content = f.read()

    # Extract Question 2 section - flexible pattern (note typo "now" in original)
    question_2_match = re.search(r'## 2\..*?detail\.\s*(.*?)(?=## 3\.)', content, re.DOTALL)

    if not question_2_match:
        raise check50.Failure("Could not find Question 2 in technology.md")

    question_2_content = question_2_match.group(1).strip()
    
    # Validate with 30 word minimum
    validate_essay_response(question_2_content, 2, min_words=30)


@check50.check(exists)
def question_3_answered():
    """Question 3 answered with at least 30 words"""
    # Read the technology.md file
    with open("technology.md", "r") as f:
        content = f.read()

    # Extract Question 3 section - flexible pattern
    question_3_match = re.search(r'## 3\..*?detail\.\s*(.*?)(?=## 4\.)', content, re.DOTALL)

    if not question_3_match:
        raise check50.Failure("Could not find Question 3 in technology.md")

    question_3_content = question_3_match.group(1).strip()
    
    # Validate with 30 word minimum
    validate_essay_response(question_3_content, 3, min_words=30)


@check50.check(exists)
def question_4_answered():
    """Question 4 answered with at least 30 words"""
    # Read the technology.md file
    with open("technology.md", "r") as f:
        content = f.read()

    # Extract Question 4 section - flexible pattern (to end of file)
    question_4_match = re.search(r'## 4\..*?tools\?\s*(.*?)$', content, re.DOTALL)

    if not question_4_match:
        raise check50.Failure("Could not find Question 4 in technology.md")

    question_4_content = question_4_match.group(1).strip()
    
    # Validate with 30 word minimum
    validate_essay_response(question_4_content, 4, min_words=30)