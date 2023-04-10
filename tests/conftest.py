import pytest
from main import read_file
@pytest.fixture(autouse=True)
def file_fixture():
    with open("fixture_file", 'w') as file:
        lines = ["Apple 2022-04-08 12.50\n",
                "Banana 2022-04-08 15.0\n",
                "Apple 2022-05-08 15.50\n",
                "Banana 2022-05-08 25.0\n"]
        file.writelines(lines)
    return "fixture_file"


