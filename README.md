# An Example of interacting with peaq-did-pallet
## An example python app demonstrating how to create and access DID attributes on the peaq network.
---
## Throughout the samples, following accounts have been used

> Owing account
```
Secret phrase:       strong need allow car sunny visual dog grab slam adjust pave illegal
  Secret seed:       0x903860c395a76e303188b319dc0f505d69c700c73ae9adb63c3d5c7f323d6ad9
  Public key (hex):  0xdca00ab130cb7123991f8404f2dbe2343e83b0a2b4d07b9ee1babd89b760bb29
  Account ID:        0xdca00ab130cb7123991f8404f2dbe2343e83b0a2b4d07b9ee1babd89b760bb29
  Public key (SS58): 5H3yw8fj3Vz1uFcPzQj8Cy5owo8dZZkZrN68hx1JBSah6Gy2
  SS58 Address:      5H3yw8fj3Vz1uFcPzQj8Cy5owo8dZZkZrN68hx1JBSah6Gy2
```

> DID account
```
did account
Secret phrase:       inmate shift pact lawsuit chapter drama bracket hawk bullet alone news vacuum
  Secret seed:       0xba69fe40f57ad78c7fd6bc1dd5b2693de00b36416525647b14d10fe6b09d983f
  Public key (hex):  0x6031188a7c447201a20c044b5e93a6857683a0186a2e02c799974c94a6e4331d
  Account ID:        0x6031188a7c447201a20c044b5e93a6857683a0186a2e02c799974c94a6e4331d
  Public key (SS58): 5EEq3C8tBC7UBiaZJX2nXUiNyhPqyDtv8ZFC8xHp4GcEyRfW
  SS58 Address:      5EEq3C8tBC7UBiaZJX2nXUiNyhPqyDtv8ZFC8xHp4GcEyRfW
```

# Requirements & Environment setup
After checking out the repository, issue the following command on bash shell

```bash
pip3 install virtualenv && \
virtualenv venv && \
source venv/bin/activate && \
pip3 install -r requirements.txt
```

# Prerequisites
Ensure some tokens have been transferred to the owing account [5H3yw8fj3Vz1uFcPzQj8Cy5owo8dZZkZrN68hx1JBSah6Gy2]

# Creating a DID attribute
The following command adds an attribute "id" for the did [`0x6031188a7c447201a20c044b5e93a6857683a0186a2e02c799974c94a6e4331d`] owed by [`0xdca00ab130cb7123991f8404f2dbe2343e83b0a2b4d07b9ee1babd89b760bb29`]
```bash
python3 create_attr.py
```

Upon successful execution output similar to following is emitted
```
Extrinsic "0xd10deea1a1558ffb8b3a9a333b181638b2a954a9d5562afdbe9cbdfbb03dc1e4" included in block "0x3fb4288a83af81cd72f939c0ca9d2e8dd4b45219f4d1eb125453e4ab9a586cbc"
Success, triggered events:
* {'phase': 'ApplyExtrinsic', 'extrinsic_idx': 1, 'event': {'event_index': '0900', 'module_id': 'PeaqDid', 'event_id': 'AttributeAdded', 'attributes': ('0xdca00ab130cb7123991f8404f2dbe2343e83b0a2b4d07b9ee1babd89b760bb29', '0xf01936fb4d5b5bb02a6adcba51142f7c4fdf66f453b2adcae7b7f8d3c6267829', 'id1', '456734', None)}, 'event_index': 9, 'module_id': 'PeaqDid', 'event_id': 'AttributeAdded', 'attributes': ('0xdca00ab130cb7123991f8404f2dbe2343e83b0a2b4d07b9ee1babd89b760bb29', '0xf01936fb4d5b5bb02a6adcba51142f7c4fdf66f453b2adcae7b7f8d3c6267829', 'id1', '456734', None), 'topics': []}
* {'phase': 'ApplyExtrinsic', 'extrinsic_idx': 1, 'event': {'event_index': '0000', 'module_id': 'System', 'event_id': 'ExtrinsicSuccess', 'attributes': {'weight': 1000, 'class': 'Normal', 'pays_fee': 'Yes'}}, 'event_index': 0, 'module_id': 'System', 'event_id': 'ExtrinsicSuccess', 'attributes': {'weight': 1000, 'class': 'Normal', 'pays_fee': 'Yes'}, 'topics': []}
```

And, on failure the output is similar to following
```
Extrinsic "0x9fc7e0940aae7a9c43447d75fb9d25fdc7aa5ad7b1881cea66c82aa78f82afac" included in block "0x30827f986aaa8c0bf4a94bf613924742d4c28d95a7fc0979cab1da182ab05138"
Extrinsic Failed:  None
```


# Reading a DID attribute
The following command reads the previously added attribute from chain state

```
python3 read_attr_cs.py
```

