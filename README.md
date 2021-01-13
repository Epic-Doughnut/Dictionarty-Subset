# Dictionary-Subset
Finds every word in English that includes certain letters and excludes others


# How to use
Run the following command in the command line:

`python dictionarySubset.py <include> [exclude]`

where you replace `<include>` with a string of letters that every word must include all of, and `[exclude]` is an optional string of letters that no word can include.

For example, `python dictionarySubset.py mae` would include words that include 'm', 'a', and 'e', such as commentator, hangmen, manley, mandrake, metabolism.

`python dictionarySubset.py '' aeiou` returns every word that doesn't include a standard vowel, including thy, g, ft, gym, fly

