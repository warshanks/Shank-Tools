class ResolutionDivider:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_width": ("INT", {"default": 1024, "min": 16}),
                "image_height": ("INT", {"default": 1024, "min": 16}),
                "divide_by": ("INT", {"default": 2, "min": 1}),
            }
        }

    RETURN_TYPES = ("INT", "INT",)
    RETURN_NAMES = ("width", "height",)
    FUNCTION = "divide_resolution"
    CATEGORY = "ShankTools"

    def divide_resolution(self, image_width, image_height, divide_by):
        return (image_width // divide_by, image_height // divide_by,)