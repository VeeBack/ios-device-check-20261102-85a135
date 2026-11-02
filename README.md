# Temporary personal iOS build

Standalone disposable build repository. It is not an upstream fork and does not
modify the source repository. `source.zip` contains an OpenStop source snapshot
(including its original license) from the current local working files.

The workflow creates a release-mode device IPA without Apple signing credentials.
Download the Actions artifact, then sign/install it on Windows using your own
Apple Account and a sideloading tool. An unsigned IPA cannot be installed directly.

The test app has a separate bundle identifier and no Associated Domains capability.
It uses live OpenStreetMap (submitted answers make real edits) and the custom callback
`network.vee.openstop.test://oauth2`. OSM login requires an OAuth public client
registered on live OSM with this exact callback. Supply its client ID using
Run workflow; do not put Apple credentials in this repository.

After the IPA has been downloaded, the owner can delete this repository.
