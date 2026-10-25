Scaffold of `.claudeignore` at the root. Write the content between the two markers as it is. Add as comments any private folders the person mentioned (none by default).

FILE START

# Files and folders that AI must NOT read.
# One path per line. Lines starting with # are comments.

# Generated files, useless to read (map of the notes, task board)
graph.html
board.html

# Secrets and access
.env
.env.*
*.key
*.pem
secrets/
access/

# Identity and bank documents (never put them in this folder)
id-scans/
cin/
rib/
bank/

# Personal data of clients
private-clients/
client-contacts/

# Private folders: remove the # in front of the line to activate
# private/
# health/
# family/
# personal-finance/

FILE END
