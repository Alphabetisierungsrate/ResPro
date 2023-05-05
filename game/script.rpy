# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    import openai
    import pyaudio
    openai.api_key = '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'
    messages = []
    messages.append({"role": "system", "content": "Roleplay. You are my girlfriend and we are about to do unspeakable things"})
    config.tts_voice = "Zira"

define e = Character("Eileen", color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.


    while True:

        menu:
            "Audio Input":
                python:
                    message = renpy.input("User input: ")

        python:
            messages.append({"role": "user", "content": message})
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages)
            output = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": output})
        m "[message]"
        e "[output]"

    # This ends the game.

    return
