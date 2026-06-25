import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module

INITIAL_ACTIVITIES = copy.deepcopy(app_module.activities)


def reset_activities() -> None:
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(INITIAL_ACTIVITIES))


@pytest.fixture(autouse=True)
def reset_app_state() -> None:
    reset_activities()


@pytest.fixture
def client() -> TestClient:
    return TestClient(app_module.app)
