import replicate

REPLICATE_API_TOKEN = "r8_JLosWfgzJu6KExgiR5Efdq9JEDVxKCg2M9gsp"

def RESPONSE():
    input = {
        "prompt": '''Create a detective story based on the following parameters:

    Difficulty Level: The difficulty level is a number between 0 and 1. A difficulty of 0 should generate a very easy story with an obvious solution, while a difficulty of 1 should generate a very challenging story with a complex and less obvious solution.

    Number of Suspects: The number of suspects involved in the story.

    Requirements:


    1. It should introduce the suspects, provide clues, and present a mystery to be solved.
    2. The clues should be appropriate for the specified difficulty level. For example, at lower difficulty, clues might be straightforward, while at higher difficulty, clues could be more subtle and require careful analysis.


    Input:
    -Difficulty Level: 0.8
    -Number of Suspects: 5
    Output:
    Json Format having three varaible story, sloution, prepetrator.


    ''',
        "temperature": 0.2
    }

    api = replicate.Client(api_token= REPLICATE_API_TOKEN)
    output = api.run(
        "snowflake/snowflake-arctic-instruct",
            input=input
        )


    for item in output:
        print(item, end="")
    return output