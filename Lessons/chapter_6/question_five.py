"""Take the list ["The",   "fox",   "jumped",    "over",    "the",   "fence",
    "."] and turn it into a grammatically correct string. There should be a
space between each word, but no space between the word fence and the period that
follows it. (Dont forget, you learned a method that turns a list of strings into
a single string."""

fof=["The","fox","jumped","over","the","fence."]
one=" ".join(fof)
print(one)
