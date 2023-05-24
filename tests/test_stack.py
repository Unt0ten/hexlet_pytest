import pytest

from hexlet_pytest.stack import stack


def test_stack():
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'


def test_empties():
    assert not stack
    stack.append('one')
    assert bool(stack)

    stack.pop()
    assert not stack


def test_pop_with_empty_stack():
    with pytest.raises(IndexError):
        stack.pop()
