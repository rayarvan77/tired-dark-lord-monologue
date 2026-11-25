"""The Tired Dark Lord: A 100-Word Villain Monologue.

Entry for the make.fun bounty
"u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb".

Writes the monologue to /output/entry.txt and prints it.
Python 3.13, standard library only, deterministic output.
"""

MONOLOGUE = (
    "People picture me on a throne of skulls, laughing. The throne is "
    "\u2014 well. It's a chair. The skulls left over the damp. Heroes keep "
    "arriving at dawn, full of speeches. Dawn is an unreasonable hour. "
    "I've moved the eclipse to Thursday. The volcano sent a notice: the "
    "lava counts as an unpermitted renovation. The minions have unionised, "
    "which I respect, and which slows everything down. The prophecy says I "
    "fall to a child with a pure heart. Fine. Let the child do the "
    "paperwork. I have a kingdom to ruin and a curse to renew \u2014 after "
    "a nap, if anyone remembers to wake me."
)


def word_count(text):
    """Count words the way a reader would: split on whitespace."""
    return len(text.split())


def validate(text):
    """Self-check against the brief's gate.

    The bounty gate requires /output/entry.txt to hold UTF-8 text of
    1 to 600 characters, not only whitespace. The brief asks for a
    monologue of about 100 words, so we also require 90-110 words.
    The tiredness must live in the voice, the rhythm and the small
    deflections, never in a plain statement, so the text must not
    contain the words tired, weary, exhausted or sleepy.
    """
    words = word_count(text)
    chars = len(text)
    assert text.strip(), "monologue must not be empty or only whitespace"
    assert 1 <= chars <= 600, f"gate: {chars} chars, must be 1-600"
    assert 90 <= words <= 110, f"brief: {words} words, want about 100"
    lowered = text.lower()
    for banned in ("tired", "weary", "exhausted", "sleepy"):
        assert banned not in lowered, f"brief: must not plainly say '{banned}'"
    return words, chars


def main():
    words, chars = validate(MONOLOGUE)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)
    print(MONOLOGUE)
    print(f"\n[words: {words} | chars: {chars}]")


if __name__ == "__main__":
    main()
