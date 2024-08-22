#!/usr/bin/env python
from nlplogic.check_wiki import get_phrases
import fire


def hello(name="World"):
    return "Hello %s!" % name


if __name__ == "__main__":
    fire.Fire(get_phrases)
