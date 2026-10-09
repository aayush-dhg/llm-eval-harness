import json
from pathlib import Path

import pytest
from app.qa import answer_question


# Hard Coding
# /** def test_answer_supported_by_context():
#     context = """
#     Python lists are mutable sequences. This means their contents can be changed
#     after the list is created.
#     """

#     question = "Can a Python list be modified after creation?"

#     answer = answer_question(question, context).lower()

#     assert "yes" in answer
#     assert (
#         "modified after creation" in answer
#         or "changed after creation" in answer
#         or "mutable" in answer
#     )


# def test_refuses_when_answer_not_in_context():
#     context = """
#     Python lists are mutable sequences. This means their contents can be changed
#     after the list is created.
#     """

#     question = "Who created Python?"

#     answer = answer_question(question, context).lower()

#     assert "don't know" in answer **/



# Pulling from Json##

DATA_FILE = Path("data/golden_cases.json")


with DATA_FILE.open("r", encoding="utf-8") as file:
    GOLDEN_CASES = json.load(file)


@pytest.mark.parametrize(
    "case",
    GOLDEN_CASES,
    ids=[case["id"] for case in GOLDEN_CASES],
)
def test_golden_cases(case):
    answer = answer_question(
        question=case["question"],
        context=case["context"],
    ).lower()

    if case["should_refuse"]:
        assert "don't know" in answer
    else:
        for fact in case["expected_facts"]:
            assert fact.lower() in answer