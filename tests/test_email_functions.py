import pytest
from pytest_mock import MockerFixture
from src import email_functions

@pytest.fixture(autouse = True)
def fake_env(monkeypatch):
    #ensures tests use fake email credentials
    monkeypatch.setattr(email_functions, "EMAIL_SENDER", "fake_email_sender")
    monkeypatch.setattr(email_functions, "EMAIL_PASSWORD", "fake_email_password")
    monkeypatch.setattr(email_functions, "EMAIL_RECIPIENT", "fake_email_recipient")

def test_format_email_body_no_results(mocker: MockerFixture):
    content = email_functions.format_email_body({"query": []})
    assert "No new results found." in content

def test_format_email_body_one_result(mocker: MockerFixture):
    fake_results = {"title": "result1", "link": "http://example.com/1", \
                    "displayLink": "http://example.com", "snippet": "Snippet 1"}
    content = email_functions.format_email_body({"query": [fake_results]})
    assert all([item in content for item in fake_results.values()])

def test_send_email_no_results(mocker: MockerFixture):
    #Mock SMTP library to avoid sending real emails
    mock_smtp = mocker.patch("src.email_functions.smtplib.SMTP")
    mock_smtp.return_value.sendmail.return_value = None

    #Call the function with no-results string
    email_functions.send_email("No new results found.")

    #Assert that send_email returns correct parameters
    args, _ = mock_smtp.return_value.sendmail.call_args
    from_addr, to_addr, msg_str = args

    assert from_addr == "fake_email_sender"
    assert to_addr == "fake_email_recipient"
    assert "No new results found." in msg_str
    assert "Subject: Google News Search Results" in msg_str

def test_send_email_with_results(mocker: MockerFixture):
    #mock SMTP so no real emails are sent
    mock_smtp = mocker.patch("src.email_functions.smtplib.SMTP")
    mock_smtp.return_value.sendmail.return_value = None

    #set up fake_results dict
    fake_results = {"title": "result1", "link": "http://example.com/1", \
                    "displayLink": "http://example.com", "snippet": "Snippet 1"}

    #format and send fake_results
    content = email_functions.format_email_body({"query": [fake_results]})
    email_functions.send_email(content)

    #capture the actual string sent in email and assert email contents are correct
    from_addr, to_addr, msg_str = mock_smtp.return_value.sendmail.call_args[0]
    assert from_addr == "fake_email_sender"
    assert to_addr == "fake_email_recipient"

    assert "result1" in msg_str
    assert "http://example.com/1" in msg_str
    assert "http://example.com" in msg_str
    assert "Snippet 1" in msg_str