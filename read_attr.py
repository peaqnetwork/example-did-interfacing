from substrateinterface import SubstrateInterface, Keypair, KeypairType

substrate = SubstrateInterface(
            url='ws://127.0.0.1:9944',
        )

keypair = Keypair.create_from_mnemonic(
    'strong need allow car sunny visual dog grab slam adjust pave illegal',
    ss58_format=42,
    crypto_type=KeypairType.SR25519)

nonce = substrate.get_account_nonce(keypair.ss58_address)

call = substrate.compose_call(
call_module='PeaqDid',
call_function='read_attribute',
call_params={
    'did_account': '5EEq3C8tBC7UBiaZJX2nXUiNyhPqyDtv8ZFC8xHp4GcEyRfW',
    'name': 'id'
    }
)   

extrinsic = substrate.create_signed_extrinsic(
    call=call, 
    keypair=keypair,
    era={'period': 64},
    nonce=nonce
)

receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)

print('Extrinsic "{}" included in block "{}"'.format(
    receipt.extrinsic_hash, receipt.block_hash
))

if receipt.is_success:

    print('✅ Success, triggered events:')
    for event in receipt.triggered_events:
        print(f'* {event.value}')

else:
    print('⚠️ Extrinsic Failed: ', receipt.error_message)

## Success output
# Extrinsic "0xf8ddf0295b450196cb9a8eb6ea69c2f5e49b7fb97992c315a7400fe69a057a04" included in block "0xff4a60403cd4da82045f3a0bd90ee69c9bd10327cecc23145b3527d25cda6aae"
# ✅ Success, triggered events:
# * {'phase': 'ApplyExtrinsic', 'extrinsic_idx': 1, 'event': {'event_index': '0901', 'module_id': 'PeaqDid', 'event_id': 'AttributeRead', 'attributes': {'name': 'id1', 'value': '456734', 'validity': 4294967295, 'created': 1638361572001}}, 'event_index': 9, 'module_id': 'PeaqDid', 'event_id': 'AttributeRead', 'attributes': {'name': 'id1', 'value': '456734', 'validity': 4294967295, 'created': 1638361572001}, 'topics': []}
# * {'phase': 'ApplyExtrinsic', 'extrinsic_idx': 1, 'event': {'event_index': '0000', 'module_id': 'System', 'event_id': 'ExtrinsicSuccess', 'attributes': {'weight': 1000, 'class': 'Normal', 'pays_fee': 'Yes'}}, 'event_index': 0, 'module_id': 'System', 'event_id': 'ExtrinsicSuccess', 'attributes': {'weight': 1000, 'class': 'Normal', 'pays_fee': 'Yes'}, 'topics': []}

## Failure output
# Extrinsic "0xc5a77d449f7b55e84b99b4d868a2f39589b08c55d3747d8595aad5a52fd09591" included in block "0x5b503594b969ee57b4a22b56861cf918977e4a98397b4dff672011c06e4c289c"
# ⚠️ Extrinsic Failed:  None