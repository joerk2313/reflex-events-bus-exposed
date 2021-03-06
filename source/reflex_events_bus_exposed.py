""" Module for ReflexEventsBusExposed """

import json
import os

import boto3
from reflex_core import AWSRule


class ReflexEventsBusExposed(AWSRule):
    """ TODO: A description for your rule """

    # TODO: Instantiate whatever boto3 client you'll need, if any.
    # Example:
    # client = boto3.client("s3")

    def __init__(self, event):
        super().__init__(event)

    def extract_event_data(self, event):
        """ Extract required event data """
        # TODO: Extract any data you need from the triggering event.
        #
        # Example:
        # self.bucket_name = event["detail"]["requestParameters"]["bucketName"]

    def resource_compliant(self):
        """
        Determine if the resource is compliant with your rule.

        Return True if it is compliant, and False if it is not.
        """
        # TODO: Implement a check for determining if the resource is compliant

    def get_remediation_message(self):
        """ Returns a message about the remediation action that occurred """
        # TODO: Provide a human readable message describing what occured. This
        # message is sent in all notifications.
        #
        # Example:
        # return f"The S3 bucket {self.bucket_name} was unencrypted. AES-256 encryption was enabled."


def lambda_handler(event, _):
    """ Handles the incoming event """
    rule = ReflexEventsBusExposed(json.loads(event["Records"][0]["body"]))
    rule.run_compliance_rule()