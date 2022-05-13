from tkinter.filedialog import asksaveasfilename
from src.objects import Size
from src.drivers import f_generate


if __name__ == "__main__":
    # Inputs
    width = float(input("Width(mm): "))
    height = float(input("Height(mm): "))
    depth = float(input("Depth(mm): "))
    side_ext = float(input("Side Extension Length(mm): "))
    bottom_ext = float(input("Bottom Extension Length(mm): "))

    size = Size(
        width=width,
        height=height,
        depth=depth,
        side_ext=side_ext,
        bottom_ext=bottom_ext
    )

    filetypes = [("Scaleable Vector Graphics", ".svg")]
    output_path = asksaveasfilename(
        filetypes=filetypes,
        defaultextension=filetypes
    )

    f_generate(output_path, size)
