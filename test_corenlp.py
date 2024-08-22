from nlplogic.check_wiki import get_phrases, search_wikipedia, summerize_wikipedia, get_text_blob



def test_search_wikipedia():
    assert len(search_wikipedia("Jan Brzechwa")) > 0

def test_summerize_wikipedia():
    assert len(summerize_wikipedia("Jan Brzechwa")) > 0

def test_get_text_blob():
    assert get_text_blob("Jan Brzechwa") is not None


