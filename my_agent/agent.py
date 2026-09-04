from strands import Agent, tool 
from strands_tools import calculator, current_time

@tool
def letter_counter(word: str, letter: str) -> int:
    """
    count occurences of a specific letter in a word

    Args: word(str): the input word to search in
    letter (str): the specific letter to count

    Returns:
        int: the number of occurences in the word
    """

    if not isinstance(word, str) or not isinstance(letter, str):
        return 0

    if len(letter) != 1:
        raise ValueError("the letter must be a single character")

    return word.lower().count(letter.lower())

#create an agent with tools from strand-tools package as well as custom letter counter tool

agent = Agent(tools=[calculator, current_time, letter_counter])

message = """
I have 4 requests:

1. What is the time right now?
2. Calculate 3111696 / 74088
3. Tell me how many letter R's are in the word "strawberry" 🍓
"""

agent(message)