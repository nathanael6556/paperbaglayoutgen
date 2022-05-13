from src.objects import Size, PaperBagLayout
from src.settings import TEMPLATE_PATH


def generate(template, size):
    layout = PaperBagLayout(size)
    return template.format(**layout.as_dict())


def f_generate(output_path, size):
    with open(TEMPLATE_PATH, "r") as f:
        template = f.read()

    result = generate(template, size)

    with open(output_path, "w") as f:
        f.write(result)
