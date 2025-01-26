# Outputs two integers for height and width

class HeightWidth:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_width": ("INT", {"default": 1024, "min": 16}),
                "image_height": ("INT", {"default": 1024, "min": 16}),
            }
        }

    RETURN_TYPES = ("INT", "INT",)
    RETURN_NAMES = ("width", "height",)
    FUNCTION = "execute"
    CATEGORY = "ShankTools"
    def execute(self, image_width, image_height):
        return (image_width, image_height,)