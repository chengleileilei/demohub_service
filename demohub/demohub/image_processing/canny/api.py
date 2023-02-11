from .type import *

introduction = """
this is a introduction to the demo.
"""

paper = """
this demo refers to this paper: link.
"""

github = """
this demo refers to this code: link.
"""


args = {
    "image_path": STRING(default_val=None),
    "--space": STRING(default="rgb", options=["rgb", "hsv"]),
}

command = """
    python demo.py {image_path} \
        --space {space}
    """.format(
        image_path=args['image_path'],
        space=args['--space']
    )