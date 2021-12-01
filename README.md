# example-did-interfacing
## An example python app demonstrating how to create and access DID attributes.
---
# Throughout the samples, following accounts have been used

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