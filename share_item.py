import asyncio
import os
from onepassword import *

async def main():
    # Gets your service account token from the OP_SERVICE_ACCOUNT_TOKEN environment variable.
    token = os.getenv("OP_SERVICE_ACCOUNT_TOKEN")
    vault_id = os.getenv("OP_VAULT_ID")
    item_id = os.getenv("OP_ITEM_ID_TO_SHARE")

    user_email = []
    if "USER_EMAIL" in os.environ:
        user_email = [os.getenv("USER_EMAIL")]

    # Connects to 1Password. Fill in your own integration name and version.
    client = await Client.authenticate(auth=token, integration_name="Phils CICD Share Workflow Demo for Blog", integration_version="v0.0.1")

    # Get the Item to share
    item = await client.items.get(vault_id, item_id)
    print("Item: ", item, "\n")

    # Get the account policy for the item
    policy = await client.items.shares.get_account_policy(item.vault_id, item.id)
    print("Policy: ", policy, "\n")

    # Create a record policy for valid recipients
    valid_recipients = await client.items.shares.validate_recipients(
        policy, user_email # This could be an email address in quotes.
    )

    # Debut the recipients
    print("Valid Recipients: ", valid_recipients,"\n")


    # Create the link to share
    share_link = await client.items.shares.create(
        item,
        policy,
        ItemShareParams(
            recipients=valid_recipients,
            expireAfter=ItemShareDuration.ONEHOUR,
            oneTimeOnly=True,
        ),
    )

    print("\n\nShare URL: ", share_link, "\n")

    # Now return the value to the OS / GitHub Workflow
    with open(os.environ["OP_SHARE_LINK"], "a") as fh:
        print(f"{share_link}", file=fh)


if __name__ == '__main__':
    asyncio.run(main())