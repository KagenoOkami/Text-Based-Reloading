from Weapons import Revolvers

revolver = Revolvers.Revolver(
                             name = "Revolver",
                             cylinder_chamber_count = 6,
                             action_type = Revolvers.Hammer_action.DAT,
                             loading_action = Revolvers.Loading_action.Swing
                            )

print("")

revolver.action_open_cylinder()
revolver.action_lookat_cylinder()

revolver.action_load()
revolver.action_rotate_cylinder(-1)
revolver.action_load()
revolver.action_rotate_cylinder(-1)
revolver.action_load()
revolver.action_rotate_cylinder(-1)

revolver.action_lookat_cylinder()

revolver.action_close_cylinder()

revolver.action_fire()
revolver.action_fire()
revolver.action_fire()


revolver.action_open_cylinder()
revolver.action_lookat_cylinder()


print("")

revolver.action_extract(using_speedextractor=True)
revolver.action_lookat_cylinder()










