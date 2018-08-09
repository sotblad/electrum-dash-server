# Main network and testnet3 definitions

# MonetaryUnit src/chainparams.cpp
params = {
    'mue_main': {
        'pubkey_address': 76, #L120
        'script_address': 16, #L122
        'genesis_hash': '000002acd994a815401fbaae0e52404b32857efd0b7b0c77b8e0715ccdd6d437' #L110
    },
    'mue_test': {
        'pubkey_address': 19, #L220
        'script_address': 38, #L222
        'genesis_hash': '00000c4e1485ee323e0dfab3c8afa871ceceff8822b9abe68005e22576d47a6f' #L210
    }
}
