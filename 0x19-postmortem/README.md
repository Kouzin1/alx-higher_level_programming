# Postmortem

Upon the release of ALX's System Engineering & DevOps project 0x19, approximately 06:00 West African Time (WAT) here in
Nigeria, an outage occerred on an isolated Ubuntu 14.04 container running an Apache web web server. GET requests on the server led to `500 Internal Server Error`'s, when the expected response was an HTML file defining a simple Holberton WordPress site.

## Debugging Process

Bug debuger Brennan (BDB... as in my actual initials... made that up on the spot, pretty good, huh?) encountered the issue upon 
opening the project and being, well, instructed to address it, roughly 19:20 PST. He promptly proceeded to undergo solving the problem.
