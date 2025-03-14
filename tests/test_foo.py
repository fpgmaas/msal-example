from msal_example.foo import foo
from tests.utils import run_within_dir


def test_foo(tmp_path):
    with run_within_dir(tmp_path):
        assert foo("foo") == "foo"
