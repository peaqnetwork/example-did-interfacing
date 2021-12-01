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
call_function='add_attribute',
call_params={
    'did_account': '5EEq3C8tBC7UBiaZJX2nXUiNyhPqyDtv8ZFC8xHp4GcEyRfW',
    'name': 'id',
    'value': '456734',
    'valid_for': None
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

    print('Success, triggered events:')
    for event in receipt.triggered_events:
        print(f'* {event.value}')

else:
    print('Extrinsic Failed: ', receipt.error_message)
