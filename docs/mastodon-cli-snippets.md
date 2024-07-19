# Mastodon CLI Snippets

```bash

# adding a user
RAILS_ENV=production /home/mastodon/live/bin/tootctl accounts create ${NAME} --email ${EMAIL} --confirmed --force

# removing a user
RAILS_ENV=production /home/mastodon/live/bin/tootctl accounts delete ${NAME}
```
