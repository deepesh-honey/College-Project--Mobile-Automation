import pytest

@pytest.mark.flaky(reruns=3)
@pytest.mark.usefixtures("failure_test_ss", "setup_teardown_Single_Device")
class BaseTest:
    pass
