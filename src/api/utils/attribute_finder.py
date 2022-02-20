from collections import namedtuple
from solana.rpc.api import Client
from solana.publickey import PublicKey
from solana.rpc.types import TokenAccountOpts, MemcmpOpts
from base58 import b58decode
import base58
from base64 import b64decode
import struct

http_client = Client("https://solana-api.projectserum.com")

#

def get_nft_info(): 
    test = list(bytes(PublicKey('9eohkfSjLNd7GfU7wMoDA5RakpWbzHEodikdik9NHuMW')))
  #  response = http_client.get_program_accounts(PublicKey('metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s'), memcmp_opts=[MemcmpOpts(33,'9eohkfSjLNd7GfU7wMoDA5RakpWbzHEodikdik9NHuMW')])
    #response = http_client.meta(PublicKey("9eohkfSjLNd7GfU7wMoDA5RakpWbzHEodikdik9NHuMW"), encoding='jsonParsed')
    key = PublicKey.find_program_address(
        [bytes("metadata", encoding='ascii'), bytes(PublicKey('metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s')),bytes(PublicKey('9eohkfSjLNd7GfU7wMoDA5RakpWbzHEodikdik9NHuMW'))], PublicKey('metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s'))
    info = http_client.get_account_info(PublicKey(key[0]))
    d = info['result']['value']['data']
    data = b64decode(d[0])
    metadata = unpack_metadata_account(data)
    a = 1

def unpack_metadata_account(data):
    assert(data[0] == 4)
    i = 1
    source_account = base58.b58encode(bytes(struct.unpack('<' + "B"*32, data[i:i+32])))
    i += 32
    mint_account = base58.b58encode(bytes(struct.unpack('<' + "B"*32, data[i:i+32])))
    i += 32
    name_len = struct.unpack('<I', data[i:i+4])[0]
    i += 4
    name = struct.unpack('<' + "B"*name_len, data[i:i+name_len])
    i += name_len
    symbol_len = struct.unpack('<I', data[i:i+4])[0]
    i += 4 
    symbol = struct.unpack('<' + "B"*symbol_len, data[i:i+symbol_len])
    i += symbol_len
    uri_len = struct.unpack('<I', data[i:i+4])[0]
    i += 4 
    uri = struct.unpack('<' + "B"*uri_len, data[i:i+uri_len])
    i += uri_len
    fee = struct.unpack('<h', data[i:i+2])[0]
    i += 2
    has_creator = data[i] 
    i += 1
    creators = []
    verified = []
    share = []
    if has_creator:
        creator_len = struct.unpack('<I', data[i:i+4])[0]
        i += 4
        for _ in range(creator_len):
            creator = base58.b58encode(bytes(struct.unpack('<' + "B"*32, data[i:i+32])))
            creators.append(creator)
            i += 32
            verified.append(data[i])
            i += 1
            share.append(data[i])
            i += 1
    primary_sale_happened = bool(data[i])
    i += 1
    is_mutable = bool(data[i])
    metadata = {
        "update_authority": source_account,
        "mint": mint_account,
        "data": {
            "name": bytes(name).decode("utf-8").strip("\x00"),
            "symbol": bytes(symbol).decode("utf-8").strip("\x00"),
            "uri": bytes(uri).decode("utf-8").strip("\x00"),
            "seller_fee_basis_points": fee,
            "creators": creators,
            "verified": verified,
            "share": share,
        },
        "primary_sale_happened": primary_sale_happened,
        "is_mutable": is_mutable,
    }
    return metadata

