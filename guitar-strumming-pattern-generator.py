"""
Generates and prints a guitar strumming pattern.
"""

import random
from enum import Enum

enable_muting = False  # muted strums off by default


class StrumTypes(Enum):
    """
    Enumeration for different types of guitar strumming patterns.
    """

    DOWN = "🔽"
    PAUSE = "  "
    UP = "🔼"
    MUTE = "X "


def strumming_pattern_generator():
    """
    Generates a dictionary containing lists of down and up strum options.

    Returns:
        dict: A dictionary with two keys 'down_strum_options' and 'up_strum_options',
              each containing a list of corresponding strumming symbols.
    """
    down_strum_options = [
        StrumTypes.DOWN.value,
        StrumTypes.PAUSE.value,
        StrumTypes.MUTE.value,
    ]
    up_strum_options = [
        StrumTypes.UP.value,
        StrumTypes.PAUSE.value,
    ]

    return {
        "down_strum_options": down_strum_options,
        "up_strum_options": up_strum_options,
    }


def filter_multiple_mutes(generated_down_strum, generated_pattern, strumming_options):
    """
    Ensures that only one, and not multiple mute strums are not allowed in the pattern.

    Args:
        generated_down_strum (str): The currently generated strum for a down stroke.
        generated_pattern (list): The list of already generated strums in the pattern.
        strumming_options (dict): A dictionary with available strumming options.

    Returns:
        str: The final choice for the down strum, ensuring no multiple mutes.
    """
    if generated_down_strum == StrumTypes.MUTE.value:
        if generated_down_strum in generated_pattern:
            while generated_down_strum == StrumTypes.MUTE.value:
                generated_down_strum = random.choice(
                    strumming_options["down_strum_options"]
                )

    return generated_down_strum


def create_output(generated_pattern):
    """
    Creates a formatted string representing the strumming pattern.

    Args:
        generated_pattern (list): The list of strums to be displayed.

    Returns:
        str: A formatted string representing the strumming pattern.
    """
    final_output = (
        "+-------+-------+-------+-------+-------+-------+-------+-------+\n"
        "|   1   |   &   |   2   |   &   |   3   |   &   |   4   |   &   |\n"
        "+-------+-------+-------+-------+-------+-------+-------+-------+\n"
        f"|   {generated_pattern[0]}  |   {generated_pattern[1]}  |   {generated_pattern[2]}  |   {generated_pattern[3]}  |   {generated_pattern[4]}  |   {generated_pattern[5]}  |   {generated_pattern[6]}  |   {generated_pattern[7]}  |\n"
        "+-------+-------+-------+-------+-------+-------+-------+-------+\n"
    )

    return final_output


def main(enable_muting=enable_muting):
    """
    Main function to generate and print a guitar strumming pattern.
    """
    strumming_options = strumming_pattern_generator()

    while True:
        generated_pattern = []
        for x in range(0, 8):
            if x % 2 == 0:  # down strum
                weights = [1, 1, 0] if not enable_muting else [1, 1, 0.15]
                generated_down_strum = random.choices(
                    #  reduce MUTE probality to either 0% or 10%.
                    strumming_options["down_strum_options"],
                    weights=weights,
                )[0]
                generated_down_strum = filter_multiple_mutes(
                    generated_down_strum, generated_pattern, strumming_options
                )

                generated_pattern.append(generated_down_strum)
            else:  # up strum
                generated_up_strum = random.choice(
                    strumming_options["up_strum_options"]
                )
                generated_pattern.append(generated_up_strum)

        print("\n")
        print(create_output(generated_pattern))
        print("\n")

        user_input = input(
            "[q] to quit | [m] to enable muted strums | [enter] to regenerate > "
        )
        if user_input.lower() == "m":
            enable_muting = True
        elif user_input != "":
            print("\nExiting!")
            return True
        print("Regenerating...")


if __name__ == "__main__":
    main()
