from scripts.helpful_scripts import get_account
from brownie import SimpleCollectible

sample_token_uri = 'https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json'
OPENSEA_URL = 'https://testnets.opensea.io/assets/{}/{}'


def deploy_simple_collectible():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({'from': account})


def create_simple_collectible():
    account = get_account()
    simple_collectible = SimpleCollectible[-1]
    tx = simple_collectible.createCollectible(sample_token_uri, {'from': account})
    tx.wait(1)
    print(
        f'Awesome, you can see your NFT at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}')


def main():
    deploy_simple_collectible()
    create_simple_collectible()
