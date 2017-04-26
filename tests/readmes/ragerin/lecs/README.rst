====
lecs
====
Lightweight Entity Component System for Python

Example usage
=============
.. code:: python

    from lecs.ecs import ECS, Entity, Component, System

    # Create a simple component
    class MooComponent(Component):
        """Data container for cow sounds."""
        def __init__(self):
            super().__init__()
            self.message = 'MOO!'

    # And another, just as an example. Note that this one doesn't have any data, so it's actually used like a property
    class BullComponent(Component):
        """Denotes that the entity is a bull."""
        def __init__(self):
            super().__init__()

    # Now create a system to handle the components
    class CattleSystem(System):
        def __init__(self, ecs, component_class):
            super().__init__(ecs, component_class)

        def Execute(self):
            for component in self.Components():
                # Let's see if the parent entity also holds a BullComponent
                if component.parent_entity.GetComponentByName('BullComponent'):
                    print('I am a BULL!')
                print(component.message)


    # Instantiate a base ECS container
    ecs = ECS()


    # Add a new empty entity
    cow = ecs.AddEntity()
    # Add a MooComponent to the entity
    cow.AddComponent(MooComponent())


    # Let's add one more entity
    bull = ecs.AddEntity()
    bull.AddComponent(MooComponent())
    # This one is a bull, so we add another component
    bull.AddComponent(BullComponent())


    # We add the CattleSystem. We also add the class name of the component it looks for.
    s = CattleSystem(ecs, 'MooComponent')

    # We call the Execute() method for the system.
    s.Execute()

    # Alternatively we can loop over multiple systems, which would be nice when we add more later
    for system in ecs.systems:
        system.Execute()
