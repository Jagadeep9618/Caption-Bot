import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7556028418:AAHGiXceLcmzzYK_cwXtXcch0ec2DbTKhXw")
      API_ID = int(os.environ.get("APP_ID", "21529028"))
      API_HASH = os.environ.get("API_HASH", "c5d7d11578ed6d8944c878fae879602c")
      CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "kofi")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "AvishkarPatil")
