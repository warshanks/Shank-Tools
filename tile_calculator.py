class TileCalculator:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_width": ("INT", {"default": 1024, "min": 16}),
                "image_height": ("INT", {"default": 1024, "min": 16}),
                "tile_width": ("INT", {"default": 1024, "min": 16}),
                "tile_height": ("INT", {"default": 1024, "min": 16}),
                "upscale_by": ("FLOAT", {"default": 1.0}),
                "steps": ("INT", {"default": 20}),
            }
        }

    RETURN_TYPES = ("STR", "INT",)
    RETURN_NAMES = ("info", "steps")
    FUNCTION = "calculate_tiles"
    CATEGORY = "ShankTools"

    def calculate_tiles(self, image_width, image_height, tile_width, tile_height, upscale_by, steps):
        import math

        # Scale the image dimensions
        scaled_width = int(image_width * upscale_by)
        scaled_height = int(image_height * upscale_by)

        # Calculate the number of tiles in each dimension
        tiles_x = math.ceil(scaled_width / tile_width)
        tiles_y = math.ceil(scaled_height / tile_height)

        # Total number of tiles
        total_tiles = tiles_x * tiles_y
        tile_size = f"{tile_width}x{tile_height}"
        scaled_size = f"{scaled_width}x{scaled_height}"
        operations = total_tiles * 2
        approximate_time = int(total_tiles * steps * 10.5 / 60)
        
        info = (f"Total tiles: {total_tiles}\n"
                f"Tile size: {tile_size}\n"
                f"Scaled size: {scaled_size}\n"
                f"Number of operations: {operations}\n"
                f"Approximate time: ~{approximate_time} minutes")

        # Return the info string wrapped in a tuple
        return (info, steps,)