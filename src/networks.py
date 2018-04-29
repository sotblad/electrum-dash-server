# Main network and testnet3 definitions

# Dash src/chainparams.cpp
params = {
    'dash_main': {
        'pubkey_address': 16, #L120
        'script_address': 76, #L122
        'genesis_hash': '000002acd994a815401fbaae0e52404b32857efd0b7b0c77b8e0715ccdd6d437' #L110
    },
    'dash_test': {
        'pubkey_address': 140, #L220
        'script_address': 19, #L222
        'genesis_hash': '00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c' #L210
    }
}
