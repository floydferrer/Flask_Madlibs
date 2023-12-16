"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    ["name_1", "name_2", "place_1", "past_tense_verb", "noun", "adjective_1", "place_2", "adjective_2", "animal", "name_3", "period_or_question_mark"],
    """Once there were two siblings named {name_1} and {name_2}. One day, they ventured too far in the {place_1} and {past_tense_verb} in the {noun}. When they woke up, they were in a {adjective_1} place called {place_2}. They met a {adjective_2} {animal} named {name_3} and lived happily ever after... The end {period_or_question_mark}"""
)
