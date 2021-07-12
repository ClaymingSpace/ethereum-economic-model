import data.api as api


def test_beaconchain():
    assert api.beaconchain.get_epoch_data().get("totalvalidatorbalance", False)
    assert api.beaconchain.get_total_validator_balance(default=1) > 0
    assert api.beaconchain.get_validators_count(default=1) > 0

def test_etherscan():
    assert api.etherscan.get_eth_supply(default=1) > 0