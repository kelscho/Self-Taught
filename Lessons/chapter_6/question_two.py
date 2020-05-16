"""Write a prgram hat collects two strings from a user, inserts them into
the string "Yesterday I wrote a [response_one]. I sent it to {response_two]!"
and prints a new string."""

response_one=input("Yesterday I wrote a: what? ")
response_two=input("I sent it to: who? ")
i="""Yesterday I wrote a {}. I sent it to {}!
""".format(response_one,response_two)

print(i)
