from Weapons import Revolvers

revolver = Revolvers.Revolver(
                             name = "Revolver",
                             cylinder_chamber_count = 6,
                             action_type = Revolvers.Hammer_action.DAT,
                             loading_action = Revolvers.Loading_action.Swing
                            )

ammocount = 10


revolver.action_open_cylinder()
revolver.action_lookat_cylinder()
#revolver.action_close_cylinder()

revolver.cock_hammer()

revolver.action_fire()