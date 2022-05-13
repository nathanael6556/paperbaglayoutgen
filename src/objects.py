class Size:
    def __init__(self, width, height, depth, side_ext, bottom_ext):
        self.width = float(width)
        self.height = float(height)
        self.depth = float(depth)
        self.side_ext = float(side_ext)
        self.bottom_ext = float(bottom_ext)
        self.half_depth = float(depth) / 2.0

    def as_dict(self):
        return {
            "width": self.width,
            "height": self.height,
            "depth": self.depth,
            "side_ext": self.side_ext,
            "bottom_ext": self.bottom_ext,
            "half_depth": self.half_depth
        }


class PaperBagLayout:
    def __init__(self, size):
        self.size = size

        self.x_guidelines = [
            0.0,
            size.side_ext,
            size.side_ext + size.half_depth,
            size.side_ext + size.depth,
            size.side_ext + size.depth + size.width,
            size.side_ext + size.depth + size.width + size.half_depth,
            size.side_ext + size.depth + size.width + size.depth,
            size.side_ext + size.depth + size.width + size.depth + size.width,
        ]
        self.y_guidelines = [
            0.0,
            size.height,
            size.height + size.half_depth,
            size.height + size.half_depth + size.bottom_ext,
        ]

        """ Specifically for the striped line """
        self.lx_guidelines = [
            self.x_guidelines[3] + size.bottom_ext,
            self.x_guidelines[4] - size.bottom_ext,
            self.x_guidelines[6] + size.bottom_ext,
            self.x_guidelines[7] - size.bottom_ext,
        ]
        self.ly_guidelines = [
            self.y_guidelines[2] + size.side_ext,
            self.y_guidelines[2] + size.half_depth,
        ]

    def as_dict(self):
        result = self.size.as_dict()

        def add_to_result(array, prefix):
            for (index, elem) in enumerate(array):
                key = prefix + str(index)
                result[key] = array[index]

        add_to_result(self.x_guidelines, "x")
        add_to_result(self.y_guidelines, "y")
        add_to_result(self.lx_guidelines, "lx")
        add_to_result(self.ly_guidelines, "ly")

        return result
