# Generate Gmail XML filters import file from list of emails, mark it as `read` and assign some label

Simple utility written on python with no deps.

## Why it might be useful?

This utility helps to avoid distraction by unnecessary notifications from Email app.

Just create your own `addresses.txt` with list of unimportant emails and generate XML file 
suitable for import into gmail filters list.

Gmail will automatically mark matching emails as `Read`,
so no notifications for new emails should appears.

### Usage example:

Create your `addresses.txt` with contents like:
```
# Promos
promo@example.com
promo@test.com

# Subs
sub@sub.com
```

> empty lines and lines with starting `#` are ignored

(update `unimportant_label` variable in beginning of `gmail.py` with your preffered label for unimportant mail)

(also, you probably want to replace XML file heading with your own data, so, go for it)

```shell
cat addresses.txt | ./gmail.py > rules.xml
```

Then, go to https://mail.google.com/mail/u/0/#settings/filters and import resulting `rules.xml`

