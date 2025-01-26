from .tile_calculator import TileCalculator
from .resolution_divider import ResolutionDivider
from .height_width import HeightWidth

NODE_CLASS_MAPPINGS = {
    "TileCalculator": TileCalculator,
    "ResolutionDivider": ResolutionDivider,
    "HeightWidth": HeightWidth
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TileCalculator": "Tile Calculator",
    "ResolutionDivider": "Resolution Divider",
    "HeightWidth": "Height & Width"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']