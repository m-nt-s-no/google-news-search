import pytest
from pytest_mock import MockerFixture
from src import email_functions

@pytest.fixture(autouse = True)
def fake_env(monkeypatch):
    #ensures tests use fake email credentials
    monkeypatch.setattr(email_functions, "EMAIL_SENDER", "fake_email_sender")
    monkeypatch.setattr(email_functions, "EMAIL_PASSWORD", "fake_email_password")
    monkeypatch.setattr(email_functions, "EMAIL_RECIPIENT", "fake_email_recipient")

    # Patch smtplib.SMTP to return a mock instance
    mock_smtp = mocker.patch("src.email_functions.smtplib.SMTP")
    smtp_instance = mock_smtp.return_value

    # Explicitly set return values for clarity
    smtp_instance.starttls.return_value = None
    smtp_instance.login.return_value = None
    smtp_instance.sendmail.return_value = None
    smtp_instance.quit.return_value = None

    #yield fake SMTP for tests to access
    yield smtp_instance

def test_format_email_body_no_results(mocker: MockerFixture):
    content = email_functions.format_email_body({"query": []})
    assert "No new results found." in content

def test_format_email_body_one_result(mocker: MockerFixture):
    fake_results = {"title": "result1", "link": "http://example.com/1", \
                    "displayLink": "http://example.com", "snippet": "Snippet 1"}
    content = email_functions.format_email_body({"query": [fake_results]})
    assert all([item in content for item in fake_results.values()])

def test_send_email_no_results(mocker: MockerFixture):
    #Call the function with no-results string
    email_functions.send_email("No new results found.")

    #Assert that send_email returns correct parameters
    fake_env.sendmail.assert_called_once()
    from_addr, to_addr, msg_str = fake_env.sendmail.call_args[0]

    assert from_addr == "fake_email_sender"
    assert to_addr == "fake_email_recipient"
    assert "No new results found." in msg_str
    assert "Subject: Google News Search Results" in msg_str

def test_send_email_with_results(mocker: MockerFixture):
    #set up fake_results dict
    fake_results = {"title": "result1", "link": "http://example.com/1", \
                    "displayLink": "http://example.com", "snippet": "Snippet 1"}

    #format and send fake_results
    content = email_functions.format_email_body({"query": [fake_results]})
    email_functions.send_email(content)

    #capture the actual string sent in email and assert email contents are correct
    fake_env.sendmail.assert_called_once()
    from_addr, to_addr, msg_str = fake_env.sendmail.call_args[0]
    assert from_addr == "fake_email_sender"
    assert to_addr == "fake_email_recipient"
    assert "result1" in msg_str
    assert "http://example.com/1" in msg_str
    assert "http://example.com" in msg_str
    assert "Snippet 1" in msg_str
