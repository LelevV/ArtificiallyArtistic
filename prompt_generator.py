"""Random prompt generator for generative art models"""
import random


def get_txt_file_as_str(file: str) -> str:
    """Read file and return as str."""
    with open(file, "r", encoding="utf-8") as f:
        string = f.read()
    return string


def read_art_file(file: str) -> list:
    """Read the art .txt file. Each line should contain one option."""
    file_str = get_txt_file_as_str(file)
    options = file_str.split("\n")
    return options


def random_prompt_generator(
    art_descriptions: list, art_styles: list, content_types: list
) -> str:
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
    prompt = [
        f"a {random.choice(art_styles)} {random.choice(content_types)}",
        f"about {random.choice(art_descriptions)}",
    ]
    prompt = " ".join(prompt).replace("  ", " ")
    return prompt


if __name__ == "__main__":
    ART_CONTENT_TYPE = "art_content_type.txt"
    ART_DESCRIPTION = "art_description.txt"
    ART_STYLE = "art_style.txt"

    art_descriptions_list = read_art_file(ART_DESCRIPTION)
    art_styles_list = read_art_file(ART_STYLE)
    content_types_list = read_art_file(ART_CONTENT_TYPE)

    for i in range(10):
        print(
            random_prompt_generator(
                art_descriptions_list, art_styles_list, content_types_list
            )
        )
