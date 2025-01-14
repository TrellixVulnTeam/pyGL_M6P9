from game.Model.Model import Model
import sys


class Terrain:
    def __init__(self, grid, loader, texture_pack, blend_map):
        self.size = 200
        self.vertex_count = 32

        self.x = grid[0] * self.size
        self.z = grid[1] * self.size

        self.texture_pack = texture_pack
        self.blend_map = blend_map
        self.indices = None
        self.model = self.generate_terrain(loader)

    def generate_terrain(self, loader):
        count = self.vertex_count * self.vertex_count
        vertices = [None] * count * 3
        normals = [None] * count * 3
        texture_coords = [None] * count * 2
        indices = [None] * 6 * (self.vertex_count-1) * (self.vertex_count-1)

        vertex_pointer = 0
        for i in range(0, self.vertex_count):
            for j in range(0, self.vertex_count):
                vertices[vertex_pointer * 3] = j/(self.vertex_count - 1) * self.size
                vertices[vertex_pointer * 3 + 1] = 0
                vertices[vertex_pointer * 3 + 2] = i/(self.vertex_count - 1) * self.size
                normals[vertex_pointer * 3] = 0
                normals[vertex_pointer * 3 + 1] = 1
                normals[vertex_pointer * 3 + 2] = 0
                texture_coords[vertex_pointer * 2] = j/(self.vertex_count - 1)
                texture_coords[vertex_pointer * 2 + 1] = i/(self.vertex_count - 1)
                vertex_pointer += 1
        pointer = 0
        for gz in range(0, self.vertex_count - 1):
            for gx in range(0, self.vertex_count - 1):
                topLeft = (gz * self.vertex_count) + gx
                topRight = topLeft + 1
                bottomLeft = ((gz + 1) * self.vertex_count) + gx
                bottomRight = bottomLeft + 1
                indices[pointer] = topLeft
                pointer += 1
                indices[pointer] = bottomLeft
                pointer += 1
                indices[pointer] = topRight
                pointer += 1
                indices[pointer] = topRight
                pointer += 1
                indices[pointer] = bottomLeft
                pointer += 1
                indices[pointer] = bottomRight
                pointer += 1
        model = Model(
            loader,
            vertices,
            texture_coords,
            normals,
            indices,
            0,
            None
        )
        self.indices = sys.getsizeof(loader.get_indices(model))
        return loader.load(model)


class TerrainTexture:
    def __init__(self, TEX_ID):
        self.TEX_ID = TEX_ID


class TerrainTexturePack:
    def __init__(self, bg_texture, r_texture, g_texture, b_texture):
        self.bg_texture = bg_texture
        self.r_texture = r_texture
        self.g_texture = g_texture
        self.b_texture = b_texture
