import pytest
from once import once

@once
def mock_func():
  mock_func.counter += 1
  return 2 + 2

mock_func.counter = 0

def test_once():
  mock_func()
  mock_func()
  assert mock_func.counter == 1
