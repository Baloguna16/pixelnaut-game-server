import os

class Config:

    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY")

class TestConfig:

    TESTING = True
    SECRET_KEY = os.getenv("SECRET_KEY")

class WalletConfig:

    PUBKEY = os.getenv("PUBKEY")
    PRIVKEY = os.getenv("PRIVKEY")

    #MINT = os.getenv("MINT_ADDRESS")
