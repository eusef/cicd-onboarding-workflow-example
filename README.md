# cicd-onboarding-workflow-example

This is a working project showing how a system administrator can temporarily provide access to credentials stored within 1Password and then distribute those credentials using Slack.

The corresponding blog post will be published and this README will be updated with a link.




To run the share_item.py you need to set a few environment variables for testing.  Otherwise they are set within GitHub

OP_VAULT_ID= #required and available in 1Password UI
OP_ITEM_ID_TO_SHARE= # required and available in 1Password UI
OP_SHARE_LINK=./my_local_output.txt # only used for local testing
USER_EMAIL= #unset will generate a URL without email verification