# Magic 8 ball microservice

A simple microservice for testing infrastructure.

## Endpoints

### `/`

Returns a Magic 8 ball reply in the format:

``` json
{
    "connotation": "positive",
    "response": "Outlook good."
}
```

### `/ping`

Returns a simple 200 response. Designed for health checks.

### `/ping/<text>`

Returns a simple 200 response with `<text>` in the response body. Designed for
health checks that bypass caching layers.
