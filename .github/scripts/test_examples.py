import json
import unittest
from html.parser import HTMLParser
from pathlib import Path

import markdown

from generate_catalog import EXAMPLES, ROOT


def template(path):
    return json.loads((ROOT / "build" / path).read_text(encoding="utf-8"))


def resource(document, resource_type):
    matches = [item for item in document["resources"] if item["type"] == resource_type]
    if len(matches) != 1:
        raise AssertionError(f"Expected exactly one {resource_type}, got {len(matches)}")
    return matches[0]


class TableRows(HTMLParser):
    def __init__(self):
        super().__init__()
        self.body = False
        self.rows = 0

    def handle_starttag(self, tag, attrs):
        if tag == "tbody":
            self.body = True
        if tag == "tr" and self.body:
            self.rows += 1

    def handle_endtag(self, tag):
        if tag == "tbody":
            self.body = False


class CompiledExamples(unittest.TestCase):
    def test_private_storage_contract(self):
        account = resource(template("modules/private-storage/main.json"), "Microsoft.Storage/storageAccounts")
        properties = account["properties"]
        self.assertEqual(properties["publicNetworkAccess"], "Disabled")
        self.assertIs(properties["allowSharedKeyAccess"], False)
        self.assertIs(properties["allowBlobPublicAccess"], False)
        self.assertIs(properties["supportsHttpsTrafficOnly"], True)
        self.assertEqual(properties["minimumTlsVersion"], "TLS1_2")

    def test_network_attaches_default_deny(self):
        document = template("modules/isolated-network/main.json")
        nsg = resource(document, "Microsoft.Network/networkSecurityGroups")
        rule = nsg["properties"]["securityRules"][0]["properties"]
        self.assertEqual((rule["direction"], rule["access"], rule["priority"]), ("Inbound", "Deny", 4096))
        network = resource(document, "Microsoft.Network/virtualNetworks")
        self.assertIn("networkSecurityGroups", network["properties"]["subnets"][0]["properties"]["networkSecurityGroup"]["id"])
        self.assertTrue(network["dependsOn"])

    def test_foundation_scopes_modules_to_created_group(self):
        document = template("examples/03-modular-foundation/main.json")
        self.assertIn("subscriptionDeploymentTemplate", document["$schema"])
        group = resource(document, "Microsoft.Resources/resourceGroups")
        deployments = [item for item in document["resources"] if item["type"] == "Microsoft.Resources/deployments"]
        self.assertEqual(len(deployments), 2)
        for deployment in deployments:
            self.assertEqual(deployment["resourceGroup"], group["name"])
            self.assertTrue(any("Microsoft.Resources/resourceGroups" in item for item in deployment["dependsOn"]))
            self.assertTrue(deployment["properties"]["template"]["resources"])

    def test_language_example_creates_no_workloads(self):
        document = template("examples/02-language/main.json")
        self.assertEqual(len(document["resources"]), 0)
        self.assertEqual(document["parameters"]["environment"]["allowedValues"], ["dev", "test", "prod"])

    def test_environment_files_compile_with_distinct_labels(self):
        for environment in ("dev", "prod"):
            parameters = template(f"examples/03-modular-foundation/{environment}.json")["parameters"]
            self.assertEqual(parameters["environment"]["value"], environment)
            self.assertEqual(parameters["storageAccountName"]["value"], "stbicepoverviewci")

    def test_catalog_renders_every_source_as_a_real_row(self):
        parser = TableRows()
        parser.feed(markdown.markdown((ROOT / "docs/catalog.md").read_text(encoding="utf-8"), extensions=["tables"]))
        self.assertEqual(parser.rows, len(EXAMPLES))


if __name__ == "__main__":
    unittest.main()
