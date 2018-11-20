import Weapons

revolver = Weapons.Weapon("revolver", 6)

ammocount = 10

# Fire when unloaded; Fail
revolver.fire()

# Load then fire; Success
revolver.load()
revolver.fire()

# Fire without reloading; Fail
revolver.fire()

#empty interal storage; Fail
revolver.load()
revolver.fire()
revolver.load()
revolver.fire()
revolver.load()
revolver.fire()
revolver.load()
revolver.fire()
revolver.load()
revolver.fire()
revolver.load()
revolver.fire()