# Imenik

A really simple function that takes in a phone number and returns the caller ID.

**Live Instance**: https://imenik.elahmo.now.sh/

## How to use

Make a post request to `https://imenik.elahmo.now.sh/` with `number` as payload,
and if the number is available in the providers' database, it will be returned.

## Supported operators

The list of supported operators is as follows:

- BHTelecom

## Contributing

Please feel free to add any operator or improve the code in any way by opening
a PR.

In particular, the addition of new operators, optimisations and a simple GUI would 
be helpful.

## Using via CLI

Initially, this was made for my specific use case, I wanted to quickly know a
caller ID before I pick up the phone, as I receive a lot of spammy calls.

It might be useful to have this as a simple `curl` call:

`curl -d "number=000000000" -X POST https://imenik.elahmo.now.sh`

or saved as a function in your `.bashrc` file:
```bash
function imenik() {
    local number=$1

    curl -d "number=$number" -X POST https://imenik.elahmo.now.sh
}
```

This enables a quick `imenik 123123123` lookup from the CLI of your choice.


Then, for production, including automatic aliasing, you can use the following:

## Development and Deployment

The code is automatically deployed to [now](http://now.sh) and the details are 
specified in the `now.json`, specifying the build process and routing.

For local development and simulation of dev environment, use `now dev`.

As some might call this approach serverless, there are some drawbacks. Cold boot
lookup takes ~ 5 seconds, otherwise, the results are returned within 2-3 seconds. 
It seems inconvenient to do the lookup in one call for BHTelecom, so two
requests are made, one to get the session and second to actually request the
number lookup.