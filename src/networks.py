# Main network and testnet3 definitions

params = {
    'dash_main': {
        'pubkey_address': 76, #Dash src/chainparams.cpp L169
        'script_address': 16, #Dash src/chainparams.cpp L170
        'genesis_hash': '00000ffd590b1485b3caadc19b22e6379c733355108f107a430458cdf3407ab6' #Darkcoin src/chainparams.cpp L161 
    },
    'dash_test': {
        'pubkey_address': 139, #Dash src/chainparams.cpp L238
        'script_address': 19, #Dash src/chainparams.cpp L239
        'genesis_hash': '00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c' #Darkcoin src/chainparams.cpp L227
    }
}
