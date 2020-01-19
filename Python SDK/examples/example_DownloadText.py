#!/usr/bin/env python
#
# Copyright (C) SlashNext, Inc. (www.slashnext.com)
#
# License:     Subject to the terms and conditions of SlashNext EULA, SlashNext grants to Customer a non-transferable,
#              non-sublicensable, non-exclusive license to use the Software as expressly permitted in accordance with
#              Documentation or other specifications published by SlashNext. The Software is solely for Customer's
#              internal business purposes. All other rights in the Software are expressly reserved by SlashNext.
#

"""
Created on January 16, 2020

Contains an example of the SlashNextDownloadScreenshot usage from SlashNextPhishingIR module.

@author: Saadat Abid
"""
from SlashNextPhishingIR import SlashNextDownloadText

download_text_action = SlashNextDownloadText(
    api_key="this_is_a_valid_api_key",
    base_url="https://oti.slashnext.cloud/api"
)

action_name = download_text_action.name()
action_title = download_text_action.title()
action_description = download_text_action.description()
action_parameters = download_text_action.parameters()
action_help = download_text_action.help()
response_details, response_list = download_text_action.execution(scanid='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')
