"""
    Run this module just one time when you add new settings.yaml file
    in project, for encrypt it. This step necessary for properly work this app.
    If you miss this step then most likely app will raise exception
"""

from functions.settings_encryptor import encryptor

# Execute this
encryptor.first_running()


