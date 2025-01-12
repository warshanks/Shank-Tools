from .tile_calculator import TileCalculator
from .resolution_divider import ResolutionDivider

NODE_CLASS_MAPPINGS = {
    "TileCalculator": TileCalculator,
    "ResolutionDivider": ResolutionDivider
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TileCalculator": "Tile Calculator",
    "ResolutionDivider": "Resolution Divider"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']