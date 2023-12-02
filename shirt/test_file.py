import pytest
import sys
import importlib
import copy

ORIGINAL_ARGS = copy.deepcopy(sys.argv)

def test_no_args():
    with pytest.raises(SystemExit) as excinfo:
        # Bad practice
        sys.argv = ['shirt.py']
        sys.modules.pop("shirt", None)
        from shirt import shirt
        sys.argv = ORIGINAL_ARGS
    assert excinfo.value.code != 0

def test_one_arg():
    with pytest.raises(SystemExit) as excinfo:
        # Bad practice
        sys.argv = ['shirt.py', 'muppet_01.jpg']
        sys.modules.pop("shirt", None)
        from shirt import shirt
        sys.argv = ORIGINAL_ARGS
    assert excinfo.value.code != 0

def test_three_args():
    with pytest.raises(SystemExit) as excinfo:
        # Bad practice
        sys.argv = ['shirt.py', 'muppet_01.jpg', 'muppet_02.jpg', 'muppet_03.jpg']
        sys.modules.pop("shirt", None)
        from shirt import shirt
        sys.argv = ORIGINAL_ARGS
    assert excinfo.value.code != 0

def test_nonexist():
    with pytest.raises(SystemExit) as excinfo:
        # Bad practice
        sys.argv = ['shirt.py', 'nonexistentfile.jpg', 'muppet_01.jpg']
        sys.modules.pop("shirt", None)
        from shirt import shirt
        sys.argv = ORIGINAL_ARGS
    assert excinfo.value.code != 0

def test_invalid_type():
    with pytest.raises(SystemExit) as excinfo:
        # Bad practice
        sys.argv = ['shirt.py', 'invalid_extension.bmp', 'muppet_01.jpg']
        sys.modules.pop("shirt", None)
        from shirt import shirt
        sys.argv = ORIGINAL_ARGS
    assert excinfo.value.code != 0

def test_type_mismatch():
    with pytest.raises(SystemExit) as excinfo:
        # Bad practice
        sys.argv = ['shirt.py', 'muppet_01.jpg', 'muppet_01_out.png']
        sys.modules.pop("shirt", None)
        from shirt import shirt
        sys.argv = ORIGINAL_ARGS
    assert excinfo.value.code != 0