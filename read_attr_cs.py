import binascii

from substrateinterface import SubstrateInterface
from substrateinterface.utils import hasher

from scalecodec.base import ScaleBytes, RuntimeConfiguration
from scalecodec.type_registry import load_type_registry_preset
  

acc_pk = bytearray.fromhex("6031188a7c447201a20c044b5e93a6857683a0186a2e02c799974c94a6e4331d")
print("acc_pk: {}".format(binascii.hexlify(acc_pk)))

attr_to_read = bytes("id",encoding='utf8')
print("attr_to_read: {}".format(binascii.hexlify(attr_to_read)))

data_to_hash = acc_pk + attr_to_read
print("data_to_hash: {}".format(binascii.hexlify(data_to_hash)))

hashed_val_of_key_in_map = hasher.blake2_256(data_to_hash)
print("unhashed key for map: [{}]".format(hashed_val_of_key_in_map))

substrate = SubstrateInterface(
    url='ws://127.0.0.1:9944',
)

pallet_hash = hasher.xxh128("PeaqDid")
print("pallet_hash [{}]".format(pallet_hash))

storage_hash = hasher.xxh128("AttributeStore")
print("storage_hash [{}]".format(storage_hash))

#shadow hashed_val_of_key_in_map
hashed_val_of_key_in_map = bytearray.fromhex(hashed_val_of_key_in_map)
key_hash = hasher.blake2_128_concat(hashed_val_of_key_in_map)
print("key_hash [{}]".format(key_hash))

storage_key = pallet_hash +  storage_hash + key_hash
print("storage_key: [{}]".format(storage_key))

print(hasher.blake2_128_concat(bytearray.fromhex("d43593c715fdd31c61141abd04a99fd6822c8558854ccde39a5684e7a56da27d")))

result = substrate.get_storage_by_key(
    None,
    storage_key
)
#Print raw result
print("Raw result: [{}]".format(result))

if result is not None:
    RuntimeConfiguration().update_type_registry(load_type_registry_preset("default"))

    custom_types = {
        "types": {
            "Attribute": {
            "type": "struct",
            "type_mapping": [
                ["name", "string"],
                ["value", "string"],
                ["validity", "BlockNumber"],
                ["created", "Moment"],
            ]
            }
        }   
    }
    RuntimeConfiguration().update_type_registry(custom_types)

    obj = RuntimeConfiguration().create_scale_object('Attribute', data=ScaleBytes(result))
    obj.decode()
    print(obj.value)

