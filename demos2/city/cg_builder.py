from dataclasses import dataclass, field
from typing import List


# ============================================================================
# Basic geometry
# ============================================================================

@dataclass
class Point2:
    x: float
    y: float

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"


# ============================================================================
# Footprint description
# ============================================================================

@dataclass
class Edge:
    indices: tuple[int, int]
    tags: List[str] = field(default_factory=list)

    def __str__(self):
        return (
            f"Edge(indices={self.indices}, "
            f"tags={self.tags})"
        )


@dataclass
class Corner:
    point: int
    tags: List[str] = field(default_factory=list)

    def __str__(self):
        return (
            f"Corner(point={self.point}, "
            f"tags={self.tags})"
        )


@dataclass
class Neighbor:
    type: str
    footprint: List[Point2]
    height: float

    def __str__(self):

        pts = ", ".join(str(p) for p in self.footprint)

        return (
            f"Neighbor(type='{self.type}', "
            f"height={self.height:.2f}, "
            f"footprint=[{pts}])"
        )


@dataclass
class Footprint:
    unit: str
    points: List[Point2]
    edges: List[Edge]
    corners: List[Corner] = field(default_factory=list)
    neighbors: List[Neighbor] = field(default_factory=list)

    # ------------------------------------------------------------------------
    # JSON loader
    # ------------------------------------------------------------------------

    @classmethod
    def from_dict(cls, data: dict) -> "Footprint":

        fp = data["footprint"]

        points = [
            Point2(*p)
            for p in fp["points"]
        ]

        edges = [
            Edge(
                indices=tuple(edge["indices"]),
                tags=edge.get("tags", [])
            )
            for edge in fp.get("edges", [])
        ]

        corners = [
            Corner(
                point=corner["point"],
                tags=corner.get("tags", [])
            )
            for corner in fp.get("corners", [])
        ]

        neighbors = []

        for neighbor in fp.get("neighbors", []):

            neighbor_points = [
                Point2(*p)
                for p in neighbor["footprint"]
            ]

            neighbors.append(
                Neighbor(
                    type=neighbor["type"],
                    footprint=neighbor_points,
                    height=neighbor["height"]
                )
            )

        return cls(
            unit=fp.get("unit", "m"),
            points=points,
            edges=edges,
            corners=corners,
            neighbors=neighbors
        )

    # ------------------------------------------------------------------------
    # String representation
    # ------------------------------------------------------------------------

    def __str__(self):

        s = "Footprint\n"
        s += f"  unit: {self.unit}\n"

        s += "  points:\n"
        for i, p in enumerate(self.points):
            s += f"    {i}: {p}\n"

        s += "  edges:\n"
        for i, e in enumerate(self.edges):
            s += f"    {i}: {e}\n"

        if self.corners:
            s += "  corners:\n"
            for i, c in enumerate(self.corners):
                s += f"    {i}: {c}\n"

        if self.neighbors:
            s += "  neighbors:\n"
            for i, n in enumerate(self.neighbors):
                s += f"    {i}: {n}\n"

        return s


if True:

    data = {
        "footprint": {
            "unit": "m",

            "points": [
                [0.0, 0.0],
                [8.0, 0.0],
                [8.0, 5.0],
                [5.5, 5.0],
                [5.5, 6.5],
                [0.0, 6.5]
            ],

            "edges": [
                {"indices": [0, 1], "tags": ["street", "main_facade"]},
                {"indices": [1, 2], "tags": ["party_wall"]},
                {"indices": [2, 3], "tags": ["courtyard"]},
                {"indices": [3, 4], "tags": ["courtyard", "cut_angle"]},
                {"indices": [4, 5], "tags": ["courtyard"]},
                {"indices": [5, 0], "tags": ["party_wall"]}
            ],

            "neighbors": [
                {
                    "type": "party_building",
                    "footprint": [
                        [8.0, 0.0],
                        [11.0, 0.0],
                        [11.0, 3.5],
                        [8.0, 3.5]
                    ],
                    "height": 7.0
                },
                {
                    "type": "party_building",
                    "footprint": [
                        [-3.0, 0.0],
                        [0.0, 0.0],
                        [0.0, 6.5],
                        [-3.0, 6.5]
                    ],
                    "height": 9.0
                }
            ],

            "corners": [
                {
                    "point": 0,
                    "tags": ["reinforced", "large_stone_base"]
                },
                {
                    "point": 1,
                    "tags": ["reinforced", "street_corner"]
                }
            ]
        }
    }

    footprint = Footprint.from_dict(data)

    print(footprint)
