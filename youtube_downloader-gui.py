from src import application as app

# run in console if new translations are includes:
# msgfmt -o i18n/de/LC_MESSAGES/messages.mo i18n/de/LC_MESSAGES/messages.po
# msgfmt -o i18n/en/LC_MESSAGES/messages.mo i18n/en/LC_MESSAGES/messages.po

if __name__ == '__main__':
    application = app.App()
    application.mainloop()