A successful execution looks similar to following
```
acc_pk: b'6031188a7c447201a20c044b5e93a6857683a0186a2e02c799974c94a6e4331d'
attr_to_read: b'6964'
data_to_hash: b'6031188a7c447201a20c044b5e93a6857683a0186a2e02c799974c94a6e4331d6964'
unhashed key for map: [01621935bef7de2129d77df46f9fc533054dbc82b03df3f4f0ac1ebeab878919]
pallet_hash [50b1bab256dbd966f3aa4c23d3a7a201]
storage_hash [77fe881efb890ea5c9aede80c0d3a143]
key_hash [28095006ceffd88dbf9a2bf8f5e9bb0c01621935bef7de2129d77df46f9fc533054dbc82b03df3f4f0ac1ebeab878919]
storage_key: [50b1bab256dbd966f3aa4c23d3a7a20177fe881efb890ea5c9aede80c0d3a14328095006ceffd88dbf9a2bf8f5e9bb0c01621935bef7de2129d77df46f9fc533054dbc82b03df3f4f0ac1ebeab878919]
de1e86a9a8c739864cf3cc5ec2bea59fd43593c715fdd31c61141abd04a99fd6822c8558854ccde39a5684e7a56da27d
Raw result: [0x08696418343536373334ffffffff41630b787d010000]
{'name': 'id', 'value': '456734', 'validity': 4294967295, 'created': 1638396552001}
```

# Detailed explanation of code

## Creating an attribute

Creating attributes is straight forward, a call is composed

```python
call = substrate.compose_call(
call_module='PeaqDid',
call_function='add_attribute',
call_params={
    'did_account': '5EEq3C8tBC7UBiaZJX2nXUiNyhPqyDtv8ZFC8xHp4GcEyRfW',
    'name': 'id',
    'value': '456734',
    'valid_for': None
    }
)
```

and then the extrinsic is invoked to include it onto the block

```python
xtrinsic = substrate.create_signed_extrinsic(
    call=call, 
    keypair=keypair,
    era={'period': 64},
    nonce=nonce
)

receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)

print('Extrinsic "{}" included in block "{}"'.format(
    receipt.extrinsic_hash, receipt.block_hash
))
```

On success, the result is parsed to iterate over generated event as part of executing the extrinsic

```python
if receipt.is_success:

    print('Success, triggered events:')
    for event in receipt.triggered_events:
        print(f'* {event.value}')

else:
    print('Extrinsic Failed: ', receipt.error_message)

```



## Understanding how storage queries work

Applications requiring quick access to data need a way to instantly access the stored information on the blockchain. Substrate organizes this information with help of a trie structure which uses hashed keys to index into the tree.

A general rpc method is exposed by the substrate node to allow callers to query the storage which bears the following signature

```
getStorage(key: StorageKey, block?: Hash): StorageData
```

In the above signature, key represents a hash which we will discuss below and block is an optional parameter which if given queries the trie for the hash at the given block number.

key hashes are data structure dependent and are calculated by concatenating hashes of the name of pallet/module, data store and a key into the data structure. Shawn Tabrizi [3] explains it with the help of following

For storage values

```python
xxhash128("ModuleName") + xxhash128("StorageName")
```

For storage maps

```python
  xxhash128("ModuleName") + xxhash128("StorageName") + blake256hash("StorageItemKey")
```

For storage double maps

```python
xxhash128("ModuleName") + xxhash128("StorageName") + blake256hash("FirstKey") + blake256hash("SecondKey")
```



With this limited introduction let&#39;s see how we can calculate the hash and query the chain state. We will use peaqDID pallet as an example here because it uses a storage map and defines a custom data type which is the value in the map.

Assuming we use the polkadotJS app to invoke the addAttribute extrinsic with the following data and that the data is included in the block and stored on the chain

```
didAccount: 6031188a7c447201a20c044b5e93a6857683a0186a2e02c799974c94a6e4331d
name: 0x6964
value: 0x456734
```

Let&#39;s first query the chain state using polkadotJS apps which requires a hash in order to query the data. In this case we have to calculate the &quot;key&quot; of the map that is used by peaqDid pallet. If we take a look at the corresponding code that is responsible for generating this key it is as follows

```
fn get_hashed_key_for_attr(
			did_account: &T::AccountId,
			name: &[u8]
		) -> [u8; 32] {

			let mut bytes_in_name: Vec<u8> = name.to_vec();
			let mut bytes_to_hash: Vec<u8> = did_account.encode().as_slice().to_vec();
			bytes_to_hash.append(&mut bytes_in_name);
			blake2_256(&bytes_to_hash[..])
		}
```

The function takes as in put the public key of the contract and the name of the attribute we are interested in storing. We can see from the algorithm that we need to take the blake2_256 hash of byte array formed by combining the public key and attribute name, the raw bytes array equates to

