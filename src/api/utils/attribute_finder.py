from solana.rpc.api import Client
from solana.publickey import PublicKey
import base58
from base64 import b64decode
import struct
import urllib.request
import json

http_client = Client("https://solana-api.projectserum.com")

def get_nft_info(mint): 
    orcanaut = {}
    key = PublicKey.find_program_address(
        [bytes("metadata", encoding='ascii'), bytes(PublicKey('metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s')),bytes(PublicKey(mint))], PublicKey('metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s'))
    info = http_client.get_account_info(PublicKey(key[0]))
    d = info['result']['value']['data']
    data = b64decode(d[0])
    metadata = unpack_metadata_account(data)
    uri = metadata['data']['uri']
    with urllib.request.urlopen(uri) as response:
        html = response.read()
        s = html.decode("utf-8")
        obj = json.loads(s)
        assert(obj['name'].startswith('Orcanauts'))
        for att in obj['attributes']:
            orcanaut[att['trait_type']] = att['value'].lower().replace(' ','_')
    return orcanaut


# https://github.com/metaplex-foundation/python-api/blob/441c2ba9be76962d234d7700405358c72ee1b35b/metaplex/metadata.py#L180
#
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

