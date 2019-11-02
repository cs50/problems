import check50

@check50.check()
def exists():
    """readability.py exists."""
    check50.exists("readability.py")

@check50.check(exists)
def single_sentence():
    """handles single sentence with multiple words"""
    check50.run("python3 readability.py").stdin("In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.").stdout("Grade\D+7", "Grade 7\n").exit(0)

@check50.check(exists)
def single_sentence_other_punctuation():
    """handles punctuation within a single sentence"""
    check50.run("python3 readability.py").stdin("There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.").stdout("Grade\D+9", "Grade 9\n").exit(0)

@check50.check(exists)
def single_sentence_complex():
    """handles more complex single sentence"""
    check50.run("python3 readability.py").stdin("Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \"and what is the use of a book,\" thought Alice \"without pictures or conversation?\"").stdout("Grade\D+8", "Grade 8\n").exit(0)

@check50.check(exists)
def multiple_sentences():
    """handles multiple sentences"""
    check50.run("python3 readability.py").stdin("Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.").stdout("Grade\D+5", "Grade 5\n").exit(0)

@check50.check(exists)
def multiple_sentences_complex():
    """handles multiple more complex sentences"""
    check50.run("python3 readability.py").stdin("It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.").stdout("Grade\D+10", "Grade 10\n").exit(0)

@check50.check(exists)
def longer_passages():
    """handles longer passages"""
    check50.run("python3 readability.py").stdin("When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.").stdout("Grade\D+8", "Grade 8\n").exit(0)

@check50.check(exists)
def sentence_punctuation():
    """handles multiple sentences with different punctuation"""
    check50.run("python3 readability.py").stdin("Congratulations! Today is your day. You're off to Great Places! You're off and away!").stdout("Grade\D+3", "Grade 3\n").exit(0)

@check50.check(exists)
def sentence_punctuation():
    """handles questions in passage"""
    check50.run("python3 readability.py").stdin("Would you like them here or there? I would not like them here or there. I would not like them anywhere.").stdout("Grade\D+2", "Grade 2\n").exit(0)

@check50.check(exists)
def before1():
    """handles reading level before Grade 1"""
    check50.run("python3 readability.py").stdin("One fish. Two fish. Red fish. Blue fish.").stdout("Before\D+Grade\D+1", "Before Grade 1\n").exit(0)

@check50.check(exists)
def grade16plus():
    """handles reading level at Grade 16+"""
    check50.run("python3 readability.py").stdin("A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.").stdout("Grade\D+16\+\n", "Grade 16+\n").exit(0)
