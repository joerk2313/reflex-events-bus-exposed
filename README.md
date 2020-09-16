# reflex-events-bus-exposed

TODO: Write a brief description of your rule and what it does.

## Usage

To use this rule either add it to your `reflex.yaml` configuration file:

```
rules:
  - reflex-events-bus-exposed:
      version: latest
```

or add it directly to your Terraform:

```
...

module "reflex-events-bus-exposed" {
  source           = "github.com/joerk2313/reflex-events-bus-exposed"
}

...
```

## License

This Reflex rule is made available under the MPL 2.0 license. For more information view
the [LICENSE](https://github.com/joerk2313/reflex-events-bus-exposed/blob/master/LICENSE)