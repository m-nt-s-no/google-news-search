import pytest
import requests
from requests.exceptions import HTTPError
from src import news_search

@pytest.fixture(autouse = True)
def fake_env(monkeypatch):
    #ensures tests always use fake API credentials
    monkeypatch.setattr(news_search, "GOOGLE_API_KEY", "fake_api_key")
    monkeypatch.setattr(news_search, "GOOGLE_CSE_ID", "fake_cse_id")

def test_run_search_multiple_pages(requests_mock):
    #mock multi-page API response; pg 1 has results, pg 2 empty
    query = "test_query"
    mock_response_page1 = {
        "items": [
            {"title": "Test News 1", "link": "http://example.com/1", "displayLink": "example.com", "snippet": "Snippet 1"},
        ]
    }
    mock_response_page2 = {
        "items": []
    }
    requests_mock.get("https://www.googleapis.com/customsearch/v1", [
        {"json": mock_response_page1, "status_code": 200},
        {"json": mock_response_page2, "status_code": 200}
    ])

    results = news_search.run_search(query)
    assert len(results) == 1
    assert results[0]["title"] == "Test News 1"

def test_run_search_no_results(requests_mock):
    #mock API response with no results
    query = "test_query"
    mock_response = {
        "items": []
    }
    requests_mock.get("https://www.googleapis.com/customsearch/v1", json = mock_response)

    results = news_search.run_search(query)
    assert len(results) == 0

def test_run_search_three_pages(requests_mock):
    #Simulate pagination across three pages
    query = "multi_page_query"
    page1 = {"items": [{"title": "P1"}]}
    page2 = {"items": [{"title": "P2"}]}
    page3 = {"items": []} 

    requests_mock.get("https://www.googleapis.com/customsearch/v1", [
        {"json": page1, "status_code": 200},
        {"json": page2, "status_code": 200},
        {"json": page3, "status_code": 200}
    ])

    results = news_search.run_search(query)
    titles = [r["title"] for r in results]
    assert len(results) == 2
    assert titles == ["P1", "P2"]

def test_run_search_http_error(requests_mock):
    #mock API response with HTTP errors other than 429
    requests_mock.get("https://www.googleapis.com/customsearch/v1", status_code = 500)

    with pytest.raises(HTTPError):
        news_search.run_search("server_error")

def test_main_handles_http_error_429(monkeypatch, capsys):
    def mock_run_search(query):
        raise HTTPError(response = type("obj", (object,), {"status_code": 429})())

    monkeypatch.setattr(news_search, "run_search", mock_run_search)
    news_search.main()
    captured = capsys.readouterr()
    assert "Too many requests" in captured.out

def test_run_search_malformed_json(requests_mock):
    #If API returns JSON without 'items' key — should not break
    query = "malformed_query"
    requests_mock.get("https://www.googleapis.com/customsearch/v1", 
                      json={"unexpected": "data"}, status_code = 200)

    results = news_search.run_search(query)
    assert results == []