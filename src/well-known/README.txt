Before launch, replace the two placeholders:
- apple-app-site-association: TEAMID = the Apple Developer Team ID of the paid account (also add the Associated Domains capability "applinks:littledaysparents.com" in Xcode).
- assetlinks.json: the SHA-256 of the Play app signing key (Play Console > Test and release > App integrity).
Until then the https://littledaysparents.com/join page still works: its button opens the app with littledays-app://join?code=...