```
6031188a7c447201a20c044b5e93a6857683a0186a2e02c799974c94a6e4331d6964
```

And the hashed 32 byte output becomes

```
01621935bef7de2129d77df46f9fc533054dbc82b03df3f4f0ac1ebeab878919
```

If we just take the above hashed key and use polkadotjs chain state explorer we can successfully query the storage, as shown below

![](https://static.slab.com/prod/uploads/yhh6vv2m/posts/images/6QTeMAFpmlip-_TMG8HbkC1i.png)

Referring back to Shaw&#39;s explanation on how the keys are constructed, polkadotjs takes care of everything for us given we provide it with the key.

To do the same programmatically using python we would go about it as follows

```python
# Get byte data and calculate the key's hash as per the algo used in peaqDid pallet
acc_pk = bytearray.fromhex("6031188a7c447201a20c044b5e93a6857683a0186a2e02c799974c94a6e4331d")
attr_to_read = bytes("id",encoding='utf8')
data_to_hash = acc_pk + attr_to_read
hashed_val_of_key_in_map = hasher.blake2_256(data_to_hash)

# Calculate the storage hash
pallet_hash = hasher.xxh128("PeaqDid")
storage_hash = hasher.xxh128("AttributeStore")
# notice here how we are again hashing the key as per the 
# hasher used in the storage map's declaration in peaqDid pallet
hashed_val_of_key_in_map = bytearray.fromhex(hashed_val_of_key_in_map)
key_hash = hasher.blake2_128_concat(hashed_val_of_key_in_map)
storage_key = pallet_hash +  storage_hash + key_hash

result = substrate.get_storage_by_key(
    None,
    storage_key
)
```

result will contain None if no associated data is found on the chain or a &quot;scale&quot; encoded value which we will need to decode.



### Decoding scale encoded custom data

Custom types can be given to the scale codec to decode returned data. Custom types are defined using json on the client side, for instance for our custom type value of Attribute which we store in the map on peaqDid pallet, it would be declared as follows

```python
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
```

Eventually the following python code uses the above declaration to decode the earlier read value from chain in a human friendly way

```python
    RuntimeConfiguration().update_type_registry(custom_types)

    obj = RuntimeConfiguration().create_scale_object('Attribute', data=ScaleBytes(result))
    obj.decode()
```

## References

### Docs

1. [https://docs.substrate.io/v3/advanced/storage/](https://docs.substrate.io/v3/advanced/storage/)
1. [https://docs.substrate.io/v3/advanced/scale-codec/#data-structures](https://docs.substrate.io/v3/advanced/scale-codec/#data-structures)
1. [https://www.shawntabrizi.com/substrate/querying-substrate-storage-via-rpc/](https://www.shawntabrizi.com/substrate/querying-substrate-storage-via-rpc/)
1. [https://www.shawntabrizi.com/substrate/transparent-keys-in-substrate/](https://www.shawntabrizi.com/substrate/transparent-keys-in-substrate/)
1. [https://docs.rs/parity-scale-codec/latest/parity_scale_codec/](https://docs.rs/parity-scale-codec/latest/parity_scale_codec/)
1. [https://docs.substrate.io/v3/runtime/debugging/](https://docs.substrate.io/v3/runtime/debugging/)
1. [https://polkascan.github.io/py-scale-codec/types.html#scalecodec.types.Bytes](https://polkascan.github.io/py-scale-codec/types.html#scalecodec.types.Bytes)

### Code

1. [https://github.com/polkascan/py-scale-codec](https://github.com/polkascan/py-scale-codec)
1. [https://docs.python.org/3/library/hashlib.html#hashlib.blake2b](https://docs.python.org/3/library/hashlib.html#hashlib.blake2b)
1. [https://github.com/polkascan/py-substrate-interface/blob/master/substrateinterface/utils/hasher.py](https://github.com/polkascan/py-substrate-interface/blob/master/substrateinterface/utils/hasher.py)
1. [https://github.com/polkascan/py-substrate-interface/issues/3](https://github.com/polkascan/py-substrate-interface/issues/3)  
1. [https://github.com/polkascan/py-scale-codec/blob/master/test/test_type_encoding.py](https://github.com/polkascan/py-scale-codec/blob/master/test/test_type_encoding.py)
1. [https://github.com/polkascan/py-substrate-interface/blob/master/substrateinterface/base.py](https://github.com/polkascan/py-substrate-interface/blob/master/substrateinterface/base.py)
1. [https://github.com/polkascan/py-substrate-interface/blob/master/examples/balance_transfer.py](https://github.com/polkascan/py-substrate-interface/blob/master/examples/balance_transfer.py)
1. [https://github.com/polkascan/py-substrate-interface/blob/master/substrateinterface/base.py](https://github.com/polkascan/py-substrate-interface/blob/master/substrateinterface/base.py)
