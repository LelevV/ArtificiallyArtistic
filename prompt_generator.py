"""Random prompt generator for generative art models"""
import random

ART_CONTENT_TYPE = "art_content_type.txt"
ART_DESCRIPTION = "art_description.txt"
ART_STYLE = "art_style.txt"


def get_txt_file_as_str(file: str) -> str:
    """Read file and return as str."""
    with open(file, "r", encoding="utf-8") as f:
        string = f.read()
    return string


def random_prompt_generator():
    """
    Returns one prompt for a generative art model like stable diffusion.

    Prompt format: 'a <<style>> <<content_type>> about <<description>>'

    Fills the different sections using the .txt files:
        1. "art_content_type.txt"
        2. "art_description.txt"
        3. "art_style.txt"

    Notes about generative art prompts:

    Iterate between:
        content type > description > style > composition
        Content type: What type of artwork you want to achieve?
                        Is it a photograph, drawing, sketch, 3D render..?
        Description: define the subject, subject attributes, environment/scene.
                      The more descriptive you are with the use of adjectives,
                      the better the output.
        Style: we’ve seen the most common ones above, but there are also “sub-categories”
                 – lightning, detail…
        Composition: it refers to aspect ratio, camera view and resolution.

    """

    description = get_txt_file_as_str(ART_DESCRIPTION).split("\n")
    style = get_txt_file_as_str(ART_STYLE).split("\n")
    content_type = get_txt_file_as_str(ART_CONTENT_TYPE).split("\n")

    prompt = [
        f"a {random.choice(style)} {random.choice(content_type)}",
        f"about {random.choice(description)}",
    ]
    prompt = " ".join(prompt).replace("  ", " ")

    return prompt


if __name__ == "__main__":
    for i in range(10):
        print(random_prompt_generator())
