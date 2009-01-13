"""Schema for CubeCAD."""

from schevo.schema import *
schevo.schema.prep(locals())


def all(seq):
    for item in seq:
        if not item:
            return False
    return True


class Coordinates(F.Field):

    def convert(self, value):
        return tuple(int(v) for v in value)

    def validate(self, value):
        if not (
            isinstance(value, tuple)
            and all(isinstance(v, int)) for v in value)
            ):
            raise ValueError('Must be a (x,y,z) tuple.')


class Distance(F.Field):

    def convert(self, value):
        return (float(value[0]), unicode(value[1]))

    def validate(self, value):
        if not (
            isinstance(value, tuple)
            and len(value) == 2
            and isinstance(value[0], (int, float))
            and isinstance(value[1], basestring)
            ):
            raise ValueError('Must be a (amount, unit) tuple.')


class Space(E.Entity):
    """A space to be populated with cubes/voxels representing beams.

    Facing the space, the origin (0,0,0) is the bottom left voxel of the
    space. Cubes are each allocated one voxel.
    """

    name = f.string()
    cube_type = f.entity('CubeType')
    x_length = f.integer(units='units')
    y_length = f.integer(units='units')
    z_length = f.integer(units='units')

    _key(name)

    _sample = [
        dict(
            name='Toddler Chair',
            cube_type=dict(
                material=dict(name='Wood'),
                edge_length=(1.5, 'inches'),
            ),
            x_length=32,
            y_length=32,
            z_length=32,
        ),
    ]


class Beam(E.Entity):
    """A beam."""

    space = f.entity('Space')
    origin = f.coordinates()
    orientation = f.entity('Orientation')
    length = f.integer()
    @f.entity_list('Cube')
    def cubes(self):
        return []

    _key(space, origin)

    _sample = [
        dict(
            space=dict(name='Toddler Chair'),
            origin=(0,0,0),
            orientation=dict(name='Bottom-to-top'),
            length=8,
        ),
        # XXX: To-do - rest of pieces!
        dict(
            space=dict(name='Toddler Chair'),
            origin=(,,),
            orientation=dict(name=''),
            length=,
        ),
        dict(
            space=dict(name='Toddler Chair'),
            origin=(,,),
            orientation=dict(name=''),
            length=,
        ),
        dict(
            space=dict(name='Toddler Chair'),
            origin=(,,),
            orientation=dict(name=''),
            length=,
        ),
        dict(
            space=dict(name='Toddler Chair'),
            origin=(,,),
            orientation=dict(name=''),
            length=,
        ),
        dict(
            space=dict(name='Toddler Chair'),
            origin=(,,),
            orientation=dict(name=''),
            length=,
        ),
        dict(
            space=dict(name='Toddler Chair'),
            origin=(,,),
            orientation=dict(name=''),
            length=,
        ),
        dict(
            space=dict(name='Toddler Chair'),
            origin=(,,),
            orientation=dict(name=''),
            length=,
        ),
        dict(
            space=dict(name='Toddler Chair'),
            origin=(,,),
            orientation=dict(name=''),
            length=,
        ),
        dict(
            space=dict(name='Toddler Chair'),
            origin=(,,),
            orientation=dict(name=''),
            length=,
        ),
        dict(
            space=dict(name='Toddler Chair'),
            origin=(,,),
            orientation=dict(name=''),
            length=,
        ),
        dict(
            space=dict(name='Toddler Chair'),
            origin=(,,),
            orientation=dict(name=''),
            length=,
        ),
    ]


class Connector(E.Entity):
    """A connector between two beams."""

    beams = f.entity_set('Beam', min_size=2, max_size=2)
    connected_at = f.entity_set('Cube', min_size=2, max_size=2)


class Cube(E.Entity):
    """A cube within a space.

    Acts as a cache to help with collision detection for beams.
    """

    space = f.entity('Space')
    location = f.coordinates()

    _key(space, location)


class CubeType(E.Entity):
    """A type of cube used to allocate beams in a space."""

    material = f.entity('Material')
    edge_length = f.distance()

    _key(material, edge_length)

    _initial = [
        dict(
            material=dict(name='Wood'),
            edge_length=(1.5, 'inches'),
        ),
    ]


class Material(E.Entity):
    """A material used to create beams."""

    name = f.string()

    _key(name)

    _initial = [
        dict(
            name='Wood',
        ),
    ]


class Orientation(E.Entity):
    """The orientation of a beam."""

    name = f.string()
    x_delta = f.integer()
    y_delta = f.integer()
    z_delta = f.integer()

    _key(name)
    _key(x_delta, y_delta, z_delta)

    _initial = [
        ('Front-to-back', 0, 1, 0),
        ('Back-to-front', 0, -1, 0),
        ('Left-to-right', 1, 0, 0),
        ('Right-to-left', -1, 0, 0),
        ('Bottom-to-top', 0, 0, 1),
        ('Top-to-bottom', 0, 0, -1),
    ]
