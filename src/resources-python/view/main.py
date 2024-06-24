import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
sys.path.append(project_dir)

from view_principal import RobotUI

robot_ui = RobotUI()

robot_ui.pack()
robot_ui.mainloop()